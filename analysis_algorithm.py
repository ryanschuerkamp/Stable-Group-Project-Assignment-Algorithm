import time
import numpy as np
import matplotlib.pyplot as plt
import assign_students


def get_sum_preferences() -> dict:
    """
    Return the sum of preferences for the proposed and random algorithm on all datasets produced

    Parameters
    ----------
    None

    Returns
    -------
    dict 
        Dictionary where key is the number of students in dataset and value is 
        a tuple. The first value in the tuple is the sum of preferences generated
        by the proposed algorithm, and the second value is the sum of preferences
        when students are randomly assigned to projects. 
    """
    # Create dictionary storing mapping of number of students in dataset to sum_preferences
    dataset_sum_preferences = {}
    # For each dataset created
    for num_students in [31, 62, 125, 250, 500, 1000]:
        # Track sum of preferences for proposed algorithm and random assignment
        algorithm_sum_preferences = 0
        random_sum_preferences = 0
        # Call helper function to create dictionary of students mapped to their preferences
        students = assign_students.load_students("data/" + str(num_students) + "students.txt")
        # Call helper function to initialize projects dictionary
        projects = assign_students.initalize_projects(students)
        # Call proposed algorithm to assign students based on their preferences
        projects, algorithm_sum_preferences = assign_students.assign_students(students, projects)
        # Reload students and projects so can run random algorithm on dataset
        students = assign_students.load_students("data/" + str(num_students) + "students.txt")
        projects = assign_students.initalize_projects(students)
        # Call function to randomly assign students to projects
        projects, random_sum_preferences = assign_students.randomly_assign_students(students, projects)
        # Store results in dictionary key mapped to a tuple
        dataset_sum_preferences[num_students] = (algorithm_sum_preferences, random_sum_preferences)
    return dataset_sum_preferences


def plot_sum_preferences(dataset_sum_preferences: dict) -> None:
    """
    Helper function to plot sum of preferences as a bar chart

    Parameters
    ----------
    dataset_sum_preferences: dict
        Dictionary where key is the number of students in dataset and value is 
        a tuple. The first value in the tuple is the sum of preferences generated
        by the proposed algorithm, and the second value is the sum of preferences
        when students are randomly assigned to projects. 

    Returns
    -------
    None
    """
    # Set up figure
    fig = plt.figure(dpi=500)
    ax = fig.add_axes([0,0,1,1])
    x = np.arange(3)
    # Get y values from dictionary
    y = list(dataset_sum_preferences.values())
    y1 = [y1[0] for y1 in y]
    y2 = [y2[1] for y2 in y]
    # Plot bars. Only plot first 3 values because later y values for y2 tower over other values
    ax.bar(x + 0.00, y1[0:3], color = 'dodgerblue', width=0.25)
    ax.bar(x + 0.25, y2[0:3], color = 'tab:green', width=0.25)
    # Add Labels
    plt.xlabel('Number of Students in Dataset', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')
    plt.ylabel('Sum of Preferences', fontweight='bold', color = 'black', fontsize='14')
    plt.title('Sum of Preferences Per Dataset', fontweight='bold', color = 'black', fontsize='14')
    plt.xticks(x, list(dataset_sum_preferences.keys())[0:3], fontsize="small")
    # Add legend
    colors = {"Proposed": 'dodgerblue', "Random": 'tab:green'}         
    labels = list(colors.keys())
    plt.legend(labels, title="Algorithm")
    # Save Plot
    fig.savefig('sum_preferences.png', bbox_inches='tight', pad_inches=0.25)
    

def get_average_runtimes() -> dict:
    """
    Helper function to get average run times for algorithm on generated datasets.

    Function runs the algorithm 10 times on each dataset and calculates average for 
    each dataset.

    Parameters
    ----------
    None

    Returns
    -------
    dict 
        Dictionary where key is the number of students in dataset and value is 
        average run time of algorithm on dataset containing the number of students
        speficied by the key
    """
    # Create dictionary to track average time spent running algorithm for each input size
    times = {}
    # For each dataset
    for num_students in [31, 62, 125, 250, 500, 1000]:
        # Create variable to track total time spent running algorithm on each dataset
        sum_times = 0
        # Run algorithm 10 times on each dataset
        for run in range(10):
            # Call helper function to create dictionary of students mapped to their preferences
            students = assign_students.load_students("data/" + str(num_students) + "students.txt")
            # Call helper function to initialize projects dictionary
            projects = assign_students.initalize_projects(students)
            # Get start time
            start = time.time()
            # Call algorithm
            assign_students.assign_students(students, projects)
            # Get end time
            end = time.time()
            # Add difference to sum_times
            sum_times += end - start
        # Add sum_times to dictionary mapping number of students to average time take 
        times[num_students] = sum_times / 10
    return times


def plot_average_runtimes(times: dict) -> None:
    """
    Helper function to plot average runtimes and save as file

    Parameters
    ----------
    times: dict
        Dictionary of number of students in dataset mapped to the average run time 
        of the algorithm on the dataset over 10 runs

    Returns
    -------
    None
    """
    # Set up figure
    x = np.arange(len(times))
    y = times.values()
    fig = plt.figure(dpi=500)
    ax = fig.add_axes([0,0,1,1])
    # Plot bar
    ax.bar(x + 0.00, times.values(), color = 'dodgerblue')
    # Add Labels
    plt.xlabel('Number of Students in Dataset', fontweight='bold', color = 'black', fontsize='14', horizontalalignment='center')
    plt.ylabel('Average Run Time Over 10 Runs (Seconds)', fontweight='bold', color = 'black', fontsize='14')
    plt.title('Average Run Time of Proposed Algorithm', fontweight='bold', color = 'black', fontsize='14')
    plt.xticks(x, times.keys(), fontsize="small")
    # Save Plot
    fig.savefig('runtimes.png', bbox_inches='tight', pad_inches=0.25)


if __name__ == "__main__":
    times = get_average_runtimes()
    plot_average_runtimes(times)
    dataset_sum_preferences = get_sum_preferences()
    plot_sum_preferences(dataset_sum_preferences)
