import React,{useContext, useState} from "react";
import {Paper, Stack, Typography} from "@mui/material";
import CustomAutocomplete from "../Autocomplete/CustomAutocomplete";
import CustomLineChart from "../LineChart/CustomLineChart";
import { GraphContext } from "../../Contexts/GraphContext";
import styles from './CustomGraph.module.css';



const data = [
  {
    "name": "Page A",
    "uv": 4000,
    "pv": 2400,
    "amt": 2400
  },
  {
    "name": "Page B",
    "uv": 3000,
    "pv": 1398,
    "amt": 2210
  },
  {
    "name": "Page C",
    "uv": 2000,
    "pv": 9800,
    "amt": 2290
  },
  {
    "name": "Page D",
    "uv": 2780,
    "pv": 3908,
    "amt": 2000
  },
  {
    "name": "Page E",
    "uv": 1890,
    "pv": 4800,
    "amt": 2181
  },
  {
    "name": "Page F",
    "uv": 2390,
    "pv": 3800,
    "amt": 2500
  },
  {
    "name": "Page G",
    "uv": 3490,
    "pv": 4300,
    "amt": 2100
  }
]

export default function CustomGraph(props) {
  const options = ["ABC","BCD","CDE","DEF","EFG"];
  const [lineValue, setLineValue] = useState();
  const [inputValue, setInputValue] = useState();
  

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
            height: 350,
        }}
        >
          <Stack spacing={0} direction="row">
            <Stack spacing={3} direction="column">
            <Typography variant="h6" className={styles.header}>Historical Trend</Typography>
            <CustomLineChart data = {props.predictionData} past="true"/>
            </Stack>
            <Stack spacing={3} direction="column">
            <Typography variant="h6" className={styles.header}>Forecasted Trend</Typography>
            <CustomLineChart data = {props.predictionData} past="false"/>
            </Stack>
          </Stack>
    </Paper>
    );
}