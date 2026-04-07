import { BrowserRouter, Routes, Route } from "react-router";
import Home from "./pages/Home";
import Summary from "./pages/Summary";
import WorkoutPage from "./pages/WorkoutPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/workout" element={<WorkoutPage />} />
        <Route path="/summary" element={<Summary />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
