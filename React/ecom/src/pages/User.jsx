import React from "react";
import { useParams } from "react-router-dom";
import { createBrowserRouter,RouterProvider } from "react-router-dom";
import { Link } from "react-router-dom";


function User(){
    const params = useParams();
    return(
        <div>
            
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
export default User