import { useState } from "react";
import { useHistory } from "react-router-dom";
import useFetchPost from "./useFetchPost";

const api = process.env.REACT_APP_API_URL;

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { postData, resData, error, isPending } = useFetchPost();


    const history = useHistory();
    

    const handleLogin = (e) => {
        e.preventDefault();
        const credential = { username, password };
        postData(
            `${api}/auth/login`, credential
        ).then((res) => {
            if (res && res.code === 0) {
                console.log(res);
                localStorage.setItem('token', res.data.access_token);
                history.push("/");
            } else {
                console.log(error);
            }
        })
    }

    return (
        <div className="login-wrapper">
            <div className="login nes-container with-title">
                <h2 className="title">Welcome Administrator!</h2>
                <form onSubmit={handleLogin}>
                    <div className="nes-field login-input-field">
                        <label htmlFor="username">Username:</label>
                        <input type="text" id="username" className="nes-input" onChange={(e) => setUsername(e.target.value)}/>
                    </div>
                    <div className="nes-field login-input-field">
                        <label htmlFor="password">Password:</label>
                        <input type="text" id="password" className="nes-input" onChange={(e) => setPassword(e.target.value)}/>
                    </div>
                    {error && <div><p className="nes-balloon from-left nes-pointer nes-text is-error">{error}</p></div>}
                    {!isPending && <button className="nes-btn is-primary">Login</button>}
                    {isPending && <button className="nes-btn is-primary" disabled >Loading</button>}
                </form>
            </div>
        </div>
    );
}

export default Login;