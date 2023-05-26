import * as React from 'react';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import CustomButton from '../Button/CustomButton';
import CustomUpload from '../Upload/CustomUpload';
import { Typography } from '@mui/material';
import {Stack} from '@mui/material';
import styles from './CustomDialog.module.css';
import Autocomplete from '@mui/material/Autocomplete';


export default function CustomDialog(props) {

 

  return (
    <div>
      <Dialog fullWidth open={props.open} onClose={props.onClose}>
        <DialogTitle>{props.heading}</DialogTitle>
        <DialogContent>
          <Stack direction="column" spacing={3}>
          <div className={styles.container}>
          <Typography variant="subtitle1" id={styles.labelText}>Select a File:</Typography>
          <CustomUpload
            onChange={props.onChange}
            text="Upload"
            />
              <Autocomplete
                          disablePortal
                          id="combo-box-demo"
                          onChange={props.handleChange}
                          options={props.options}
                          sx={{ width: 200 }}
                          renderInput={(params) => <TextField {...params} label="SiteName" />}
                          selectedvalue={props.selectedvalue}
                     />
          </div>
          {/* <Stack spacing={2} direction='row'>
          {props.hasTextfield === "true" && 
          
            props.editableData.map((formData,index)=>{
              return (
                <Stack key={index} spacing={2} direction='row'>
                  <Typography variant="subtitle1" id={styles.labelText}>{formData["name"]}:</Typography>
                  <TextField
                  variant='outlined'
                  size='small'
                  sx={{ m: 0, width: '120px' }}
                  {...formData}
                  />
                </Stack>
              );
            })
          }
          
        </Stack> */}
      
        </Stack>
        </DialogContent>
        
        <DialogActions>
            <CustomButton onClick={props.onClose}>Cancel</CustomButton>
            <CustomButton onClick={props.onClick}>Train</CustomButton>
        </DialogActions>

        <Typography 
        id={props.status === true ? styles.responseMessage : styles.errorResponseMessage}
        variant="caption" component="h2">{props.message}</Typography>

      </Dialog>
    </div>
  );
}
