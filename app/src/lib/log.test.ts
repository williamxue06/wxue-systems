import { describe,it,expect } from "vitest";
import {validate,readEntries,persist} from "./log";
const entry={id:"one",exercise:"Cable lateral raise",weightLb:17.5,reps:10,createdAt:"2026-11-19T18:00:00.000Z"};
describe("validation",()=>{
 it("accepts zero and fractional weights",()=>{expect(validate("Push up","0","12")).toEqual({});expect(validate("Raise","17.5","10")).toEqual({});});
 it("rejects blank, out-of-range and fractional reps",()=>{expect(Object.keys(validate(" ","-1","1.5"))).toHaveLength(3);expect(validate("Raise","","0")).toHaveProperty("weight");expect(validate("Raise","1.234","1001")).toHaveProperty("reps");});
});
describe("storage",()=>{
 it("round-trips entries without merging identical sets",()=>{let raw:string|null=null;persist({setItem:(_k,v)=>{raw=v;}},[entry,{...entry,id:"two"}]);expect(readEntries(raw)).toHaveLength(2);expect(readEntries(raw)[0]).toEqual(entry);});
 it("rejects corrupted data and invalid saved values",()=>{expect(()=>readEntries("bad")).toThrow();expect(()=>readEntries(JSON.stringify({version:1,entries:[{...entry,reps:-1}]}))).toThrow();});
 it("propagates write failures so UI cannot report success",()=>{expect(()=>persist({setItem:()=>{throw new Error("full");}},[entry])).toThrow("full");});
 it("sorts newest first and handles empty storage",()=>{expect(readEntries(null)).toEqual([]);expect(readEntries(JSON.stringify({version:1,entries:[entry,{...entry,id:"two",createdAt:"2026-11-20T18:00:00.000Z"}]}))[0].id).toBe("two");});
});
