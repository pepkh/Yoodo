import { useNavigate } from 'react-router-dom'
import {NavBar} from '../components/NavBar'

import { YogaCard } from '../components/YogaCard';

const dummyList = [
    {
        title: "Bird of Paradise",
        benefit:"Increases the flexibility of the spine and back and stretches the shoulders. Strengthens the legs. Increases flexibility of the hip and knee joints. Improves balance. Opens the groin. Stretches the hamstrings.",
        link: "https://www.youtube.com/watch?v=wIJzVgTTVew&ab_channel=AloMoves-OnlineYoga%26FitnessVideos"
    },
    {
        title: "Big Toe",
        benefit:"Lengthens and strengthens the back of the legs.",
        link: "https://www.youtube.com/watch?v=kcRs6Bm4kFo&ab_channel=YogaWithTim"
}
]

export const Recommendation = () => {
    const navigate = useNavigate();

    const handleBack = ()=> {
        navigate("/")
      }

    const size = dummyList.length;

    return(
        <div style={{display: "flex",
        flexDirection: "column"}}>
            <NavBar/>
            <div style={listStyle}>
            <h1>Here are {size} recommended yoga posts</h1>
            {Object.entries(dummyList).map(([key, value]) => (
                <YogaCard key={key} title={value.title} benefit={value.benefit} link={value.link} />
            ))}
                        <button style={buttonStyle} onClick={handleBack}> Back to Home</button>
            </div>
        </div>
    )
    
}

const listStyle = {
    display: "flex",
    flexDirection: "column",
    // justifyContent: "center",
    alignItems: "center",
    height: "70vh", // Full viewport height to center content vertically
    width: "100vw", // Full viewport width to center content horizontally
    margin: "0", 
    padding: "0", // Ensure no padding is interfering with the centering
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
}