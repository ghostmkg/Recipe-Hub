
import React from 'react';

interface FooterProps {
  year: number;
}

const Footer: React.FC<FooterProps> = ({ year }) => {
  return (
    <footer style={{ padding: '1rem', backgroundColor: '#333', color: 'white', textAlign: 'center', marginTop: 'auto' }}>
      <p>&copy; {year} Recipe Hub. All rights reserved.</p>
    </footer>
  );
};

export default Footer;