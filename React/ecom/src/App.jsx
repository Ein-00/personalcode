
import './App.css';
import { createBrowserRouter,RouterProvider } from "react-router-dom";
import Home from './pages/Home'
import About from './pages/About';
import Login from './pages/Login';
import Navbar from './components/Header';
import User from './pages/User';
import Create from './pages/Create';

export default function App(){
  const router = createBrowserRouter([
    {
      path:"/Home",
      element: < ><Navbar /> <Home/></>

    },
    {
      path:"/",
      element:< ><Navbar /> <Login/></>
    },
    {
      path: "/about",
      element : < ><Navbar /> <About/></>
    },
    {
      path:"/create",
      element:<><Navbar /> <Create/></>
    },
    {
      path:"/user/:username",
      element:<><Navbar /><User /></>
    },
])
  return (
  <>
      <div className='Maindiv'></div>
      <RouterProvider router={router}/>
      
    </>
  );
}




