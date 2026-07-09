import { useEffect, useState } from "react"
import api from "../services/api"

function TaskList({ applicationId }) {

    const [tasks, setTasks] = useState([])

    useEffect(() => {

        fetchTasks()

    }, [])

    const fetchTasks = async () => {

        try {

            const response =
                await api.get(
                    `/tasks/${applicationId}`
                )

            setTasks(response.data)

        }

        catch (error) {

            console.log(error)
        }
    }

    const toggleTask = async (task) => {

        try {

            await api.put(

                `/tasks/${task.id}`,

                {
                    completed: !task.completed
                }
            )
            // toggle task status -> updated status in the database -> fetch the tasks with new states
            fetchTasks()

        }

        catch (error) {

            console.log(error)
        }
    }

    const completedCount =
        tasks.filter(
            task => task.completed
        ).length

    return (

        <div>

            <h4>
                Progress : {completedCount}/{tasks.length}
            </h4>

            {
                tasks.map((task) => (

                    <div
                        key={task.id}
                        style={{
                            marginBottom: "10px"
                        }}
                    >

                        <input
                            type="checkbox"
                            checked={task.completed}
                            onChange={() =>
                                toggleTask(task)
                            }
                        />

                        <span
                            style={{
                                marginLeft: "10px"
                            }}
                        >
                            {task.task}
                        </span>

                    </div>

                ))
            }

        </div>
    )
}

export default TaskList