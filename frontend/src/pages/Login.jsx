import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import api from "../services/api"

function Login() {

    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")
    const [showPassword, setShowPassword] = useState(false);

    const navigate=useNavigate()

    const handleLogin=async()=>{

        try{

            // login doesn't mean we redirect to the dashboard, it means token is generated and stored in response
            const response=await api.post(
                "/users/login",
                {
                    email,
                    password
                }
            )

            // store the token in localstorage
            localStorage.setItem(
                "token",
                response.data.access_token
            )
            
            // role based navigation

            // first get the current user by jwt token
            const user=await api.get(
                "/users/getuser"
            )

            if(user.data.role==="candidate"){
                navigate("/candidate")
            }
            else{
                navigate("/recruiter")
            }

        }

        catch(error){

            console.log(error)

            alert("Login Failed")
        }
    }

    return(

        <div className="page">

            <div
                className="card"
                style={{
                    maxWidth:"500px",
                    margin:"50px auto"
                }}
            >

                <h1 className="title">
                    ATS Login
                </h1>

                <input
                    className="input"
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e)=>setEmail(e.target.value)}
                />

                <div className="password-container">
                    <input
                        className="input"
                        type={showPassword ? "text" : "password"}
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />

                    <span
                        className="eye-icon"
                        onClick={() => setShowPassword(!showPassword)}
                    >
                        {showPassword ? "⌣" : "👁"}
                    </span>
                </div>

                <button
                    className="button"
                    onClick={handleLogin}
                >
                    Login
                </button>

                <p
                    style={{
                        marginTop:"20px"
                    }}
                >
                    Don't have an account?{" "}
                    <Link to="/register">
                        Register
                    </Link>
                </p>

            </div>

        </div>

    )
}

export default Login