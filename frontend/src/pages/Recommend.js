import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { NavBar } from '../components/NavBar';
import { YogaCard } from '../components/YogaCard';
import axios from 'axios';

export const Recommendation = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const [yogaPoses, setYogaPoses] = useState([]);
    const [isLoading, setIsLoading] = useState(true);  // Add state to track loading status

    const handleBack = () => {
        navigate("/");
    };

    useEffect(() => {
        const postData = {
            user_input_mood: location.state.moods,
            user_input_health: location.state.healthConditions
        };

        axios.post('http://127.0.0.1:5000/generate_text', postData)
            .then(response => {
                setYogaPoses(response.data);
                setIsLoading(false);  // Data fetched, set loading to false
                console.log(response.data)
            })
            .catch(error => {
                console.error('Fetching yoga poses failed:', error);
                setIsLoading(false);  // Ensure loading is set to false even on error
            });
    }, [location.state]);  // Add location.state to the dependency array if its content might change

    return (
        <div style={{ display: "flex", flexDirection: "column" }}>
            <NavBar />
            <div style={listStyle}>
                {isLoading ? (
                    <p>Loading recommended yoga poses...</p>  // Display a loading message or a spinner
                ) : (
                    <>
                        <h1>Here are {yogaPoses.length} recommended yoga poses</h1>
                        {yogaPoses.map((pose, index) => (
                            <YogaCard key={index} title={pose.title} benefit={pose.description} link={pose.video_link} />
                        ))}
                    </>
                )}
                <button style={buttonStyle} onClick={handleBack}> Back to Home</button>
            </div>
        </div>
    );
};

const listStyle = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    height: "70vh",
    width: "100vw",
    margin: "0",
    padding: "0",
    textAlign: "center",
};

const buttonStyle = {
    margin: "10px",
    width: "30%",
    padding: "10px",
    border: "none",
    backgroundColor: "#33CAAF",
    color: "black",
    fontSize: "large",
    fontWeight: "bold",
    borderRadius: "20px",
    boxShadow: "0 2px 4px 0 rgba(0, 0, 0, 0.2)",
};
