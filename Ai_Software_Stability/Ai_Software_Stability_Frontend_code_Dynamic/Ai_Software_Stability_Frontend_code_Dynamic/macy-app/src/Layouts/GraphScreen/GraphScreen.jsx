import { Stack } from "@mui/material";
import React, { useContext } from "react";
import CustomNavbar from '../../Components/CustomNavbar/CustomNavbar';
import Wrapper from "../Wrapper/Wrapper";
import { GraphContext } from "../../Contexts/GraphContext";
import Loading from "../../Components/Loading/Loading";



export default function GraphScreen() {
    const {loading} = useContext(GraphContext);
    return (
    <div className="container-fluid">
        <div className="row">
            <CustomNavbar/>
            {loading === true &&
            <Loading/>
            }
            <Wrapper/>
        </div>
    </div>

    );
}