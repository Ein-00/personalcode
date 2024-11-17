import React from "react";
import { useState } from "react";
function Home(){
  const [selectedop,setselectedop] = useState('')
  const handlechange = (event)=>{
    setselectedop(event.target.value)
  }
  return(
      <div>
        <h1>Product details</h1>
        /*insert the table here */
        <h2>Select an option:</h2>
      <select value={selectedop} onChange={handlechange}>
        <option value="">Select...</option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
        {/* Add more options as needed */}
      </select>


      </div>
  );
}


export default Home