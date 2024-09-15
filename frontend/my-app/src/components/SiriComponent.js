import React, { useState } from "react";

const SiriComponent = () => {
  const [isActive, setIsActive] = useState(false);

  const toggleSiri = () => {
    setIsActive((prevState) => !prevState);
  };

  return (
    <div onClick={toggleSiri} style={{ cursor: "pointer" }}>
      <img
        className="siri-component-image"
        alt="siri-state"
        src={isActive ? "images/active.gif" : "images/notactive.png"} 
      />
    </div>
  );
};

export default SiriComponent;
