import React from "react";
import { Link } from "react-router-dom";
import mailIcon from "../../assets/mail.png";
import phoneIcon from "../../assets/call.png";
import linkedinIcon from "../../assets/linkedin.png";
import biclogo from "../../assets/biclogo.png";
import './Footer.css';

const Footer = () => {
  return (
    <footer>
      <div className="container">
        <div className="footer-content">
          <div className="footer-wrapper">
            {/* Contact Information */}
            <div className="footer-column">
              <h4 className="footer-heading">Get in touch</h4>
              <div className="contact-info">
                <div className="contact-item">
                  <img src={mailIcon} alt="Mail Icon" className="icon" height="30" width="30" />
                  <span>biustinnovationclub&#64;gmail.com</span>
                </div>
                <div className="contact-item">
                  <img src={phoneIcon} alt="Phone Icon" className="icon" height="30" width="30" />
                  <span>+267 XX XXX XXX</span>
                </div>
              </div>
            </div>
            {/* Office Locations */}
            <div className="footer-column">
              <h4 className="footer-heading">Location</h4>
              <div className="offices-info">
                <p>
                  BIUST Campus
                  <br />
                  Palapye
                  <br />
                  Botswana
                </p>
              </div>
            </div>
            {/* Social Media Links */}
            <div className="footer-column">
              <h4 className="footer-heading">Follow us</h4>
              <ul className="social-icons">
                <li>
                  <a 
                    href="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley" 
                    target="_blank" 
                    rel="noopener noreferrer"
                  >
                    <img src={linkedinIcon} alt="LinkedIn logo" height="30" width="30" />
                  </a>
                </li>
              </ul>
            </div>

            <div className="footer-column">
              <ul className="bic-logo">
                    <img src={biclogo} alt="Bic logo"/>
              </ul>
            </div>
          </div>

          {/* Footer Bottom */}
          <div className="footer-bottom">
            <p>
              © 2024 BIUST Innovation Club. All Rights Reserved | {" "}
              <Link to="/terms-of-use">Terms of Use</Link>
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;