import { useState } from "react"
import api from "../services/api"

function Applicants() {

    // for searching with jobid
    const [jobId,setJobId]=useState("")
    const [applications,setApplications]=useState([])
    const [feedback,setFeedback]=useState("")

    const fetchApplicants=async()=>{

        try{
            // this api endpoint is from jobs module
            const response=await api.get(
                `/jobs/${jobId}/applications`
            )

            setApplications(response.data)

        }

        catch(error){

            console.log(error)

            alert("Failed to load applicants")
        }
    }

    const updateStatus=async(applicationId,status)=>{

        try{
            // this api endpoint is from applications module
            await api.put(
                `/applications/${applicationId}`,
                {
                    status,
                    recruiter_message:feedback
                }
            )

            alert("Updated Successfully")

            fetchApplicants()

        }

        catch(error){

            console.log(error)

            alert("Update Failed")
        }
    }


    const viewResume = async (applicationId) => {

        try {

            const response = await api.get(
                `/applications/${applicationId}/resume`
            );

            const url = `http://127.0.0.1:8000/${response.data.file_path}`;

            console.log(url);

            window.open(url, "_blank");

        }

        catch (error) {

            console.log(error);

            alert("Unable to open resume");
        }

    }
    return(

        <div className="page">

            <h1 className="title">
                Applicants
            </h1>

            <input
                className="input"
                placeholder="Enter Job Id"
                value={jobId}
                onChange={(e)=>setJobId(e.target.value)}
            />

            <button
                className="button"
                onClick={fetchApplicants}
            >
                Load Applicants
            </button>

            <br /><br />

            {
                applications.map((app)=>(

                    <div
                        key={app.id}
                        className="card"
                    >

                        <h3>
                            Candidate Id : {app.candidate_id}
                        </h3>

                        <p>
                            ATS Score : {app.ats_score}
                        </p>

                        <p>
                            Similarity Score : {app.similarity_score}
                        </p>

                        <p>
                            Status : {app.status}
                        </p>

                        <button
                            className="button"
                            onClick={() => viewResume(app.id)}
                        >
                            View Resume
                        </button>
                        <textarea
                            className="input"
                            placeholder="Feedback"
                            onChange={(e)=>setFeedback(e.target.value)}
                        />

                        <button
                            className="button success"
                            onClick={()=>
                                updateStatus(
                                    app.id,
                                    "Shortlisted"
                                )
                            }
                        >
                            Shortlist
                        </button>

                        <button
                            className="button danger"
                            onClick={()=>
                                updateStatus(
                                    app.id,
                                    "Rejected"
                                )
                            }
                        >
                            Reject
                        </button>

                    </div>

                ))
            }

        </div>

    )
}

export default Applicants