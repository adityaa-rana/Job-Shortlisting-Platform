import { useNavigate } from "react-router-dom"
import Navbar from "../components/Navbar"

function CandidateDashboard() {

    const navigate = useNavigate()

    return (

        <>

            <Navbar />

            <div className="page">

                <h1 className="title">
                    Candidate Dashboard
                </h1>

                <div className="dashboard">

                    <div
                        className="dashboard-card"
                        onClick={()=>navigate("/jobs")}
                    >
                        <h2>Jobs</h2>
                        <p>
                            Browse available jobs
                        </p>
                    </div>

                    <div
                        className="dashboard-card"
                        onClick={()=>navigate("/resumes")}
                    >
                        <h2>Resumes</h2>
                        <p>
                            Upload and manage resumes
                        </p>
                    </div>

                    <div
                        className="dashboard-card"
                        onClick={()=>navigate("/applications")}
                    >
                        <h2>Applications</h2>
                        <p>
                            Track application status
                        </p>
                    </div>

                </div>

            </div>

        </>

    )
}

export default CandidateDashboard