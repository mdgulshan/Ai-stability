import React, { useContext, useState} from 'react';
import 'aos/dist/aos.css';
import CustomDatePicker from '../DesktopDatePicker/CustomDatePicker';

function DatePicker(props) {
  
  return (
         props.labelText.map((text, index)=>{
          return (
            <CustomDatePicker
            key = {text} 
            label = {text} 
            value = {props.datePickerValue[text]}
            onChange = {(newValue)=>{props.setDataPickerValue({...props.datePickerValue, [text]:newValue})}}
            
            />
          )
        })   
  );
}

export default DatePicker;

  