import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [books, setCurrentBook] = useState(0)

  useEffect(()=>{
    fetch('/book').then(res => res.json()).then(data =>{
      setCurrentBook(data.title)
    })

  },[]);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
          <h1> the current time is {books}.</h1>
        </a>
      </header>
    </div>
  );
}

export default App;
