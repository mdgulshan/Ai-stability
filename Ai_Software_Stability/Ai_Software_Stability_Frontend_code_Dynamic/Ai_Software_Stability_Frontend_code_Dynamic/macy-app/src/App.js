import React from "react";
import './App.css';
import { GraphDataContextProvider } from "./Contexts/GraphContext";
import GraphScreen from "./Layouts/GraphScreen/GraphScreen";

function App() {

  return (
    <div className="App">
      <GraphDataContextProvider>
        <GraphScreen/>
      </GraphDataContextProvider>
    </div>
  );
}

export default App;
