import { BrowserRouter,Routes,Route } from "react-router-dom"

import Login from "./pages/Login"
import Register from "./pages/Register"
import CandidateDashboard from "./pages/CandidateDashboard"
import RecruiterDashboard from "./pages/RecruiterDashboard"
import Jobs from "./pages/Jobs"
import Resumes from "./pages/Resumes"
import Applications from "./pages/Applications"
import CreateJob from "./pages/CreateJob"
import Applicants from "./pages/Applicants"
import ProtectedRoute from "./routes/ProtectedRoute"
import InterviewQuestions from "./pages/InterviewQuestions"
import MyJobs from "./pages/MyJobs";
function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Login />}
                />

                <Route
                    path="/register"
                    element={<Register />}
                />
                <Route
                    path="/my-jobs"
                    element={<ProtectedRoute><MyJobs /></ProtectedRoute>}
                />
                <Route
                    path="/candidate"
                    element={
                        <ProtectedRoute>
                            <CandidateDashboard />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/recruiter"
                    element={
                        <ProtectedRoute>
                            <RecruiterDashboard />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/jobs"
                    element={
                        <ProtectedRoute>
                            <Jobs />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/resumes"
                    element={
                        <ProtectedRoute>
                            <Resumes />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/applications"
                    element={
                        <ProtectedRoute>
                            <Applications />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/create-job"
                    element={
                        <ProtectedRoute>
                            <CreateJob />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="/applicants"
                    element={
                        <ProtectedRoute>
                            <Applicants />
                        </ProtectedRoute>
                    }
                />

                <Route
                    path="*"
                    element={<h1>Page Not Found</h1>}
                />

                <Route
                    path="/questions/:jobId"
                    element={
                        <ProtectedRoute>
                            <InterviewQuestions/>
                        </ProtectedRoute>
                    }
                />

            </Routes>

        </BrowserRouter>

    )
}

export default App