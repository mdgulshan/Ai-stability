import { Stack } from "@mui/material";
import React, { useContext, useState } from "react";
import CustomNavbar from '../../Components/CustomNavbar/CustomNavbar';
import CustomNavigation from "../../Components/Navigation/CustomNavigation";
import DatePicker from "../../Components/DatePicker/DatePicker";
import CustomGraph from "../../Components/CustomGraph/CustomGraph";
import CustomDialog from "../../Components/Dialog/CustomDialog";
import trainForecast from "../../Middlewares/GraphMiddleware";
import dayjs from "dayjs";
import { forecastData } from "../../Middlewares/GraphMiddleware";
import { GraphContext } from "../../Contexts/GraphContext";
import CustomAutocomplete from "../../Components/Autocomplete/CustomAutocomplete";
import CustomButton from "../../Components/Button/CustomButton";
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { CardActionArea } from '@mui/material';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { analysis } from "../../Middlewares/GraphMiddleware";
import styles from '../Wrapper/Wrapper.module.css';
import CustomChart from "../../Components/CustomChart/CustomChart";
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';

export default function Wrapper() {
    const [modalOpen, setModalOpen] = useState(false);
    const [secondModalOpen, setSecondModalOpen] = useState(false);
    const [files, setFiles] = useState(null);
    const buttonText = ['Train (Forecast)','Analysis'];
    const [file,setFile] = useState(null);
    const [lookBack, setlookBack] = useState(null);
    const [futurePrediction, setFuturePrediction] = useState(null);
    const [message, setMessage] = useState(null);
    const [status, setStatus] = useState(false);
    const [datePickerValue, setDataPickerValue] = useState({StartDate : dayjs(), EndDate : dayjs()});
    const labelText = ['StartDate', 'EndDate'];
    const [predictionData, setPredictionData] = useState([]);
    const [graphOpen,  setGraphOpen] = useState(false);
    const [selectedSiteName, setSelectedSiteName] = useState('')
    const dropdowns = [
        ["MLO-050 MLO - Portland", "MLO-869 MLO - Tulsa", "MLO-506 MLO - Goodyear","MLO-043 MLO - West Virginia","MLO-500 MLO - Cheshire","None"],
        ["WMS MA", "Ship On Time (SOT)"]
    ];
   const {selectedValues, setSelectedValues, loading, setLoading} = useContext(GraphContext);
   const siteName = [
    "MLO-050 MLO - Portland", "MLO-869 MLO - Tulsa", "MLO-506 MLO - Goodyear","MLO-043 MLO - West Virginia","MLO-500 MLO - Cheshire",'None'
   
];
    const handleGenerate = async(event) => {
        setMessage("Modal Training is in Progress, Please Wait");
        const response1 = await trainForecast(event,file,siteName);
        console.log(response1)
        setStatus(true)
        setMessage(response1.result1);
        
        const response2 = await trainForecast(event,file,siteName);
        console.log(response2)
        //setStatus(true)
        setMessage(response1.result2);
        setStatus(true)
        //setMessage(response);
        setTimeout(() => {
          setStatus(false)
          setMessage("");
          setModalOpen(false); 
        },5000);
    
      }

    const onForecast = async(event) => {
        event.preventDefault();
        setLoading(true);
        let dropdownValue;
        
        if (selectedValues[0] === false) {
            dropdownValue = selectedValues[1];
        } else {
            dropdownValue = selectedValues[0];
        }
        
        const response = await forecastData(event, datePickerValue.StartDate, datePickerValue.EndDate, dropdownValue);
        setLoading(false);
        setGraphOpen(true);
        setPredictionData(response);
        return response;
    }

    const handleAnalysisGenerate = async(event) => {
        const response = await analysis(event, files);
        console.log(response);
        setSecondModalOpen(false);
        return response;
    
    }
    

    return (
    <div className="container-fluid">
        <div className="row">
            <Stack spacing={20}>
                <Stack spacing={3} direction="row" className={styles.buttonDiv}>
                
                <CustomNavigation
                buttonText={buttonText}
                onChange={[()=>{setModalOpen(true)},()=>{setSecondModalOpen(true)}]}
                />

                </Stack>
                <Stack spacing={4} direction='column'>
                <Card sx={{ maxWidth: 1500}} style={{backgroundColor:'whitesmoke', opacity:0.8}} elevation={0}>
                        <CardContent>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <Stack spacing={3} direction="row">
                                
                                    <DatePicker
                                    labelText={labelText}
                                    datePickerValue={datePickerValue}
                                    setDataPickerValue={setDataPickerValue}
                                    />
                                                    
                                <CustomAutocomplete/>
                                <CustomButton onClick={(event)=>{onForecast(event)}}>Forecast</CustomButton>  
                            </Stack>
                        </LocalizationProvider>
                        </CardContent>
                </Card>

                {graphOpen === true &&
                <CustomGraph predictionData={predictionData}/>
                }
               
                </Stack>

                {modalOpen === true &&
                  <Stack spacing={3} direction="row">
                    <CustomDialog
                    open={modalOpen}
                    onChange={(event)=>{setFile(event.target.files[0])}}
                    setOpen={setModalOpen}
                    onClose={()=>setModalOpen(false)}
                    hasTextfield="true"
                    heading="Train Forecasting"
                    onClick={handleGenerate}
                    message={message}
                    status={status}
                    options={siteName}
                    handleChange={(event, newValue) => {
                        //setSelectedOption(newValue);
                        setSelectedSiteName(newValue);
                      }}
                    selectedvalue={selectedSiteName}
                    editableData = {[]
                    }
                    />
                   
                  </Stack>  
                
                }
                {secondModalOpen === true &&
                  <CustomDialog
                  open={secondModalOpen}
                  onChange={(event) => {setFiles(event.target.files[0])}}
                  setOpen={setSecondModalOpen}
                  onClose={()=>setSecondModalOpen(false)}
                  hasTextfield="false"
                  heading="Analysis"
                  onClick={handleAnalysisGenerate}
                  />
                
                }
            </Stack>
        </div>
    </div>

    );
}