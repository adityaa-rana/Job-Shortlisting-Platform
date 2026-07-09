import { useState } from "react"
import { Link, useNavigate } from "react-router-dom"
import api from "../services/api"

function Register() {

    const [name,setName]=useState("")
    const [email,setEmail]=useState("")
    const [password,setPassword]=useState("")
    const [role,setRole]=useState("candidate")
    const [showPassword, setShowPassword] = useState(false);

    const navigate=useNavigate()

    const handleRegister=async()=>{

        try{

            await api.post(
                "/users/register",
                {
                    // It is a JavaScript Object
                    name,
                    email,
                    password,
                    role
                }
            )

            // alert("Registration Successful")


            // navigate is  Used when JavaScript decides to change pages.
            navigate("/")

        }

        catch(error){

            console.log(error)

            alert("Registration Failed")
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
                    ATS Registration
                </h1>

                <input
                    className="input"
                    type="text"
                    placeholder="Full Name"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                />

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

                <select
                    className="input"
                    value={role}
                    onChange={(e)=>setRole(e.target.value)}
                >
                    <option value="candidate">
                        Candidate
                    </option>

                    <option value="recruiter">
                        Recruiter
                    </option>
                </select>

                <button
                    className="button"
                    onClick={handleRegister}
                >
                    Register
                </button>

                <p
                    style={{
                        marginTop:"20px"
                    }}
                >
                    Already have an account?{" "}

            
                    <Link to="/">
                        Login
                    </Link>
                </p>

            </div>

        </div>

    )
}

export default Register
