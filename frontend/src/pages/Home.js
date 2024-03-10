import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { NavBar } from '../components/NavBar';
import { QuestionCard } from '../components/QuestionCard';

export const Home = () => {
    const navigate = useNavigate();
    const question1 = "What's your mood today?";
    const question2 = "Are there any specific Health Conditions?";
    const description1 = "Enter one mood...";
    const description2 = "Enter one health condition...";

    // State for input values for each question
    const [inputValues1, setInputValues1] = useState(['']);
    const [inputValues2, setInputValues2] = useState(['']);

    const handleSubmit = () => {
        // Example action: log input values from both questions
        console.log(inputValues1, inputValues2);
        navigate("/letsyoga");
    };

    return (
        <div>        
            <NavBar />
            <div style={listStyle}>
                <QuestionCard question={question1} description={description1} inputValues={inputValues1} setInputValues={setInputValues1}/>
                <QuestionCard question={question2} description={description2} inputValues={inputValues2} setInputValues={setInputValues2}/>
                <button style={buttonStyle} onClick={handleSubmit}>Let's Do Yoga!</button>
            </div>
        </div>
    );
};



const listStyle = {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    height: "80vh", 
    margin: "0", 
    padding: "10px",
    textAlign: "center",
};


const buttonStyle = {
    margin: "10px",
    width: "50%",
    padding: "10px",
    border: "none",
    backgroundColor: "#33CAAF",
    color: "black",
    fontSize: "large",
    fontWeight: "bold",
    borderRadius: "20px",
    boxShadow: "0 2px 4px 0 rgba(0, 0, 0, 0.2)",
}

