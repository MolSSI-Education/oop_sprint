[![Build Status](https://travis-ci.org/MolSSI-SSS/oop_sprint.svg?branch=master)](https://travis-ci.org/MolSSI-SSS/oop_sprint)

# oop_sprint

A simple Object Oriented Programming (OOP) project to test Agile sprinting.

## Description
The project is a simple student class to handle student-related functions.

There are two types of students: graduate and undergrads.

## How to run

Clone the project
```
git clone https://github.com/MolSSI-SSS/oop_sprint.git
```

Create a conda environment and install the project for development (-e) including tests requirements ([tests])
```
conda create -n oop_sprint_env python=3.5 pip
source activate oop_sprint_env
cd oop_sprint
pip install -e .[tests]
```

Run tests
```
pytest
```

## Agile and Sprinting Overview Presentation

The link to the PPT presentation from the agile sprinting day is [here](https://docs.google.com/presentation/d/1N58JygLF4w6-5s6FrZCpAUSAq2zy2KIoFfLWfXeLEVU/edit?usp=sharing).
