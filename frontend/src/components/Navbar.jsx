import { useNavigate } from "react-router-dom"

function Navbar() {

    const navigate = useNavigate()

    const logout = () => {

        localStorage.clear()

        navigate("/")
    }

    return (

        <div className="navbar">

            <h2>
                ATS System
            </h2>

            <button
                className="button danger"
                onClick={logout}
            >
                Logout
            </button>

        </div>

    )
}

export default Navbar