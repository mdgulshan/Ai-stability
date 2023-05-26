export default async function trainForecast(event, file, siteName) {
    try {
      event.preventDefault();
      const fileData = new FormData();
  
      fileData.append("excel_file", file);
      fileData.append("dataset", siteName);

      
      
      const response = await fetch("http://localhost:8000/Read_csv_site_Name/"
        ,
        {
          method: "POST",
  
          headers: {
            // "Content-Type": "application/json"
            // "Content-Type": 'multipart/form-data'
            
          },
          body: fileData
          // body: JSON.stringify(DATA_FORMAT)
        }
      );
      const json = await response.json();
      if (response.status === 200) {
        // setMessage(json);
        
        return json;
      
      } 
    } catch (error) {
      return error.message;
    }
  }

 export async function analysis(event,files) {
    try {
      event.preventDefault();
      const fileData = new FormData();
      fileData.append(files);
      console.log(fileData)
      console.log(JSON.stringify(fileData))
      const response = await fetch("http://localhost:8000/trigramdf",
        {
          method: "POST",
  
          headers: {
            // "Content-Type": "application/json"
            // "Content-Type": 'multipart/form-data'
           
          },
          body: fileData
          // body: JSON.stringify(DATA_FORMAT)
        }
      );
      const json = await response.json();
      if (response.status === 200) {
        // setTabularData(json);
        console.log(json)
        return json;
       
      } 
    } catch (error) {
      return error.message;
    }
  }

  export async function forecastData(event, startdate, enddate, dataset) {
    console.log(startdate)
    console.log(enddate)
    console.log(dataset)
   
    try {
      event.preventDefault();
      const fileData = new FormData();
      fileData.append("start_date", startdate);
      fileData.append("end_date", enddate);
      fileData.append("dataset", dataset);
      console.log(fileData)
      console.log(JSON.stringify(fileData))
      const response = await fetch("http://localhost:8000/predict_site_Name/",
        {
          method: "POST",
  
          headers: {
            // "Content-Type": "application/json"
            // "Content-Type": 'multipart/form-data'
           
          },
          body: fileData
          // body: JSON.stringify(DATA_FORMAT)
        }
      );
      const json = await response.json();
      if (response.status === 200) {
        // setTabularData(json);
        console.log(json)
        return json;
       
      } 
    } catch (error) {
      return error.message;
    }
  }
