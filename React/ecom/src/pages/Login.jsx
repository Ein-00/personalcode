import React from "react";
import { Link } from "react-router-dom";


function Login(){
  <nav>
    <Link to ="/create">create</Link>
    <Link to ="/Home">Home  </Link>
  </nav>
  


    return(
        <div className='Logindetail'>
      <h1 className='Header'>Login</h1>
      <input type="text" className='inputid' placeholder='ID' />
      <input type="password" className='inputpass' placeholder='Password' />
      <Link to = "/Home"><button className='loginb'>Submit</button></Link>
      <Link to ="/create">Don't have an account.</Link>
      
    </div>
    );
}
export default Login