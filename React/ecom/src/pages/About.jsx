import React from "react";
import './About.css'
import Image from '../img/bak.jpg'
import styled from 'styled-components';

const Maindiv = styled.div`
    background-color: white;
`;





function About(){
    return(
     
        
        <Maindiv>
            <img className='imagetest' src='../img/bak.jpg' />
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Labore laborum voluptate esse voluptatum velit nostrum cupiditate! Laboriosam dignissimos sequi possimus voluptatum sunt optio animi unde! Enim magni sapiente excepturi nam.
        </Maindiv>
    );
}
export default About