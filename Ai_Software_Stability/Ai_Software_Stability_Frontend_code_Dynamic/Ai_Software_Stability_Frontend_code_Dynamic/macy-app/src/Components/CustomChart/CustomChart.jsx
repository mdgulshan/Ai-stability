import React, { useState } from "react";
import {Paper} from "@mui/material";
import {
    ResponsiveContainer,
    Cell,
    PieChart,
    Pie,
    LabelList,
    Legend, Tooltip
  } from "recharts";
import CustomAutocomplete from "../Autocomplete/CustomAutocomplete";


  const dummyData = [
    { name: 'DB issue', value: 40 },
    { name: 'Printer Failure', value: 30 },
    { name: 'Order Stuck', value: 15 },
    { name: 'DB1 connection issue', value: 15 },
];


export default function CustomChart() {
    const options = ["ABC","BCD","CDE","DEF","EFG"];
    const [lineValue, setLineValue] = useState();
    const [inputValue, setInputValue] = useState();

    const renderCustomizedLabelPercentage = (dummyData, total = 1) => {
        
        let percentageCalculated = (dummyData.value);
        
        return percentageCalculated.toString() +" "+ "%";
        
      };
    
      const customColors = ["#2980B9", "#73C6B6", "#512E5F", "#546E7A ", "#003f5c"];

      const onHandleChange = (event, newInputValue) => {
        setInputValue(newInputValue);
    
      }

      const onHandle = (event, newValue) => {
        setLineValue(newValue);
      }



    return (
        <Paper
        sx={{
            p: 2,
            display: 'flex',
            flexDirection: 'column',
            height: 400,
        }}
        >
            
            <CustomAutocomplete label="Select" options={options} inputValue={inputValue} onInputChange={onHandleChange} value={lineValue} onChange={onHandle}/>
            
            <ResponsiveContainer>
                            <PieChart>
                                <Pie
                                    data={dummyData}
                                    color="#000000"
                                    dataKey="value"
                                    nameKey="name"
                                    cx="50%"
                                    cy="50%"
                                    outerRadius={120}
                                    fill="#8884d8"
                                >
                                    <LabelList
                                    dy={-3}
                                    fill="white" // Percentage color
                                    // dataKey="percentage"
                                    dataKey={renderCustomizedLabelPercentage}
                                    position="inside"
                                    angle="0"
                                    stroke="none" // Border of letters
                                    className="label-percentage"
                                    />
                                    {dummyData.map((entry, index) => (
                                        <Cell
                                            key={`cell-${index}`}
                                            fill={customColors[index % customColors.length]}
                                        />
                                    ))}
                                </Pie>
                                <Tooltip />
                                <Legend verticalAlign="top" height={36} iconSize={10} />
                            </PieChart>
                        </ResponsiveContainer>
    </Paper>
    );
}