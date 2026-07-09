import { useState, useEffect } from "react"
import Navbar from "../components/Navbar"
import api from "../services/api"

function Resumes() {

    // for uploading file
    // also on display these 3 things are there -> path , resume, resumeid
    const [file, setFile] = useState(null)
    const [resumes, setResumes] = useState([])
    const [resumeId, setResumeId] = useState("")

    useEffect(() => {

        fetchResumes()

    }, [])

    const fetchResumes = async () => {

        try {

            const response = await api.get(
                "/resumes/getall"
            )

            setResumes(response.data)

        }

        catch (error) {

            console.log(error)

            alert("Failed To Load Resumes")
        }
    }

    const searchResume = async () => {

        if (!resumeId) {

            fetchResumes()

            return
        }

        try {

            const response = await api.get(
                `/resumes/get/${resumeId}`
            )

            setResumes([response.data])

        }

        catch (error) {

            console.log(error)

            alert("Resume Not Found")
        }
    }

    const uploadResume = async () => {

        try {

            if (!file) {

                alert("Please Select A Resume")

                return
            }

            const formData = new FormData()

            formData.append("file", file)

            await api.post(
                "/resumes/upload",
                formData
            )

            alert("Resume Uploaded Successfully")

            // so that another file can be uploaded
            setFile(null)

            fetchResumes()

        }

        catch (error) {

            console.log(error)

            alert("Resume Upload Failed")
        }
    }

    const deleteResume = async (resumeId) => {

            const confirmDelete = window.confirm(
                "Are you sure you want to delete this resume?"
            )

            if (!confirmDelete)
                return

            try {

                await api.delete(
                    `/resumes/delete/${resumeId}`
                )


                fetchResumes()

            }

            catch (error) {

                console.log(error)

                alert("Failed To Delete Resume")
            }

        }

    return (

        <>

            <Navbar />

            <div className="page">

                <h1 className="title">
                    Resumes
                </h1>

                {/* Upload Resume */}

                <div className="card">

                    <h2>
                        Upload Resume
                    </h2>

                    <input
                        className="input"
                        type="file"
                        onChange={(e) => setFile(e.target.files[0])}
                    />

                    <button
                        className="button"
                        onClick={uploadResume}
                    >
                        Upload Resume
                    </button>

                </div>

                {/* Search Resume */}

                <div className="card">

                    <h2>
                        Search Resume By ID
                    </h2>

                    <input
                        className="input"
                        type="number"
                        placeholder="Enter Resume ID"
                        value={resumeId}
                        onChange={(e) => setResumeId(e.target.value)}
                    />

                    <button
                        className="button"
                        onClick={searchResume}
                    >
                        Search
                    </button>

                    <button
                        className="button"
                        onClick={fetchResumes}
                        style={{
                            marginLeft: "10px"
                        }}
                    >
                        Show All
                    </button>

                </div>

                {/* Resume List */}

                <div className="card">

                    <h2>
                        My Resumes
                    </h2>

                    {
                        resumes.length === 0 ?

                            (
                                <p>
                                    No Resumes Found
                                </p>
                            )

                            :

                            resumes.map((resume) => {

                                const filename =
                                    resume.file_path.split("/").pop()

                                return (

                                    <div
                                        key={resume.id}
                                        style={{
                                            padding: "10px",
                                            borderBottom: "1px solid #ddd"
                                        }}
                                    >

                                        <p>
                                            <strong>Resume ID:</strong> {resume.id}
                                        </p>

                                        <p>
                                            <strong>File:</strong> {filename}
                                        </p>

                                        <a
                                            href={`http://127.0.0.1:8000/${resume.file_path}`}
                                            target="_blank"
                                            rel="noreferrer"
                                        >
                                            View PDF
                                        </a>
                                        <br />

                                        <button
                                            className="button"
                                            onClick={() => deleteResume(resume.id)}
                                            style={{
                                                marginTop: "10px"
                                            }}
                                        >
                                            Delete Resume
                                        </button>

                                    </div>

                                )

                            })
                    }

                </div>

            </div>

        </>

    )
}

export default Resumes