import React from "react";
import { CartesianGrid, Legend, Tooltip, XAxis, YAxis, LineChart, Line} from "recharts";


export default function CustomLineChart(props) {
    return (
        <LineChart width={600} height={250} data={props.data}
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey={props.past === "true" ? "past_dates" : "Predicted_Date"} />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey={props.past === "true" ? "past_count" : "Predicted_Count"} stroke="#8884d8" />
            
          </LineChart>
    );
}