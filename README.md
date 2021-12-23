# Stable Group Project Assignment Algorithm

An algorithm to assign students to projects based on their preferences.

A description of the problem and algorithm, pseudocode, example cases, time complexity analysis, evaluation, and discussion of the algorithm can be found in Report.pdf. The code in this repository implements the algorithm, generates test data, and evaluates and compares the algorithm to an algorithm which randomly assigns students to projects. 

This code and the report were created as part of a group project for CSE 374 Algorithms taught at Miami University. I wrote all of the code and almost all of the report by myself other than sections 2.3, and I wrote the pseudocode but didn't type it in LaTex. My group mates typed the pseudocode in LaTex, proofread the report, and created slides and a video presentation. 

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
In order to run the code and install dependencies, you need python and pip installed. 

### Generate Data
To install Faker dependency which is required to generate data run:
```bash
pip install Faker
```
To generate the data used in our report and contained in the data folder run:
```bash
python data_generator.py
```
To generate new datasets specify the number of students you want for each dataset separated by spaces:
```bash
python data_generator.py 47 432 1467
```
The above command will produce 3 datasets called 47students.txt, 432students.txt, and 1467students.txt.

### Assign Students to Projects
To run the algorithm to assign students to projects run:
```bash
python assign_students.py 125students.txt
```
The above command will assign the 125 students in the file to projects and save the results of the project assignments to a file called 32project_assignments.txt.

125students.txt can be replaced by any file containing students. The resulting file will be named based on the number of projects as displayed above by 32project_assignments.txt.
