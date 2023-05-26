import React from "react";
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker';
import { TextField } from "@mui/material";
import { makeStyles } from '@material-ui/core/styles';


const useStyles = makeStyles({
    datePicker: {
      width: '150px', 

    },
  });


export default function CustomDatePicker(props) {
    const classes = useStyles();
    return (
      
        <DesktopDatePicker
        className={classes.datePicker} 
        label={props.label}
        inputFormat="YYYY/MM/DD"
        value={props.value}
        onChange={props.onChange}
        renderInput={(params) => <TextField size="small" {...params} />}
        />
    );
}