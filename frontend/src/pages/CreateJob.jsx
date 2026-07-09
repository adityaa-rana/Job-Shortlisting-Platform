import { useState } from "react"
import api from "../services/api"
import Navbar from "../components/Navbar"

function CreateJob() {

    const [title,setTitle] = useState("")
    const [description,setDescription] = useState("")
    const [experienceLevel,setExperienceLevel] = useState("")
    const [file,setFile] = useState(null)

    const createJob = async() => {

        try{

            const formData = new FormData()

            formData.append("title",title)
            formData.append("description",description)
            formData.append("experience_level",experienceLevel)
            formData.append("jd_file",file)

            await api.post(
                "/jobs/create",
                formData
            )

            alert("Job Created Successfully")

            // set it back for another job
            setTitle("")
            setDescription("")
            setExperienceLevel("")
            setFile(null)

        }

        catch(error){

            console.log(error)

            alert("Failed To Create Job")
        }
    }

    return (

        <>

            <Navbar />

            <div className="page">

                <h1 className="title">
                    Create Job
                </h1>

                <div className="card">

                    <input
                        className="input"
                        placeholder="Job Title"
                        value={title}
                        onChange={(e)=>setTitle(e.target.value)}
                    />

                    <input
                        className="input"
                        placeholder="Job Description"
                        value={description}
                        onChange={(e)=>setDescription(e.target.value)}
                    />

                    <input
                        className="input"
                        placeholder="Experience Level"
                        value={experienceLevel}
                        onChange={(e)=>setExperienceLevel(e.target.value)}
                    />

                    <input
                        className="input"
                        type="file"
                        onChange={(e)=>setFile(e.target.files[0])}
                    />

                    <button
                        className="button"
                        onClick={createJob}
                    >
                        Create Job
                    </button>

                </div>

            </div>

        </>

    )
}

export default CreateJob