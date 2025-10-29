import { Link } from 'react-router-dom';
import { useHistory, useLocation } from 'react-router-dom';

const Navbar = () => {
    const token = localStorage.getItem("token");
    const history = useHistory();
    const localtion = useLocation();

    const handleLogout = () => {
        localStorage.removeItem("token");
        if (localtion.pathname === "/") {
            history.go(0);
        } else {
            history.push("/");
        }
    }

    return (
        <nav className="navbar">
            <div className="navbar-core">
                <h1 className="nes-text">Pdr's Blog</h1>
                <div className="links">
                    <Link to="/" className="">Home</Link>
                    {token && <Link to="/create" className="">Create</Link>}
                    {token && (<button type="button" onClick={handleLogout}>Logout</button>)}
                </div>
            </div>
        </nav>
    );
}
 
export default Navbar;