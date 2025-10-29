import { jwtDecode } from "jwt-decode";
import { useHistory, Redirect } from "react-router-dom";
import { Route } from "react-router-dom/cjs/react-router-dom.min";

const ProtectedRoute = ({ children, ...rest }) => {
    const token = localStorage.getItem("token");
    let isOk = false;

    try {
        const decoded = jwtDecode(token);
        isOk = token && decoded.exp * 1000 > Date.now();
    } catch {
        isOk = false;
    }

    return (
    <Route 
        {...rest}
        render = {() => {return isOk === true? children : <Redirect to="login" />}}
    ></Route>);
}

export default ProtectedRoute; 