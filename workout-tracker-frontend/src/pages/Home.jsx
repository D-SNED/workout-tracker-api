import { useState } from "react";

const Home = () => {
  const [workoutType, setWorkoutType] = useState("");

  return (
    <div>
      <h1>Workout Tracker</h1>
      <p>What are you working out today?</p>
      <div className="home-buttons">
        <div className="button-container">
          <button>Push</button>
        </div>
        <div className="button-container">
          <button>Pull</button>
        </div>
        <div className="button-container">
          <button>Legs</button>
        </div>
      </div>
      <div className="button-container submit-button">
        <button>Create Workout</button>
      </div>
    </div>
  );
};

export default Home;
