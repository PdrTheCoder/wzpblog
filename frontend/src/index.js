import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import "nes.css/css/nes.min.css";
import App from './App';
import Login from './Login';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Switch>
        <Route path="/login">
          <Login></Login>
        </Route>

        <Route path="/">
          <App></App>
        </Route>
      </Switch>
    </Router>
  </React.StrictMode>
);
