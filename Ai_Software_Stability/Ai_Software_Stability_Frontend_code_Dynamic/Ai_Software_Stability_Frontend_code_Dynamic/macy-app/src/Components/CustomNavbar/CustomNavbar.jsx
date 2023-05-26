import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import styles from './CustomNavbar.module.css';



export default function CustomNavbar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar>
        <Toolbar>
          <img src="./images/logo.png"  style={{width : "210px"}}/>
          <Typography variant="h6" className={styles.header}>
            AI FOR SOFTWARE STABILITY
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}






