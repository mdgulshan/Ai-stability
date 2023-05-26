import React, { useContext, useState} from 'react';
import 'aos/dist/aos.css';
import dayjs from 'dayjs';
import Stack from '@mui/material/Stack';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
// import { LocalizationProvider } from '@mui/x-date-pickers-pro';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { CardActionArea } from '@mui/material';
import { forecastData } from '../../Middlewares/GraphMiddleware';
import CustomButton from '../Button/CustomButton';
import CustomDatePicker from '../DesktopDatePicker/CustomDatePicker';
import CustomAutocomplete from '../Autocomplete/CustomAutocomplete';
import {GraphContext} from '../../Contexts/GraphContext';
import DropDownField from '../../Utils/DropDownField.json';


function DatePicker() {
  // const [startDate, setStartDate] = React.useState(dayjs('2022-11-01'));
  // const [endDate, setEndDate] = useState(dayjs('2022-11-28'));
  // const [firstValue, setFirstValue] = useState(null);
  const [inputValue, setInputValue] = useState("");
  const siteName = ["MLO-050  MLO - Portland", "MLO-869 MLO - Tulsa", "MLO-506 MLO - Goodyear","MLO-043 MLO - West Virginia","MLO-500 MLO - Cheshire"];
  const applicationFunction = ["WMS MA", "Ship On Time (SOT)"]
  // const [secondValue, setSecondValue] = useState(null);
  const [InputValueNew, setInputValueNew] = useState("");
  const [datePickerValue, setDataPickerValue] = useState({StartDate : new Date(), EndDate : new Date()});
  const {predictionData, setPredictionData} = useContext(GraphContext);
  const [dropDownOne, setDropDownOne] = useState({firstValue:null, secondValue:null});
  const [dropDownTwo, setDropDownTwo] = useState({inputValueOne:null, inputValueTwo:null});



  // const handleChange = (newValue) => {
  //   setStartDate(newValue);
  //   // setDataPickerValue.Start_Date=newValue;
    
  // };

  // const handleChangeEnd = (newValue) => {
  //   setEndDate(newValue);
  //   // setDataPickerValue.End_Date=newValue;
  // };

  // const onForecast = async(event) => {
  //   let dropdownValue;

  //   if (firstValue) {
  //     dropdownValue = firstValue;
  //   } else {
  //     dropdownValue = secondValue;
  //   }
   
  //   const response = await forecastData(event, startDate, endDate, dropdownValue);
  //   setPredictionData(response);
  //   console.log(predictionData);
  //   console.log(startDate);
  //   console.log(endDate);
   
  //   console.log(dropdownValue)
   
  //   return response;
  // }

  const onForecast = async(event) => {
    let dropdownValue;

    if (dropDownOne["firstValue"]) {
      dropdownValue = dropDownOne["firstValue"];
    } else {
      dropdownValue = dropDownOne["secondValue"];
    }
   
    const response = await forecastData(event, datePickerValue['Start Date'], datePickerValue['End Date'], dropdownValue);
    setPredictionData(response);
    console.log(predictionData);
    console.log(dropDownOne["firstValue"]);
    console.log(dropDownOne["secondValue"]);
    console.log(dropdownValue)
   
    return response;
  }


  const labelText = ['StartDate', 'EndDate'];

  const dropDownItems = [siteName, applicationFunction]

  const inputNames = ['firstValue', 'secondValue']


  return (
    <Card sx={{ maxWidth: 1500}} style={{backgroundColor:'whitesmoke'}}>
        <CardActionArea>
            <CardContent>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
                    <Stack spacing={10} direction="row">
                      {labelText.map((text, index)=>{
                        return (
                          <CustomDatePicker
                          key = {text} 
                          label = {text} 
                          value = {datePickerValue[text]}
                          onChange = {(date)=>{setDataPickerValue({...datePickerValue, [text]:date})}}
                          />
                        )
                      })}


                      {/* <CustomDatePicker label="Start date" value={startDate} onChange={handleChange}/> */}
                      {/* <CustomDatePicker label="End date" value={endDate} onChange={handleChangeEnd}/> */}

                      <CustomAutocomplete/>

                      {/* {inputNames.map((data,index) => {
                        return (
                          <CustomAutocomplete
                          key = {data}
                          options = {dropDownItems[index]}
                          inputValue = {dropDownTwo[data]}
                          onInputChange={(event,newInputValue)=>{setDropDownTwo({...dropDownTwo,[data]:newInputValue});}}
                          value={dropDownOne[data]}
                          onChange={(event,newValue)=>{setDropDownOne({...dropDownOne,[data]:newValue})}}
                          />

                        );
                      })} */}

                      {/* <CustomAutocomplete 
                      label="Select" 
                      options={siteName} 
                      inputValue={inputValue} 
                      onInputChange={(event,newInputValue) => {setInputValue(newInputValue)}} 
                      value={firstValue} 
                      onChange={(event,newValue) => {setFirstValue(newValue)}}
                      statement={secondValue} 
                      />
                      
                      <CustomAutocomplete 
                      label="Select" 
                      options={applicationFunction} 
                      inputValue={InputValueNew} 
                      onInputChange={(event,newInputValue) => {setInputValueNew(newInputValue)}} 
                      value={secondValue} 
                      onChange={(event, newValue) => {setSecondValue(newValue)}}
                      statement={firstValue}
                      /> */}
                    
                     
                      <CustomButton onClick={(event)=>{onForecast(event)}}>Forecast</CustomButton>
                    </Stack>
                </LocalizationProvider>
            </CardContent>
        </CardActionArea>
    </Card>
  );
}

export default DatePicker;

  