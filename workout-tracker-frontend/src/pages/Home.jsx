import { useState } from "react";

const Home = () => {
  const [workoutType, setWorkoutType] = useState("");

  return (
    <div>
      <h1>Workout Tracker</h1>
      <p>What are you working out today?</p>
      <div className="home-buttons">
        <button>Push</button>
        <button>Pull</button>
        <button>Legs</button>
      </div>
      <div>
        <button>Create Workout</button>
      </div>
    </div>
  );
};

export default Home;
