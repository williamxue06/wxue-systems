export const KEY = "gym-workout-log:v1";
export type Entry = { id: string; exercise: string; weightLb: number; reps: number; createdAt: string };
export function validate(exercise: string, weight: string, reps: string) {
  const errors: Record<string,string> = {};
  if (!exercise.trim() || exercise.trim().length > 80) errors.exercise = "Enter an exercise name (1–80 characters).";
  if (!weight.trim() || !Number.isFinite(Number(weight)) || Number(weight) < 0 || Number(weight) > 2000 || !/^\d+(\.\d{1,2})?$/.test(weight.trim())) errors.weight = "Enter a weight from 0 to 2000 lb, with up to two decimals.";
  if (!reps.trim() || !/^\d+$/.test(reps.trim()) || Number(reps) < 1 || Number(reps) > 1000) errors.reps = "Enter a whole number of reps from 1 to 1000.";
  return errors;
}
export function readEntries(raw: string | null): Entry[] {
  if (raw === null) return [];
  const data = JSON.parse(raw);
  if (data?.version !== 1 || !Array.isArray(data.entries)) throw new Error("Invalid saved data");
  const ids = new Set<string>();
  for (const e of data.entries) {
    if (!e || typeof e.id !== "string" || !e.id || ids.has(e.id) || typeof e.exercise !== "string" || e.exercise !== e.exercise.trim() || typeof e.weightLb !== "number" || typeof e.reps !== "number" || typeof e.createdAt !== "string" || !Number.isFinite(Date.parse(e.createdAt)) || Object.keys(validate(e.exercise,String(e.weightLb),String(e.reps))).length) throw new Error("Invalid saved entry");
    ids.add(e.id);
  }
  return data.entries.sort((a: Entry,b: Entry) => Date.parse(b.createdAt)-Date.parse(a.createdAt));
}
export function persist(storage: Pick<Storage,"setItem">, entries: Entry[]) {
  storage.setItem(KEY, JSON.stringify({version:1, entries}));
}
