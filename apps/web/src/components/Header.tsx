import React from 'react';

interface HeaderProps {
  title: string;
}

const Header: React.FC<HeaderProps> = ({ title }) => {
  return (
    <header style={{ padding: '1rem', backgroundColor: '#f0f0f0', textAlign: 'center' }}>
      <h1>{title}</h1>
      <nav>
        <a href="/" style={{ margin: '0 10px' }}>Home</a>
        <a href="/add" style={{ margin: '0 10px' }}>Add Recipe</a>
        <a href="/about" style={{ margin: '0 10px' }}>About</a>
      </nav>
    </header>
  );
};

export default Header;