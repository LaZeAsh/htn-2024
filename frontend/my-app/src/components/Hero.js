import React from "react";
import Leaderboard from "./Leaderboard";
import Sidebar from "./Sidebar";
import SiriComponent from "./SiriComponent";

const Hero = () => {
  return (
    <div className="hero">
      <div className="main-body">
        <Leaderboard />
        <div className="vertical-line"></div>
        <Sidebar />
      </div>
    </div>
  );
};

export default Hero;
