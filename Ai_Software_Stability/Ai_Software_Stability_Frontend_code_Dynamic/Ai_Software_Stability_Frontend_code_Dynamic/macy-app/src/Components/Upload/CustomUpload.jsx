import * as React from 'react';
import Button from '@mui/material/Button';


export default function UploadButton(props) {
  return (
      <Button variant="contained" component="label">
        {props.text}
        <input hidden multiple type="file" onChange={props.onChange} />
      </Button>
  );
}