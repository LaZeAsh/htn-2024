import React, { useState } from "react";
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import axios from 'axios';

const SiriComponent = ({ onScoreUpdate }) => {
  const [isActive, setIsActive] = useState(false);

  const {
    transcript,
    listening,
    resetTranscript,
  } = useSpeechRecognition();

  const toggleSiri = async () => {
    if (!isActive) {
      startListening();
    } else {
      stopListening();
    }
  };

  const startListening = () => {
    setIsActive(true);
    SpeechRecognition.startListening({ continuous: true });
  };

  const stopListening = async () => {
    try {
      setIsActive(false);
      SpeechRecognition.stopListening();
      await sendTranscriptForAnalysis(transcript);
      resetTranscript();
    } catch (error) {
      console.error('Error during stopListening:', error);
    }
  };

  const sendTranscriptForAnalysis = async (transcript) => {
    try {
      const response = await axios.post('http://localhost:5001/analyze_transcript',
          { transcript }
      );
      
      if (typeof onScoreUpdate === 'function') {
        onScoreUpdate(response.data.score);
      } else {
        console.error('onScoreUpdate is not a function');
      }
    } catch (error) {
      console.error('Error sending transcript for analysis:', error);
    }
  };

  if (!SpeechRecognition.browserSupportsSpeechRecognition) {
    return <span>Your browser doesn't support Speech to Text</span>;
  }

  return (
    <div>
      <div onClick={toggleSiri} style={{ cursor: "pointer" }}>
        <img
          className="siri-component-image"
          alt="siri-state"
          src={isActive ? "images/active.gif" : "images/notactive.png"} 
        />
      </div>
    </div>
  );
};

export default SiriComponent;