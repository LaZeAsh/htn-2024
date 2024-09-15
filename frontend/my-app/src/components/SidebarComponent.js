import React from "react";

const SidebarComponent = () => {
  return (
    <div className="sidebar-component">
      <div className="sidebar-component-profile">
        <img src="images/cropped_headshot.png" alt="user"></img>
        <div className="sidebar-component-profile-text">
          <h3>Aayush</h3>
          <p>1st Place</p>
        </div>
        <div style={{flex: 1}}></div>
        <p className="sidebar-component-score">1124</p>
      </div>
      <hr className="sidebar-component-horizontal-line"></hr>
    </div>
  );
};

export default SidebarComponent;
