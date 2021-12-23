import sys
import math
import random

def load_students(path_to_file: str) -> dict:
    """
    Helper function to load in students from file

    Each line in the file should contain a student's name followed 
    by their list of preferences as in the sample data files.
    This function reads in the students and their preferences and 
    creates a dictionary mapping the student to their preferences.

    Parameters
    ----------
    path_to_file: str
        Path to the file containing the students and their preferences

    Returns
    -------
    dict 
        Students mapped to their preferences
    """
    try:
        # Open the file
        with open(path_to_file) as file:
            # Read all the lines in 
            lines = file.readlines()
    except:
        # Print an error message if there is an issue opening the file
        print("Please enter a valid path to a file containing the students", file=sys.stderr)
    # Create dictionary to store mapping of students to their preferences
    students = {}
    # Process each line in the file
    for line in lines:
        # Find beginning ot student's name based on first '
        name_start = line.find("'") + 1
        # Find end ot student's name based on second '
        name_end = line.find("'", name_start)
        # Extract student's name from the line
        name = line[name_start:name_end]
        # Extract students preferences from the line as an array
        preferences = line[name_end + 2:].strip().split(" ")
        # Store mapping of student to their preferences
        students[name] = preferences
    return students


def initalize_projects(students: dict) -> dict:
    """
    Helper function to initialize dictionary of projects based on students preferences

    Parameters
    ----------
    students: dict
        Dictionary of students mapped to their preferences

    Returns
    -------
    dict 
        Projects dictionary where each project is mapped to empty list which will be filled with students assigned to the project
    """
    # Declare dictionary to store project mapped to students assigned to it
    projects = {}
    # Initialize each project in projects to an empty list
    for project in students[list(students.keys())[0]]:
        projects[project] = []
    return projects


def initial_assignment(students: dict, projects: dict) -> dict:
    """
    Helper function to assign students to their first preference

    Parameters
    ----------
    students: dict
        Dictionary of students mapped to their preferences
    projects: dict
        Dictionary of projects mapped to the students assigned to the project

    Returns
    -------
    dict 
        Projects dictionary where each student has been assigned to their first preference
    """
    # Assign each student to their first preference
    for student in students:
        first_preference = students[student][0]
        projects[first_preference].append(student)
    return projects


def assign_students_projects(students: dict, projects: dict, sorted_projects: list, start: int, 
                                end: int, students_project: int, sum_preferences: int) -> tuple:
    """
    Helper function to assign students to projects 

    Parameters
    ----------
    students: dict
        Dictionary of students mapped to their preferences
    projects: dict
        Dictionary of projects mapped to the students assigned to the project
    sorted_projects: list
        List of projects descendingly sorted by the number of students assigned to them
    start: int
        First project to check if has too many students assigned to it
    end: int
        Last project to check if has too many students assigned to it
    students_project: int
        Number of students allowed per project
    sum_preferences: int
        Sum of students preferences; lower value means more students got higher preferences (1st, 2nd 3rd)

    Returns
    -------
    tuple 
        First entry is projects dictionary where each project between start and end has been assigned at most students_project students
        Second entry is sum_preferences; lower value means more students got higher preferences (1st, 2nd 3rd) 
    """
    # For each project in the range provided
    for i in range(start, end):
        # Students second preference
        num_preference = 1
        # While the current project has more students assigned to it than it should
        while len(projects[sorted_projects[i]]) > students_project:
            # Iterate through the students assigned to the project
            for student in projects[sorted_projects[i]]:
                # Get the students next preference
                next_preference = students[student][num_preference]
                # If the students next preference has an opening
                if len(projects[next_preference]) < students_project:
                    # Add current preference to sum preferences, reflecting student is getting a lower preference
                    sum_preferences += num_preference 
                    # Add student to their most prefered project that is available
                    projects[next_preference].append(student)
                    # Remove student from current project
                    projects[sorted_projects[i]].remove(student)
            num_preference += 1
    return (projects, sum_preferences)


def assign_students(students: dict, projects: dict) -> tuple:
    """
    function to assign students to projects based on their preferences

    Parameters
    ----------
    students: dict
        Dictionary of students mapped to their preferences
    projects: dict
        Dictionary of projects mapped to the students assigned to the project

    Returns
    -------
    tuple 
        First entry is projects dictionary where each project has been assigned 3 or 4 students
        Second entry is sum_preferences; lower value means more students got higher preferences (1st, 2nd 3rd) 
    """
    # If there are less than 6 students or not enough projects, return None
    if len(students) < 6 or len(projects) != math.ceil(len(students) / 4):
        return None
    # Calculate number of projects that will be assigned 3 students
    num_projects_of_three = (4 - len(students) % 4) % 4
    # Call helper function to assign student to their first preference
    projects = initial_assignment(students, projects)
    # Create sum of preferences variable to track performance of algorithm
    # A lower value means more students got their higher prefered projects 
    # Initially, each student gets first preference, so sum of preferences is the number of students
    sum_preferences = len(students)
    # Sort projects by the number of students assigned to them in descending order
    sorted_projects = sorted(projects, key=lambda k: len(projects[k]), reverse=True)
    # Call helper function to assign students to projects, allowing at most 4 students per projects in range
    projects, sum_preferences = assign_students_projects(students, projects, sorted_projects, 0, 
                                    len(projects) - num_projects_of_three - 1, 4, sum_preferences)
    # Sort projects by the number of students assigned to them in descending order
    sorted_projects = sorted(projects, key=lambda k: len(projects[k]), reverse=True)
    # Create variable to track number of projects with 3 students assigned to them
    current_num_projects_of_three = 0
    # Calculate number of projects with 3 students assigned to them
    for project in sorted_projects:
        if len(projects[project]) == 3:
            current_num_projects_of_three += 1
    # If there aren't enough projects with 3 students, call function to assign students until each project has 3 or 4 students
    if current_num_projects_of_three != num_projects_of_three:
        projects, sum_preferences = assign_students_projects(students, projects, sorted_projects, 
                                        len(projects) - num_projects_of_three, len(projects), 3, sum_preferences)
    return (projects, sum_preferences)


def random_initial_assignment(students: dict, projects: dict) -> tuple:
    """
    Helper function to assign students to a random project

    Parameters
    ----------
    students: dict
        Dictionary of students mapped to their preferences
    projects: dict
        Dictionary of projects mapped to the students assigned to the project

    Returns
    -------
    tuple 
        First entry is projects dictionary where each student has been assigned to a project
        Second entry is sum_preferences; lower value means more students got higher preferences (1st, 2nd 3rd)
    """
    # Create sum of preferences variable to track performance of algorithm
    # A lower value means more students got their higher prefered projects
    sum_preferences = 0
    # Assign each student to a random project
    for student in students:
        # Selected a random project from students preferences
        random_preference = random.randint(0, len(students[student]) - 1)
        # Get random project based on random_preference
        random_project = students[student][random_preference]
        # Add random_preference + 1 to sum_preferences since a
        # random_preference of 0 corresponds to a student's first preference
        sum_preferences += random_preference + 1
        # Assign student to random project
        projects[random_project].append(student)
    return (projects, sum_preferences)


def randomly_assign_students_projects(students: dict, projects: dict, sorted_projects: list, start: int, 
                                end: int, students_project: int, sum_preferences: int) -> tuple:
    """
    Helper function to randomly assign students to projects 

    Parameters
    ----------
    students: dict
        Dictionary of students mapped to their preferences
    projects: dict
        Dictionary of projects mapped to the students assigned to the project
    sorted_projects: list
        List of projects descendingly sorted by the number of students assigned to them
    start: int
        First project to check if has too many students assigned to it
    end: int
        Last project to check if has too many students assigned to it
    students_project: int
        Number of students allowed per project
    sum_preferences: int
        Sum of students preferences; lower value means more students got higher preferences (1st, 2nd 3rd)

    Returns
    -------
    tuple 
        First entry is projects dictionary where each project between start and end has been assigned at most students_project students
        Second entry is sum_preferences; lower value means more students got higher preferences (1st, 2nd 3rd) 
    """
    # For each project in the range provided
    for i in range(start, end):
        # While the current project has more students assigned to it than it should
        while len(projects[sorted_projects[i]]) > students_project:
            # Iterate through the students assigned to the project
            for student in projects[sorted_projects[i]]:
                # Get a random preference from the student's list of preferences
                random_preference = random.randint(0, len(students[student]) - 1)
                # Get random project based on random_preference
                random_project = students[student][random_preference]
                # If the students random preference has an opening
                if len(projects[random_project]) < students_project:
                    # Get student's preference for current project
                    current_preference = students[student].index(sorted_projects[i]) + 1
                    # Add difference between current and random preference to sum
                    # Student could be more or less happy with new project since it's random
                    sum_preferences += random_preference + 1 - current_preference 
                    # Add student to random project that has openning
                    projects[random_project].append(student)
                    # Remove student from current project
                    projects[sorted_projects[i]].remove(student)
    return (projects, sum_preferences)


def randomly_assign_students(students: dict, projects: dict) -> tuple:
    """
    Function to randomly assign students to projects

    Parameters
    ----------
    students: dict
        Dictionary of students mapped to their preferences
    projects: dict
        Dictionary of projects mapped to the students assigned to the project

    Returns
    -------
    tuple 
        First entry is projects dictionary where each project has been assigned 3 or 4 students
        Second entry is sum_preferences; lower value means more students got higher preferences (1st, 2nd 3rd) 
    """
    # If there are less than 6 students or not enough projects, return None
    if len(students) < 6 or len(projects) != math.ceil(len(students) / 4):
        return None
    # Calculate number of projects that will be assigned 3 students
    num_projects_of_three = (4 - len(students) % 4) % 4
    # Call helper function to assign student to random project
    projects, sum_preferences = random_initial_assignment(students, projects) 
    # Sort projects by the number of students assigned to them in descending order
    sorted_projects = sorted(projects, key=lambda k: len(projects[k]), reverse=True)
    # Call helper function to randomly assign students to projects, allowing at most 4 students per projects in range
    projects, sum_preferences = randomly_assign_students_projects(students, projects, sorted_projects, 0, 
                                    len(projects) - num_projects_of_three - 1, 4, sum_preferences)
    # Sort projects by the number of students assigned to them in descending order
    sorted_projects = sorted(projects, key=lambda k: len(projects[k]), reverse=True)
    # Create variable to track number of projects with 3 students assigned to them
    current_num_projects_of_three = 0
    # Calculate number of projects with 3 students assigned to them
    for project in projects:
        if len(projects[project]) == 3:
            current_num_projects_of_three += 1
    # If there aren't enough projects with 3 students, call function to randomly assign students until each project has 3 or 4 students
    if current_num_projects_of_three != num_projects_of_three:
        projects, sum_preferences = randomly_assign_students_projects(students, projects, sorted_projects, 
                                        len(projects) - num_projects_of_three, len(projects), 3, sum_preferences)
    return (projects, sum_preferences)


def write_project_assignments(projects: dict, filename: str) -> None:
    """
    Write projects with students assigned to them to the filename provided

    Each project and the students assigned to them are written to the 
    filename provided on their own line. 

    Parameters
    ----------
    projects: dict
        Dictionary containing projects mapped to the students assigned to them
    filename: str
        Name of the file that will contain the projects and assigned students

    Returns
    -------
    None
    """
    # Get list of students
    project_list = list(projects)
    # Open file in write mode
    with open(filename, 'w') as output:
        # Write all students other than the last one to the file on a new line
        for index in range(len(project_list) - 1):
            print(project_list[index], ",".join(projects[project_list[index]]), file=output)
        # Write last student to file without end character to prevent blank last line
        print(project_list[-1], ",".join(projects[project_list[-1]]), file=output, end='')
            

if __name__ == "__main__":
    try:
        # Read in first command line argument which is path to file
        path_to_file = sys.argv[1]
    except:
        # Print error message if no command line argument supplied
        print("Please provide file name containing students", file=sys.stderr)
    # Call helper function to create dictionary of students mapped to their preferences
    students = load_students(path_to_file)
    # Call helper function to initialize projects dictionary
    projects = initalize_projects(students)
    # Call function to assign students to projects based on their preferences
    projects, sum_preferences = assign_students(students, projects)
    # Display results
    print("How Many Students:", len(students), "Proposed Algorithm Sum of preferences:", sum_preferences)
     # Save results of student assignment to a file
    write_project_assignments(projects, str(len(projects)) + "project_assignments.txt")
    # Reload students and projects to randomly assign students to projects
    # Call helper function to create dictionary of students mapped to their preferences
    students = load_students(path_to_file)
    # Call helper function to initialize projects dictionary
    projects = initalize_projects(students)
    # Call function to randomly assigned students to projects
    projects, sum_preferences = randomly_assign_students(students, projects)
    # Display results
    print("How Many Students:", len(students), "Random Algorithm Sum of preferences:", sum_preferences)
    # Show path to results file
    print("Project assignments written to", str(len(projects)) + "project_assignments.txt")