import React, { useState } from 'react';
import './YogaCard.css';

export const YogaCard = ({ title, benefit, link }) => {

    const [showVideo, setShowVideo] = useState(false);


    const handleToggleVideo = () => {
        setShowVideo(!showVideo);
    };

    return (
        <div className="yoga-card">
            <h1>{title}</h1>
            <p>{benefit}</p>
            {showVideo? <button className='video-btn' onClick={handleToggleVideo}>Collapse Video</button>: <button className='video-btn' onClick={handleToggleVideo}>View Video</button>}
            {showVideo && (
                <iframe width="560" height="315" src="https://www.youtube.com/embed/kcRs6Bm4kFo?si=DJY9V1crjT3PpP_U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            )}
        </div>
    );
};
