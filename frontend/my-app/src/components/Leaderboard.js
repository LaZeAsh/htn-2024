import React from "react";

const Leaderboard = () => {
  return (
    <div className="leaderboard">
      <h2>LEADERBOARD 🏆</h2>
      <div className="leaderboard-items">
        <div className="leaderboard-item-2">
          <h3 className="rank">2nd</h3>
          <img src="/images/cropped_headshot.png" alt="Emma" />
          <h3>Emma</h3>
          <p className="score">1847</p>
        </div>
        <div className="leaderboard-item-1">
          <h3 className="rank">1st</h3>
          <img src="/images/cropped_headshot.png" alt="Aayush" />
          <h3>Aayush</h3>
          <p className="score">2430</p>
        </div>
        <div className="leaderboard-item-3">
          <h3 className="rank">3rd</h3>
          <img src="/images/cropped_headshot.png" alt="Ayush" />
          <h3>Ayush</h3>
          <p className="score">1674</p>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
