import React, { useState } from 'react';
import './App.css'; // Assuming you have a CSS file for styling
import Header from './web/';
import Footer from './components/Footer';
import GreetUser from './GreetUser.tsx';

interface AppProps {
  appName: string;
}

const App: React.FC<AppProps> = ({ appName }) => {
  const [count, setCount] = useState<number>(0);

  const incrementCount = () => {
    setCount(prevCount => prevCount + 1);
  };

  const decrementCount = () => {
    setCount(prevCount => (prevCount > 0 ? prevCount - 1 : 0));
  };

  return (
    <div className="App">
      <Header title={appName} />
      <main>
        <GreetUser name="Alice" />
        <p>Current Count: {count}</p>
        <button onClick={incrementCount}>Increment</button>
        <button onClick={decrementCount}>Decrement</button>
      </main>
      <Footer year={new Date().getFullYear()} />
    </div>
  );
};

export default App;