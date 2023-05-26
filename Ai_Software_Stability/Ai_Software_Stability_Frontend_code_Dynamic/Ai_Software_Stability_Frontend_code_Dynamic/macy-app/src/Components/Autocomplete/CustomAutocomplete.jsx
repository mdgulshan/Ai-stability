import { useContext, useState } from 'react';
import { MenuItem, Select, IconButton, FormControl } from '@mui/material';
import ClearIcon from '@mui/icons-material/Clear';
import { GraphContext } from '../../Contexts/GraphContext';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';


export default function CustomAutocomplete(props) {

    const dropdowns = [
        ["MLO-050  MLO - Portland", "MLO-869 MLO - Tulsa", "MLO-506 MLO - Goodyear","MLO-043 MLO - West Virginia","MLO-500 MLO - Cheshire"],
        ["WMS MA", "Ship On Time (SOT)"]
    ];

    const {selectedValues,setSelectedValues} = useContext(GraphContext);
   


    const handleDropdownChange = (event, index) => {
        const selectedValue = event.target.value;
        setSelectedValues(
            selectedValues.map((_value, i) => (i === index ? selectedValue : false))
        );
    };

    const handleClearClick = (event, index) => {
        event.stopPropagation();
        setSelectedValues(selectedValues.map((value, i) => (i === index ? null : value)));
    };

    return (
        <>
            {dropdowns.map((dropdown, index) => {
                return (
                    <Box sx={{ minWidth: 120 }}>
                        <FormControl fullWidth>
                            <InputLabel>Select</InputLabel>
                                <Select
                                    key={index}
                                    value={selectedValues[index]}
                                    onChange={(event) => handleDropdownChange(event, index)}
                                    label="Select"
                                    sx={{ width: '150px',height:'40px'}}
                                >
                                      
                                {dropdown.map((option, optionIndex) => (
                                    <MenuItem key={optionIndex} value={option} disabled={selectedValues.some((value, i) => value && i !== index)}>
                                        {option}
                                    </MenuItem>
                                ))}

                                    <IconButton
                                        aria-label="clear"
                                        onClick={(event) => handleClearClick(event, index)}
                                        size="large"
                                        disabled={!selectedValues[index]}
                                    >
                                        <ClearIcon />
                                    </IconButton>
                                </Select>
                        </FormControl>
                    </Box>
                ); 
        })}

        </>
    );
}