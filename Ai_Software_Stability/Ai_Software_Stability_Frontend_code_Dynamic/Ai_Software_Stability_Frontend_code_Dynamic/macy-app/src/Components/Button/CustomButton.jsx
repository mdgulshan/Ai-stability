import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import { Box } from '@mui/material';

export default function CustomButton(props) {

  return (
    <div style={{display:"flex"}}>
      <Button 
      variant="contained"
      size = "medium" 
      onClick={props.onClick}
      sx={props.style}
      
      >
        {props.children}
      </Button>
    </div>
  );
}
