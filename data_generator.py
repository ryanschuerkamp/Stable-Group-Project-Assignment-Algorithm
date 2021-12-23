from faker import Faker
import random
import math
import sys

def generate_students(num_students: int, num_projects: int) -> dict:
    """
    Generate num_students students and return resulting students
    
    Each generated student has a unique first and last name combination and 
    their own preferences. The students are stored in a dictionary mapping 
    their name to their preferences. 

    Parameters
    ----------
    num_students: int
        How many students to generate
    num_projects: int
        How many projects there are

    Returns
    -------
    dict
        Students mapped to their preferences
    """
    # Create dictionary to store students mapped to their preferences
    students = {}
    # Create faker object to generate random names
    fake = Faker()
    # Create num_students students
    while len(students) < num_students:
        # Generate random first and last name for a student
        name = "'" + fake.name() + "'"
        # Generate random preferences for student
        preferences = random.sample(range(1, num_projects + 1), num_projects)
        # Convert preferences to space delimited string
        preferences = ' '.join(str(preference) for preference in preferences)
        # Store student mapped to their preferences in the dictionary of students
        students[name] = preferences
    return students


def write_students(students: dict, filename: str) -> None:
    """
    Write students to the filename provided

    Each student and their preferences are written to the filename provided
    and are on their own line. 

    Parameters
    ----------
    students: dict
        Dictionary containing students to write to file
    filename: str
        Name of the file that will contain the students

    Returns
    -------
    None
    """
    # Get list of students
    student_list = list(students)
    # Open file in write mode
    with open(filename, 'w') as output:
        # Write all students other than the last one to the file on a new line
        for index in range(len(student_list) - 1):
            print(student_list[index], students[student_list[index]], file=output)
        # Write last student to file without end character to prevent blank last line
        print(student_list[-1], students[student_list[-1]], file=output, end='')


if __name__ == "__main__":
    try:
        # Allow the user to enter in command line arguments to specify datasets to generate
        # For example, user could enter 80 120 and a file containing 80 and another
        # file containing 120 students would be produced
        class_sizes = sys.argv[1:]
        # Convert each command line argument specificed to int
        class_sizes = [int(size) for size in class_sizes]
        # If no command line arguments provided, generate the dataset used in our report
        if len(class_sizes) == 0:
            class_sizes = [31, 62, 125, 250, 500, 1000]
    except:
        # Assign class sizes to the dataset sizes considered in our report if 
        # error invalid command-line arguments are provided or if none are
        class_sizes = [31, 62, 125, 250, 500, 1000]
    # Create file(s) containing specified number of students
    for num_students in class_sizes:
        # The maximum number of students that can be assigned to a project
        max_students_per_project = 4
        # Calculate number of projects
        num_projects = math.ceil(num_students / max_students_per_project)
        # Call helper function to generate students
        students = generate_students(num_students, num_projects)
        # Call helper function to write students to file
        write_students(students, str(num_students) + "students.txt")
