import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./style.css";
import App from "./App.jsx";
import Workout from "./WorkoutPage.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
    <Workout />
  </StrictMode>,
);
