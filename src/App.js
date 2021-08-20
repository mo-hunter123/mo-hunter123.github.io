import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>
          FOR SALE
        </h1>
        <h2>Buy this premium domain</h2>
        <p>
          contact &nbsp;
          <a
            className="App-link"
            href="mailto:ahrrass.00@gmail.com?subject=Domain sale"
            target="_blank"
            rel="noopener noreferrer"
          >
            ahrrass.00@gmail.com
          </a>
          &nbsp;
          for more information
        </p>
        
      </header>
    </div>
  );
}

export default App;
