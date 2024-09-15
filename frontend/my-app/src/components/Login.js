import React from "react";

const Login = () => {

  return (
<div className="mobile-container">
      <div className="mobile-content">
        <div className="user-info">
          <img alt="profile-picture" src="images/cropped_headshot.png" />
          <p>Log Out</p>
        </div>

        <h1 className="record-title">Track your <br /> <span style={{fontWeight: "bold", fontSize: "3.5vh"}}>🔮 AURA! 🔮</span></h1>

        <p className="record-score"><span style={{fontWeight: "bold"}}>Score:</span> {currScore}</p>

        <div className="record-bottom-text">
          <p className="record-leaderboard-text">LEADERBOARD:</p>
          <p className="record-website-text">www.traura.ai</p>
        </div>
      </div>
    </div>
  );
};

export default Login;
