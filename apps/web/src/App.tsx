import React from 'react';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';

const App: React.FC = () => {
  return (
    <div className="App">
      <Header title="Recipe Hub" />
      <main>
        <h1>Welcome to Recipe Hub!</h1>
        <p>This is a placeholder for the main content. Dependencies for routing were not installed.</p>
      </main>
      <Footer year={new Date().getFullYear()} />
    </div>
  );
};

export default App;
