import React from "react";
import { useState } from "react";
function Create(){
    const [selectedop,setSelectedop]= useState('')
    const handleoption = (event)=>{
        setSelectedop(event.target.value)
    }

    return(
        <div>
               <h1 className='Header'>Create Account</h1>
      <input type="text" className='inputid' placeholder='ID' />
      <input type="password" className='inputpass' placeholder='Password' />
      <input type="text" className="inputname" placeholder="Name"/>
      <label>
        <input
             type="radio"
            value="farmer"
            checked = {selectedop === 'farmer'}
            onChange={handleoption}
        />
        Farmer
      </label>
      <label>
        <input
            type="radio"
            value="buisness"
            checked = {selectedop === 'buisness'}
            onChange={handleoption}
        />Buisness
      </label>
      <button className='loginb'>Submit</button> 
        </div>

    );
}
export default Create