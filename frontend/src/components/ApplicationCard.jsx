import { useState } from "react"
import TaskList from "./TaskList"
import api from "../services/api"

function ApplicationCard({ application, onWithdraw }) {

    const [showSkills, setShowSkills] = useState(false)
    const [showRoadmap, setShowRoadmap] = useState(false)
    const [showTodo, setShowTodo] = useState(false)

    const [showQuestions, setShowQuestions] = useState(false)
    const [questions, setQuestions] = useState("")

    const loadQuestions = async () => {

        // Hide if already open
        if (showQuestions) {
            setShowQuestions(false)
            return
        }

        // If already fetched once, don't call backend again
        if (questions) {
            setShowQuestions(true)
            return
        }

        try {

            const response = await api.get(
                `/questions/${application.job_id}`
            )

            setQuestions(response.data.questions)
            setShowQuestions(true)

        }

        catch (error) {

            console.log(error)
            alert("Unable to generate interview questions")

        }

    }

    return (

        <div className="card">

            <h3>
                Status : {application.status}
            </h3>

            <p>
                ATS Score : {application.ats_score}
            </p>

            <p>
                Similarity Score : {application.similarity_score}
            </p>

            <p>
                Feedback : {application.recruiter_message || "No feedback yet"}
            </p>

            <div
                style={{
                    display: "flex",
                    gap: "10px",
                    flexWrap: "wrap",
                    marginTop: "15px"
                }}
            >

                <button
                    className="button"
                    onClick={() => setShowSkills(!showSkills)}
                >
                    Missing Skills
                </button>

                <button
                    className="button"
                    onClick={() => setShowRoadmap(!showRoadmap)}
                >
                    Roadmap
                </button>

                <button
                    className="button"
                    onClick={() => setShowTodo(!showTodo)}
                >
                    Todo
                </button>

                <button
                    className="button"
                    onClick={loadQuestions}
                >
                    Practice Interview
                </button>
                <button
                    className="button"
                    onClick={() => onWithdraw(application.id)}
                >
                    Withdraw Application
                </button>

            </div>

            {
                showSkills && (

                    <div style={{ marginTop: "20px" }}>

                        <h4>Missing Skills</h4>

                        <p>
                            {
                                application.missing_skills
                                    ? application.missing_skills
                                    : "Your resume already covers all required skills."
                            }
                        </p>

                    </div>

                )
            }

            {
                // application.learning_roadmap is the argument required for learning road map to be present
                showRoadmap &&
                application.learning_roadmap && (

                    <div style={{ marginTop: "20px" }}>

                        <h4>Learning Roadmap</h4>

                        <pre
                            style={{
                                whiteSpace: "pre-wrap",
                                background: "#f8fafc",
                                padding: "15px",
                                borderRadius: "10px"
                            }}
                        >
                            {application.learning_roadmap}
                        </pre>

                    </div>

                )
            }

            {
                // application_id is the argument required for learning road map to be present
                showTodo &&
                application.id && (

                    <div style={{ marginTop: "20px" }}>

                        <h4>Learning Progress</h4>

                        <TaskList
                            applicationId={application.id}
                        />

                    </div>

                )
            }

            {
                showQuestions && (

                    <div style={{ marginTop: "20px" }}>

                        <h4>Practice Interview</h4>

                        <pre
                            style={{
                                whiteSpace: "pre-wrap",
                                background: "#f8fafc",
                                padding: "15px",
                                borderRadius: "10px"
                            }}
                        >
                            {questions}
                        </pre>

                    </div>

                )
            }

        </div>

    )

}

export default ApplicationCard