import React from "react";
import styles from "./Loading.module.css";
import CircularProgress from '@mui/material/CircularProgress';

function Loading() {
  return (
    <div className={styles.backdrop}>
      <div className={styles.centreDiv}>
      <CircularProgress size={80} thickness={5}/>
        {/* <h1 className={styles.logo}>~Loading~</h1> */}
      </div>
    </div>
  );
}

export default Loading;
