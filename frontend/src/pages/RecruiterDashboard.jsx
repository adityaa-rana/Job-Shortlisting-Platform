import { useNavigate } from "react-router-dom"
import Navbar from "../components/Navbar"

function RecruiterDashboard() {

    const navigate = useNavigate()

    return (

        <>

            <Navbar />

            <div className="page">

                <h1 className="title">
                    Recruiter Dashboard
                </h1>

                <div className="dashboard">

                    <div
                        className="dashboard-card"
                        onClick={()=>navigate("/create-job")}
                    >
                        <h2>Create Job</h2>

                        <p>
                            Create a new job and upload JD
                        </p>
                    </div>
                    <div
                        className="dashboard-card"
                        onClick={() => navigate("/my-jobs")}
                    >
                        <h2>My Jobs</h2>

                        <p>
                            View, manage and delete your jobs
                        </p>
                    </div>
                    <div
                        className="dashboard-card"
                        onClick={()=>navigate("/applicants")}
                    >
                        <h2>Applicants</h2>

                        <p>
                            Review and manage candidates
                        </p>
                    </div>

                </div>

            </div>

        </>

    )
}

export default RecruiterDashboard