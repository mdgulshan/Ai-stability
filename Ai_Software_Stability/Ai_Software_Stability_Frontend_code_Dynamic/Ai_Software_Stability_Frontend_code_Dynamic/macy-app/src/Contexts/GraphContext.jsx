import React from "react";
import { createContext, useState } from "react";

export const GraphContext = createContext();

export function GraphDataContextProvider(props) {

 
 const [selectedValues, setSelectedValues] = useState([false,false]);
 const [loading, setLoading] = useState(false);


return (
    <GraphContext.Provider value={{selectedValues,setSelectedValues,loading,setLoading}}>
        {props.children}
    </GraphContext.Provider>
      
);

}