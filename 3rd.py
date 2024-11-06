# Function to check if the current color assignment is safe for a given vertex
def is_safe(graph, color, vertex, c):


    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:  # Check adjacency
            return False
    return True

# Utility function to solve the graph coloring problem
def graph_coloring_util(graph, m, color, vertex):
    if vertex == len(graph):  # If all vertices are colored, return True
        return True

    # Try assigning each color to this vertex
    rgb = ["Red", "Green", "Blue"]
    for c in rgb:
        if is_safe(graph, color, vertex, c):
            color[vertex] = c  # Assign the color
            if graph_coloring_util(graph, m, color, vertex + 1):  # Recur to assign colors to the next vertex
                return True
            color[vertex] = None  # Backtrack if assigning this color doesn't lead to a solution

    return False

# Main function to solve the graph coloring problem using backtracking
def graph_coloring(graph, m):
    n = len(graph)  # Number of vertices in the graph
    color = [None] * n  # Color array to store colors assigned to vertices

    # Call the utility function to solve the problem
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False

    # Print the solution
    print("Solution exists. Assigned colors are:")# Define a job class to store job information
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


# Function to perform job scheduling using a greedy algorithm
def job_scheduling(jobs, max_deadline):
    # Sort the jobs based on decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Array to store the result of scheduled jobs
    result = [None] * max_deadline  # Time slots array
    total_profit = 0  # To store the total profit

    # Iterate through all given jobs
    for job in jobs:
        # Find a free time slot from the job's deadline, moving backward
        for j in range(min(job.deadline, max_deadline) - 1, -1, -1):
            if result[j] is None:
                result[j] = job.job_id  # Assign the job ID to the slot
                total_profit += job.profit  # Add the job's profit
                break  # Job scheduled, no need to look further

    # Print scheduled jobs
    print("Scheduled jobs:", [job for job in result if job is not None])
    print(f"Total Profit: {total_profit}")


# Driver code
if __name__ == "__main__":
    # Example list of jobs (job_id, deadline, profit)
    jobs = [
        Job('Job1', 2, 100),
        Job('Job2', 1, 19),
        Job('Job3', 2, 27),
        Job('Job4', 1, 25),
        Job('Job5', 3,50)
    ]

    for i in range(n):
        print(f"Vertex {i} ---> Color {color[i]}")

    return True

# Driver code
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]

    m = 3  # Number of colors

    # Solve the graph coloring problem
    graph_coloring(graph, m)
