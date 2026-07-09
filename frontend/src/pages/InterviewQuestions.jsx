import { useParams } from "react-router-dom"
import { useEffect,useState } from "react"
import api from "../services/api"

function InterviewQuestions(){

    const { jobId } = useParams()

    const [questions,setQuestions] =
    useState("")

    useEffect(()=>{

        fetchQuestions()

    },[])

    const fetchQuestions=async()=>{

        const response=
        await api.get(
            `/questions/${jobId}`
        )

        setQuestions(
            response.data.questions
        )
    }

    return(

        <div className="page">

            <h1 className="title">
                Practice Interview
            </h1>

            <pre
                style={{
                    whiteSpace:"pre-wrap"
                }}
            >
                {questions}
            </pre>

        </div>
    )
}

export default InterviewQuestions