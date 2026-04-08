import { useState } from "react";
import { useNavigate } from "react-router";

const Home = () => {
  const [workoutType, setWorkoutType] = useState("");
  const navigate = useNavigate();

  return (
    <div>
      <h1>Workout Tracker</h1>
      <p>What are you working out today?</p>
      <div className="home-buttons">
        <div className="button-container">
          <button
            className={workoutType === "push" ? "button-active" : ""}
            onClick={() => setWorkoutType("push")}
          >
            Push
          </button>
        </div>
        <div className="button-container">
          <button
            className={workoutType === "pull" ? "button-active" : ""}
            onClick={() => setWorkoutType("pull")}
            value="Pull"
          >
            Pull
          </button>
        </div>
        <div className="button-container">
          <button
            className={workoutType === "legs" ? "button-active" : ""}
            onClick={() => setWorkoutType("legs")}
            value="Legs"
          >
            Legs
          </button>
        </div>
      </div>
      <div className="button-container submit-button">
        <button
          onClick={() => {
            workoutType === "" ? console.log("what") : navigate("/workout");
          }}
        >
          Create Workout
        </button>
      </div>
    </div>
  );
};

export default Home;
