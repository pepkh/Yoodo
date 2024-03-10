import { useNavigate } from 'react-router-dom'
import {NavBar} from '../components/NavBar'
import { YogaCard } from '../components/YogaCard';

const dummyList = [
    {
        title: "Cat-cow pose (marjaryasana-bitilasana)",
        benefit:"Cat-Cow pose may help relieve menstrual cramps by promoting blood flow to the pelvic region, while its rhythmic flow can have a calming effect on the nervous system, potentially easing emotional distress during menstruation..",
        link: "https://www.youtube.com/embed/kqnua4rHVVA?si=pS8f1bJNQgWJumAP"
    },
    {
        title: "Child's Pose - Balasana",
        benefit:"Child's Pose may alleviate menstrual cramps by stretching the lower back and pelvic area, while its restorative nature and deep breathing can help reduce emotional distress and promote a calming effect. To practice, start in tabletop position, sit back on your heels, extend arms, and focus on slow, deep breaths for relaxation.",
        link: "https://www.youtube.com/embed/srLgwheLnmc?si=-qOVVbcKkloKo7lP"
    },
    {
        title: "Lion's Pose - Simhasana",
        benefit:"Lion's Pose, with its forceful breath and expressive release, may alleviate period pain by reducing tension and offer emotional relief, potentially easing feelings of sadness and annoyance.",
        link: "https://www.youtube.com/embed/lqHn0n_1O7A?si=2e5qvFIL36S5sRKP"
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
            <h1>Here are {size} recommended yoga poses</h1>
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