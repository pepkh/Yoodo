import './App.css';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import { Home } from './pages/Home';
import { Recommendation } from './pages/Recommend'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/letsyoga" element={<Recommendation/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
