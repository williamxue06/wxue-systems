"use client";
import { useEffect, useRef, useState } from "react";
import { KEY, Entry, readEntries, persist, validate } from "../lib/log";
export default function Home() {
 const [entries,setEntries]=useState<Entry[]>([]), [ready,setReady]=useState(false), [blocked,setBlocked]=useState(false);
 const [exercise,setExercise]=useState(""), [weight,setWeight]=useState(""), [reps,setReps]=useState("");
 const [errors,setErrors]=useState<Record<string,string>>({}), [message,setMessage]=useState(""), [failure,setFailure]=useState("");
 const repsInput=useRef<HTMLInputElement>(null);
 useEffect(()=>{try{setEntries(readEntries(localStorage.getItem(KEY)));}catch{setBlocked(true);setFailure("Your saved log could not be read. Logging is paused to protect your data. Your existing saved data has not been changed.");}finally{setReady(true);}},[]);
 function save(event: React.FormEvent<HTMLFormElement>) {
  event.preventDefault(); setMessage(""); setFailure(""); const nextErrors=validate(exercise,weight,reps); setErrors(nextErrors);
  if(Object.keys(nextErrors).length || !ready || blocked) return;
  const entry: Entry={id:crypto.randomUUID(),exercise:exercise.trim(),weightLb:Number(weight),reps:Number(reps),createdAt:new Date().toISOString()};
  const next=[entry,...entries];
  try{persist(localStorage,next);setEntries(next);setReps("");setMessage(`${entry.exercise}: ${entry.weightLb} lb × ${entry.reps} reps saved.`);repsInput.current?.focus();}
  catch{setFailure("Could not save this set. Your browser storage may be blocked or full. Your inputs are still here; try again.");}
 }
 const days=new Set(entries.map(e=>new Date(e.createdAt).toLocaleDateString())).size;
 return <main>
  <header><a className="brand" href="/" aria-label="Repbook home"><span className="brand-icon">▥</span> repbook<span className="brand-dot">.</span></a><span className="header-note">YOUR TRAINING, ON RECORD</span></header>
  <section className="intro"><p className="eyebrow">ONE SET AT A TIME</p><h1>Show up.<br/><span>Write it down.</span></h1><p className="lede">Less guessing. More progress. Keep a simple record of the work you put in.</p></section>
  <section className="workspace" aria-label="Gym workout log">
   <div className="form-card"><div className="section-top"><span className="eyebrow">TODAY’S WORK</span><span className="tag">WORKOUT LOG</span></div><h2>Log a set</h2><p className="muted">A few numbers. A little more progress.</p>
    <form onSubmit={save} noValidate>
     <label htmlFor="exercise">Exercise</label><input id="exercise" value={exercise} maxLength={80} placeholder="e.g. Dumbbell chest press" onChange={e=>setExercise(e.target.value)} aria-invalid={!!errors.exercise} aria-describedby={errors.exercise?"exercise-error":undefined}/>{errors.exercise&&<p id="exercise-error" className="error">{errors.exercise}</p>}
     <div className="fields"><div><label htmlFor="weight">Weight <span className="muted">(lb)</span></label><input id="weight" type="text" inputMode="decimal" value={weight} placeholder="0" onChange={e=>setWeight(e.target.value)} aria-invalid={!!errors.weight} aria-describedby={errors.weight?"weight-error":undefined}/>{errors.weight&&<p id="weight-error" className="error">{errors.weight}</p>}</div><div><label htmlFor="reps">Reps</label><input id="reps" ref={repsInput} type="text" inputMode="numeric" value={reps} placeholder="0" onChange={e=>setReps(e.target.value)} aria-invalid={!!errors.reps} aria-describedby={errors.reps?"reps-error":undefined}/>{errors.reps&&<p id="reps-error" className="error">{errors.reps}</p>}</div></div>
     <button disabled={!ready||blocked} type="submit">＋ Save set</button>
     <p role="status" className="success">{message}</p>{failure&&<p role="alert" className="error">{failure}</p>}
    </form><div className="storage-note"><span aria-hidden="true">◈</span><p>Saved in this browser only.<br/><span>Use the same browser to find your history. Clearing browser data removes your log.</span></p></div>
   </div>
   <div className="history-panel"><div className="history-heading"><div><p className="eyebrow">THE WORK ADDS UP</p><h2>Your history</h2></div><span className="count">{entries.length} {entries.length===1?"set":"sets"} · {days} {days===1?"day":"days"}</span></div>
    {!ready?<p className="empty">Loading your log…</p>:entries.length===0?<div className="empty"><span className="empty-icon" aria-hidden="true">▥</span><h3>Your first set starts here.</h3><p>Log an exercise and your numbers.<br/>Next time, you’ll know where you left off.</p></div>:<ul className="history">{entries.map(e=><li key={e.id}><div><h3>{e.exercise}</h3><time dateTime={e.createdAt}>{new Date(e.createdAt).toLocaleString(undefined,{month:"short",day:"numeric",year:"numeric",hour:"numeric",minute:"2-digit"})}</time></div><div className="numbers"><strong>{e.weightLb}<small> lb</small></strong><span>×</span><strong>{e.reps}<small> reps</small></strong></div></li>)}</ul>}
   </div>
  </section><footer><span>BUILT FOR THE NEXT REP.</span><span>Keep it simple. Keep showing up.</span></footer>
 </main>;
}
