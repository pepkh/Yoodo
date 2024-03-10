import './NavBar.css'
import logo from '../images/Yoodo_logo.png'

export const NavBar = () => {
    return (
        <div className="navbar">
            {/* icon and main options */}
            <img src={logo} alt="" width={220} height={150}></img>
        </div>
    );
};
