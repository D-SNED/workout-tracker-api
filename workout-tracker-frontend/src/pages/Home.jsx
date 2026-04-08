import { useState } from "react";
import { useNavigate } from "react-router";

const Home = () => {
  const [workoutType, setWorkoutType] = useState("");
  const [error, setError] = useState(false);
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
      <div className="submit-button button-container">
        <button
          onClick={() => {
            workoutType === "" ? setError(true) : navigate("/workout");
          }}
        >
          Create Workout
        </button>
        {error === true ? <p>Select a workout type to create</p> : null}
      </div>
    </div>
  );
};

export default Home;
