# Stable Group Project Assignment Algorithm

An algorithm to assign students to projects based on their preferences.

A description of the problem and algorithm, pseudocode, example cases, time complexity analysis, evaluation, and discussion of the algorithm are in Report.pdf. The code in this repository generates test data, implements the algorithm, and evaluates and compares the algorithm to an algorithm that randomly assigns students to projects.

This code and the report are part of a group project for CSE 374 Algorithms taught at Miami University. I wrote all of the code and the report by myself other than section 2.3, and I wrote the pseudocode but didn't type it in LaTex. My teammates wrote section 2.3, typed the pseudocode in LaTex, proofread the report, and created slides and a video presentation.

## Project Organization
The data folder contains sample datasets of the same size used in Report.pdf. The results folder contains sample results based on the datasets in the data folder.

data_generator.py generates datasets with students and their preferences like the data in the data folder.

assign_students.py assigns students to projects based on their preferences using the algorithm and a random algorithm and prints the sum of preferences for both algorithms. It also saves the project assignments by the algorithm to a file named numberOfProjectsproject_assignments.txt (i.e. 32project_assignments.txt).

analysis_algorithm.py creates a figure (runtimes.png) of the average run time of the algorithm over 10 runs for different numbers of students to display how the run time grows as the input size grows. It also creates a figure (sum_preferences.png) to compare the sum of preferences between the proposed and random algorithms.

## How to Run

### Set Up
To clone the repository run the following command:
```bash
git clone https://github.com/ryanschuerkamp/Stable-Group-Project-Assignment-Algorithm.git
```

To switch into the repository run:
```bash
cd Stable-Group-Project-Assignment-Algorithm/
```
To run the code and install dependencies, you need python and pip installed. 

### Generate Data
To install Faker dependency which is required to generate data run:
```bash
pip install Faker
```
To generate data sets containing the same number of students as in our report and the data folder run:
```bash
python data_generator.py
```
To generate new data sets specify the number of students you want for each dataset separated by spaces:
```bash
python data_generator.py 47 432 1467
```
The above command will produce three data sets called 47students.txt, 432students.txt, and 1467students.txt.

### Assign Students to Projects
To run the algorithm to assign students to projects run:
```bash
python assign_students.py 125students.txt
```
The above command will assign the 125 students in the file to projects and save the results of the project assignments to a file called 32project_assignments.txt.

Any file containing students can replace 125students.txt. The number of projects determines the name of the results file as displayed above by 32project_assignments.txt (125 students assigned to 32 projects).

### Run Analysis
To install NumPy, required for the analysis script, run:
```bash
pip install numpy
```
To install Matplotlib, also mandatory, run:
```bash
pip install matplotlib
```
To generate the figures runtimes.png and sum_preferences.png run:
```bash
python analysis_algorithm.py
```
