# Student Progression Outcome Program

## Overview

This Python program is designed to assess and classify student progression outcomes based on their credits in pass, defer, and fail modules. The project is divided into multiple parts for educational purposes and includes validation, outcome generation, data visualization, and file handling features.

**Author**: Student ID: w2001181  
**Date**: 22-11-2023  
**Coursework**: Software Development - Coursework 2023

---

## Features

### Part 1 – Main Program

- **A. Outcomes**  
  Determines student progression based on inputs:
  - Progress
  - Progress (module trailer)
  - Module retriever
  - Exclude

- **B. Validation**
  - Ensures user inputs are integers
  - Validates credit values (must be in steps of 20, up to 120)
  - Ensures total credits sum to exactly 120

- **C. Multiple Outcomes**
  - Allows input of multiple student records
  - User can continue entering data until choosing to quit

- **D. Histogram Visualization**
  - Displays a graphical histogram of outcomes using the `graphics.py` module
  - Bar chart includes Progress, Trailer, Retriever, and Exclude categories

### Part 2 – List Extension

- Stores progression credit data into separate lists using a function `empList`
- Demonstrates use of list data structures for further processing

### Part 3 – Text File Output

- Outputs static headers into a file `part3file.txt` to simulate result export
- Demonstrates basic file handling in Python

---

## Requirements

- Python 3.x
- `graphics.py` file (must be in the same directory as this script)

---

## How to Run

1. Ensure Python and the `graphics.py` module are installed.
2. Place the `w2001181.py` file and `graphics.py` in the same folder.
3. Run the script:
   ```bash
   python w2001181.py
