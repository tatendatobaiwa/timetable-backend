import React, { useEffect, useState } from 'react';
import rightarrow from "../../assets/right-arrow.png";
import backgroundImage from '../../assets/output-onlinepngtools.png';
import './Home.css'; 

const Home = () => {
  const [animate, setAnimate] = useState(false);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  
  useEffect(() => {
    const timer = setTimeout(() => {
      setAnimate(true);
    }, 100);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div
      className="container"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundAttachment: 'fixed',
      }}
    >
      <div className="thrive-container">
        <h1 className={`${animate ? 'fade-in' : 'pre-animate'}`}>
          Streamline your schedule. Effortlessly create, customize, and manage your perfect timetable
        </h1>
        <button 
              className={`button ${animate ? 'fade-in-delayed' : 'pre-animate'}`}
                >
                  Get Started
                  <img
                        src={rightarrow}
                        alt="right-arrow"
                        className="arrow-icon"
                        height="20"
                        width="20"
                        style={{ paddingLeft: '15px' }}
                      />
                    </button>
      </div>
    </div>
  );
};

export default Home;