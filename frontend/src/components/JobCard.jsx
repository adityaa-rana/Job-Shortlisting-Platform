import api from "../services/api"

// object destructuring
function JobCard({ job }) {

    const applyJob = async () => {

        try {

            const resumeId = prompt("Enter Resume Id")

            if (!resumeId) {
                return
            }

            await api.post(
                "/applications/apply",
                {
                    job_id: job.id,
                    resume_id: Number(resumeId)
                }
            )

            alert("Applied Successfully")

        }

        catch (error) {

            console.log(error)

            alert("Application Failed")
        }
    }

    return (

        <div className="card">

            <h2>{job.title}</h2>

            <p>{job.description}</p>

            <p>
                <strong>Experience:</strong> {job.experience_level}
            </p>

            <button
                className="button"
                onClick={applyJob}
            >
                Apply Now
            </button>

        </div>

    )
}

export default JobCard