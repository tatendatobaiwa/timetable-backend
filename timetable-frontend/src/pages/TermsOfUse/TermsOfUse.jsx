import React, { useEffect } from 'react';
import './TermsOfUse.css';

const TermsOfUse = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="terms-of-use-container">
      <div className="terms-of-use-content">
      <h1>Terms of Use</h1>

      <p>Welcome to Schedule Master! By using Schedule Master ("the Service"), you agree to these Terms of Use. If you do not agree with these terms, please do not use the Service.</p>

      <h2>1. Acceptance of Terms</h2>
      <p>By accessing or using the Service, you confirm that you accept these Terms of Use. If you are using the Service on behalf of an organization, you represent that you have the authority to bind the organization to these Terms.</p>

      <h2>2. Eligibility</h2>
      <p>You must be at least 16 years old or the age of majority in your jurisdiction to use this Service. By using Schedule Master, you confirm that you meet this eligibility requirement.</p>

      <h2>3. User Responsibilities</h2>
      <p>You agree to use the Service only for lawful purposes. You will not:</p>
      <ul>
        <li>Input false or misleading data.</li>
        <li>Use the Service in a way that violates any applicable laws.</li>
        <li>Distribute harmful software or malware.</li>
        <li>Engage in any activity that could damage or disrupt the Service.</li>
      </ul>

      <h2>4. Description of the Service</h2>
      <p>Schedule Master is a tool that allows users to input their modules and generate a personalized timetable. The Service is entirely free to use and provides users with the ability to schedule and organize their academic activities. We may modify or discontinue any aspect of the Service at any time.</p>

      <h2>5. Privacy and Data Collection</h2>
      <p>Your use of Schedule Master is governed by our <strong>Privacy Policy</strong>. By using the Service, you consent to the collection and use of your data as described in the Privacy Policy.</p>

      <h2>6. Prohibited Uses</h2>
      <p>You agree not to:</p>
      <ul>
        <li>Use the Service in any manner that could interfere with or damage its functionality.</li>
        <li>Attempt to reverse-engineer or decompile the Service.</li>
        <li>Use the Service for unauthorized commercial purposes.</li>
      </ul>

      <h2>7. Termination</h2>
      <p>We may suspend or terminate your account if we believe you have violated these Terms. You may also terminate your account at any time by following the account termination procedure in the settings.</p>

      <h2>8. Limitation of Liability</h2>
      <p>Schedule Master is provided "as is" and we do not make any representations or warranties about the accuracy or reliability of the Service. We are not liable for any indirect, incidental, or consequential damages arising from your use of the Service.</p>

      <h2>9. Changes to Terms</h2>
      <p>We may update these Terms from time to time. We will notify users of any significant changes. By continuing to use the Service, you accept the updated Terms.</p>

      <h2>10. Contact Information</h2>
      <p>For any questions regarding these Terms, please contact us at: <strong>+267 XX XXX XXX</strong></p>
      </div>
    </div>
  );
};

export default TermsOfUse;
