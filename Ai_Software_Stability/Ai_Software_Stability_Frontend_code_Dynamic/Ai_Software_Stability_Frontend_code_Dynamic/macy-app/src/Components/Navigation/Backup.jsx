import React, {useState} from 'react';
import Stack from '@mui/material/Stack';
import CustomButton from '../Button/CustomButton';
import CustomDialog from '../Dialog/CustomDialog';
import trainForecast, { analysis } from '../../Middlewares/GraphMiddleware';

export default function CustomNavigation() {
  const [open, setOpen] = useState(false);
  const [modalOpen, setModalOpen] = React.useState(false);
  const [file, setFile] = useState(null);
  const [files, setFiles] = useState(null);
  const [lookBack, setlookBack] = useState(null);
  const [futurePrediction, setFuturePrediction] = useState(null);
  const [message, setMessage] = useState(null);
  const [status, setStatus] = useState(false);

  const handleClick = () => {
    setOpen(true);
    console.log(open)

  }

  const handleClickOpen = () => {
    setModalOpen(true);
  }

  const handleClose = () => {
    setOpen(false);

  }

  const handleCloseModal = () => {
    setModalOpen(false);

  }


  const handleGenerate = async(event) => {
    console.log(file)
    console.log(lookBack)
    console.log(futurePrediction)
    setMessage("Modal Training is in Progress, Please Wait");
    const response = await trainForecast(event, file, lookBack, futurePrediction);
    setStatus(true)
    console.log(response)
    setMessage(response);
    setTimeout(() => {
      setStatus(false)
      setMessage("");
      setOpen(false); 
    },5000);

  }

  const handleAnalysisGenerate = async(event) => {
    const response = await analysis(event, files);
    console.log(response);
    setModalOpen(false);
    return response;

  }

  return (
    <>
     <Stack spacing={2} direction="row" style={{position:"sticky", top:"90px"}}>
      <CustomButton onClick={handleClick}>Train (Forecast)</CustomButton>
      <CustomButton onClick={handleClickOpen}>Analysis</CustomButton>
      {open === true &&
     
     <CustomDialog
     open={open}
     onChange={(event)=>{setFile(event.target.files[0])}}
     setOpen={setOpen}
     onClose={handleClose}
     hasTextfield="true"
     heading="Title"
     onClick={handleGenerate}
     message={message}
     status={status}
     
     editableData = {[{
      name: "Look Back",
      onChange : (event)=>{setlookBack(event.target.value)},
      fullwidth: true,
      xs: 12,
      sm: 6,
      required: true,
      
    },
    {
      name: "Future Prediction",
      onChange: (event)=>{setFuturePrediction(event.target.value)},
      fullwidth: true,
      xs: 12,
      sm: 6,
      required:true
      
    }
  ]
}
     />
    }


    {modalOpen === true &&
     <CustomDialog
     open={modalOpen}
     onChange={(event) => {setFiles(event.target.files[0])}}
     setOpen={setModalOpen}
     onClose={handleCloseModal}
     hasTextfield="false"
     heading="Title"
     onClick={handleAnalysisGenerate}
     />
    }
    </Stack>
    </>
  );
}
