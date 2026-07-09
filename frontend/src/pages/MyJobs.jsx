import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import api from "../services/api";

function MyJobs() {

    const [jobs, setJobs] = useState([]);
    const [topApplicants, setTopApplicants] = useState({});

    const loadJobs = async () => {

        try {

            const res = await api.get("/jobs/my-jobs");

            setJobs(res.data);

        }

        catch (error) {

            console.log(error);

            alert("Failed to load jobs");

        }

    };

    const deleteJob = async (id) => {

        if (!window.confirm("Delete this job?"))
            return;

        try {

            await api.delete(`/jobs/delete/${id}`);

            alert("Job deleted");

            loadJobs();

        }

        catch (error) {

            console.log(error);

            alert("Delete failed");

        }

    };

    const loadTopApplicants = async(jobId) => {

        try{

            const res = await api.get(`/jobs/${jobId}/top_candidates`);

            setTopApplicants(prev => ({
                ...prev,
                [jobId]: res.data
            }));

        }

        catch(error){

            console.log(error);

            alert("Unable to load applicants");

        }

    }

    useEffect(() => {

        loadJobs();

    }, []);

    return (

        <>

            <Navbar />

            <div className="page">

                <h1 className="title">

                    My Jobs

                </h1>

                {

                    jobs.map(job => (

                        <div
                            className="card"
                            key={job.id}
                        >

                            <h2>{job.title}</h2>

                            <p>{job.description}</p>

                            <p>

                                Experience : {job.experience_level}

                            </p>

                            <button
                                className="button"
                                onClick={() => deleteJob(job.id)}
                            >
                                Delete Job
                            </button>

                            <button
                                className="button"
                                onClick={() => loadTopApplicants(job.id)}
                            >
                                View Top Applicants
                            </button>

                        </div>

                    ))

                }

            </div>

        </>

    );

}

export default MyJobs;