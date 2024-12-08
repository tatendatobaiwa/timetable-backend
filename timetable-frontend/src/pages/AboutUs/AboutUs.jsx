import React, { useEffect } from 'react';
import './AboutUs.css';

const AboutUs = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  return (
    <div className="about-us-container">
      <div className="about-us-content">
        <h1>About BIUST Innovation Club</h1>
        <p>
          The BIUST Innovation Club is a forward-thinking initiative aimed at fostering creativity, research, and entrepreneurship in Botswana. As part of the Botswana International University of Science and Technology (BIUST), the club focuses on providing an environment that nurtures innovation and supports individuals who are passionate about technology and business solutions.
        </p>
        <h2>Our Mission</h2>
        <p>
          Our mission is to empower students, researchers, and innovators to bring their ideas to life through access to resources, mentorship, and collaboration with industry leaders. By providing a conducive space for technological advancement, we aim to contribute to the development of sustainable solutions for the challenges facing Botswana and the world.
        </p>
        <h2>Why This Web App Was Created</h2>
        <p>
          This web application was created with the purpose of simplifying the process of managing academic schedules for BIUST students and staff. With a user-friendly interface and dynamic features, the app helps users efficiently create, manage, and access timetables, ensuring a smooth and organized academic experience.
        </p>
      </div>
    </div>
  );
};

export default AboutUs;
