// this page is all about displaying jobs

import { useState,useEffect } from "react"
import api from "../services/api"
import JobCard from "../components/JobCard"
import Navbar from "../components/Navbar"

function Jobs(){

    const [jobs,setJobs]=useState([])

    useEffect(()=>{

        fetchJobs()

    },[])

    const fetchJobs=async()=>{

        try{

            const response=await api.get(
                "/jobs/getall"
            )

            setJobs(response.data)

        }

        catch(error){

            console.log(error)

            alert("Failed To Load Jobs")
        }
    }

    return(

        <>

            <Navbar />

            <div className="page">

                <h1 className="title">
                    Available Jobs
                </h1>

                {
                    jobs.length===0 ? (

                        <div className="card">

                            <p>
                                No Jobs Available
                            </p>

                        </div>

                    ) : (

                        jobs.map((job)=>(

                            <JobCard
                                // key is not passed to JobCard rather used by React to uniquely identify each job
                                key={job.id}
                                job={job}
                            />

                        ))

                    )
                }

            </div>

        </>

    )
}

export default Jobs