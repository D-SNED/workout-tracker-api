import { useState, useEffect } from "react";

export default function Workout() {
  console.log("workout component rendered");
  const [workouts, setWorkouts] = useState([]);

  async function fetchWorkouts() {
    const workoutRes = await fetch("/api/workouts/");
    const workoutJson = await workoutRes.json();

    console.log(workoutJson);
  }

  useEffect(() => {
    fetchWorkouts();
  }, []);

  return <div>hello</div>;
}
