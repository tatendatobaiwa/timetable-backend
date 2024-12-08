import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Settings.css';

const Settings = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [language, setLanguage] = useState('en');

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
    document.body.style.backgroundColor = isDarkMode ? '#fff' : '#030303'; // Adjust body bg color
  };

  const handleLanguageChange = (e) => {
    setLanguage(e.target.value);
    // Optionally, add logic to switch app content based on language
  };

  return (
    <div className={`settings-container ${isDarkMode ? 'dark-mode' : ''}`}>
      <div className="settings-header">
        <h1>Settings</h1>
      </div>
            <div className="settings-item">
        <h2>Appearance (Under Construction!) </h2>
        <div className="switch-container">
            <label className="switch">
            <input type="checkbox" checked={isDarkMode} onChange={toggleDarkMode} />
            <span className="slider round"></span>
            </label>
            <span className="mode-label">{isDarkMode ? 'Dark Mode' : 'Light Mode'}</span>
        </div>
        </div>
      <div className="settings-item">
        <h2>Language (Under Construction!)</h2>
        <select value={language} onChange={handleLanguageChange}>
          <option value="en">English (UK)</option>
          <option value="ts">Setswana</option>
        </select>
      </div>

      <div className="settings-item" style={{marginBottom:'4rem'}}>
        <h2>About Us</h2>
        <Link to="/about-us" className="about-us-link">Learn more about us</Link>
      </div>
    </div>
  );
};

export default Settings;
