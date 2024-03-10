import React from 'react';
import './QuestionCard.css';

export const QuestionCard = ({ question, inputValues, setInputValues }) => {
    const handleAddInput = () => {
        if (inputValues.length < 3) {
            setInputValues([...inputValues, '']); // Add another empty input to the array
        }
    };

    const handleInputChange = (index, event) => {
        const newInputs = [...inputValues];
        newInputs[index] = event.target.value;
        setInputValues(newInputs);
    };

    const handleRemoveInput = (index) => {
        const newInputs = [...inputValues];
        newInputs.splice(index, 1);
        setInputValues(newInputs);
    };

    return (
        <div className="question-card">
            <p>{question}</p>
            {inputValues.map((input, index) => (
                <div key={index} className="input-group" style={{ display: 'flex', padding: "5px", alignItems: 'center' }}>
                    <input
                        type="text"
                        value={input}
                        onChange={(event) => handleInputChange(index, event)}
                        className="question-input"
                    />
                    {inputValues.length > 1 && (
                        <button onClick={() => handleRemoveInput(index)} className="remove-btn">X</button>
                    )}
                </div>
            ))}
            <button onClick={handleAddInput} disabled={inputValues.length >= 3} className={inputValues.length >= 3 ? "disabled-btn" : "available-btn"}>Add Extra Field</button>
        </div>
    );
};
