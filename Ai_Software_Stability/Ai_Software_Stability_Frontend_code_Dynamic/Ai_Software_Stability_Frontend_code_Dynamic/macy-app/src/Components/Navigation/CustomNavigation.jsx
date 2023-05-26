import React, {useState} from 'react';
import Stack from '@mui/material/Stack';
import CustomButton from '../Button/CustomButton';
import styles from '../Navigation/CustomNavigation.module.css';


export default function CustomNavigation(props) {

  return (
    <>
      {props.buttonText.map((button,index)=>{
        return (
          <CustomButton
           key={index}
           onClick={props.onChange[index]}
          //  style={styles.buttonStyle}
           >
            {button}
          </CustomButton>
        );
      })}
    </>
  );
}
