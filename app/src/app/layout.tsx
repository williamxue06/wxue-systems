import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "Repbook | Gym Workout Log", description: "Record your sets. See your progress." };
export default function Layout({children}: Readonly<{children: React.ReactNode}>) { return <html lang="en"><body>{children}</body></html>; }
