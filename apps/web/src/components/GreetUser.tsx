

import React from 'react';

interface GreetUserProps {
  name?: string; 
}

const GreetUser: React.FC<GreetUserProps> = ({ name = 'Guest' }) => {
  return (
    <div style={{ padding: '1rem', textAlign: 'center' }}>
      <h2>Hello, {name}! Welcome to Recipe Hub.</h2>
    </div>
  );
};

export default GreetUser;