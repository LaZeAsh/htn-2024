import React from "react";

const Leaderboard = () => {
  return (
    <div className="leaderboard">
      <h2>LEADERBOARD</h2>
      <div className="leaderboard-items">
        <div className="leaderboard-item-2">
          <h3 className="rank">2nd</h3>
          <img src="/images/cropped_headshot.png" alt="Jackson" />
          <h3>Jackson</h3>
          <p className="score">1847</p>
        </div>
        <div className="leaderboard-item-1">
          <h3 className="rank">1st</h3>
          <img src="/images/cropped_headshot.png" alt="Eiden" />
          <h3>Eiden</h3>
          <p className="score">2430</p>
        </div>
        <div className="leaderboard-item-3">
          <h3 className="rank">3rd</h3>
          <img src="/images/cropped_headshot.png" alt="Emma Aria" />
          <h3>Emma Aria</h3>
          <p className="score">1674</p>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
