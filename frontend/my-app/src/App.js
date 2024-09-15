import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./components/Home";
import RecordingPage from "./components/RecordingPage";


function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/record" element={<RecordingPage />} />
        <Route path="*" element={<Home />} />
      </Routes>
    </BrowserRouter>

  );
}

export default App;