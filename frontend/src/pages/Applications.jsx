import { useEffect,useState } from "react"
import api from "../services/api"
import ApplicationCard from "../components/ApplicationCard"

function Applications(){

    const [applications,setApplications]=useState([])

    useEffect(()=>{

        fetchApplications()

    },[])

    const fetchApplications=async()=>{

        try{

            const response=await api.get(
                "/applications/my-applications"
            )

            setApplications(response.data)

        }

        catch(error){

            console.log(error)

            alert("Failed to load applications")
        }
    }

    const withdrawApplication = async (applicationId) => {

        const confirmWithdraw = window.confirm(
            "Are you sure you want to withdraw this application?"
        )

        if (!confirmWithdraw)
            return

        try {

            await api.delete(
                `/applications/delete/${applicationId}`
            )

            alert("Application Withdrawn Successfully")

            fetchApplications()

        }

        catch (error) {

            console.log(error)

            alert("Failed To Withdraw Application")
        }

    }

    return(

        <div className="page">

            <h1 className="title">
                My Applications
            </h1>

            {
                applications.length===0 ? (

                    <div className="card">

                        <p>
                            No Applications Found
                        </p>

                    </div>

                ) : (

                    applications.map((application)=>(

                        <ApplicationCard
                            key={application.id}
                            application={application}
                            onWithdraw={withdrawApplication}
                        />
                        

                    ))

                )
            }

        </div>

    )
}

export default Applications