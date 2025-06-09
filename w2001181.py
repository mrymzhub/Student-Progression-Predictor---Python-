# I declare that my work contains no examples of misconduct, such as plagirism, or collusion.
# Student ID: w2001181
# Date: 22-11-2023

#       SOFTWARE DEVELOPMENT - COURSEWORK 2023

# PART 1 - MAIN VERSION
#                    A. OUTCOMES
print("Part 1 - A. Outcomes")  #Just so that the user can know why he is entering the data here

passingScore = int(input("Enter your pass marks: "))
deferredScore = int(input("Enter your defer marks: "))
failingScore = int(input("Enter your fail marks: "))

#  PROGRESS --- outcome 1
if passingScore == 120 and deferredScore == 0 and failingScore == 0:
    outcome = "Progress"

#  TRAILING --- outcome 2
elif passingScore == 100 and (deferredScore == 20 or deferredScore == 0) and (failingScore == 20 or failingScore == 0):
    outcome = "Progress(module trailer)"

#   MODULE RETRIEVER --- outcome 3
elif (passingScore == 80 or passingScore == 60 or passingScore == 40 or passingScore == 20 or passingScore == 0) and (deferredScore == 120 or deferredScore == 100 or deferredScore == 80 or deferredScore == 60 or deferredScore == 40 or deferredScore == 20 or deferredScore == 0) and (failingScore == 60 or failingScore == 40 or failingScore == 20 or failingScore == 0):
    outcome = "Module Retriever"

#   EXCLUDE --- outcome 4
elif (passingScore == 40 or passingScore == 20 or passingScore == 0) and (deferredScore == 40 or deferredScore == 20 or deferredScore == 0) and (failingScore == 120 or failingScore == 100 or failingScore == 80):
    outcome = "Exclude"

else:
    print("Unknown Data Category")
#   RESULT
print("The Progress Outcome is", outcome)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Part 1 - B. Validation")  #Just so that the user can know why he is entering the data here
#                   B. VALIDATION
print("INTEGER REQUIRED")   #Just so that the user can know why he is entering the data here
#   INTEGER REQUIRED
passingScore = input("Enter your pass marks: ")
deferredScore = input("Enter your defer marks: ")
failingScore = input("Enter your fail marks: ")

if passingScore.isdigit() and deferredScore.isdigit() and failingScore.isdigit():
    passingScore = int(passingScore)
    deferredScore = int(deferredScore)
    failingScore = int(failingScore)
    print("The above data types is integers.")
else:
    print("Integer Required")


# --------------------------------------------------------------------------------------------------------------------------------------------------------
print("OUT OF RANGE")   #Just so that the user can know why he is entering the data here
#   OUT OF RANGE
passingScore = int(input("Enter your pass marks: "))
deferredScore = int(input("Enter your defer marks: "))
failingScore = int(input("Enter your fail marks: "))

if passingScore in [0, 20, 40, 60, 80, 100, 120] and deferredScore in [0, 20, 40, 60, 80, 100, 120] and failingScore in [0, 20, 40, 60, 80, 100, 120]:
    print("The integers are in range")
else:
    print("Out of Range")


# --------------------------------------------------------------------------------------------------------------------------------------------------------
print("TOTAL INCORRECT")   #Just so that the user can know why he is entering the data here
#   TOTAL INCORRECT
passingScore = int(input("Enter your pass marks: "))
deferredScore = int(input("Enter your defer marks: "))
failingScore = int(input("Enter your fail marks: "))

add = passingScore + deferredScore + failingScore

if add == 120:
    print("The Total is: ", add)
else:
    print("Total Incorrect")

# if add != 120:
#   print("Total Incorrect")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Part 1 - C. Multiple Outcomes")   #Just so that the user can know why he is entering the data here
#                   C.  MULTIPLE OUTCOMES
#   LOOP UNTIL THE USER ENTERS 'q' TO QUIT
while True:
    passingScore = int(input("Enter your pass marks: "))
    deferredScore = int(input("Enter your defer marks: "))
    failingScore = int(input("Enter your fail marks: "))

    #  PROGRESS --- outcome 1
    if passingScore == 120 and deferredScore == 0 and failingScore == 0:
        outcome = "Progress"

    #  TRAILING --- outcome 2
    elif passingScore == 100 and (deferredScore == 20 or deferredScore == 0) and (failingScore == 20 or failingScore == 0):
        outcome = "Trailing"

    #   MODULE RETRIEVER --- outcome 3
    elif (passingScore == 80 or passingScore == 60 or passingScore == 40 or passingScore == 20 or passingScore == 0) and (deferredScore == 120 or deferredScore == 100 or deferredScore == 80 or deferredScore == 60 or deferredScore == 40 or deferredScore == 20 or deferredScore == 0) and (failingScore == 60 or failingScore == 40 or failingScore == 20 or failingScore == 0):
        outcome = "Module Retriever"

    #   EXCLUDE --- outcome 4
    else:
        outcome = "Exclude"

    #   RESULT
    print("The Progress Outcome is", outcome)

    # PROMPT TO CONTINUE OR QUIT
    choose = input("Enter 'q' to quit or 'y' to continue: ")
    if choose == 'q':
        break
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Part 1 - D. Histogram")   #Just so that the user can know why he is entering the data here
#                   D. HISTOGRAM

# for this part of code I have taken help and ideas from different coding websites like w3school.com and also youtube. Along with that, I read the lecture slides and the tutorial sessions (tutorial week 7). 

from graphics import *   #import the graphics.py module (must be in the same folder as this file)


#OPEN THE WINDOW
win = GraphWin("My First Graphics Window", 800, 600)                     #open a window object called "win" with size and title 
win.setBackground("Mint Cream")                                          # Set the background colour of the window

# INITIALIZATION OF HISTOGRAM DATA
progress_count = 0
trailing_count = 0
retriever_count = 0
exclude_count = 0
 

#   LOOP UNTIL THE USER ENTERS 'q' TO QUIT
while True:
    passingScore = int(input("Enter your pass marks: "))
    deferredScore = int(input("Enter your defer marks: "))
    failingScore = int(input("Enter your fail marks: "))

    #  PROGRESS --- outcome 1
    if passingScore == 120 and deferredScore == 0 and failingScore == 0:
        progress_count += 1
        outcome = "Progress"

    #  TRAILING --- outcome 2
    elif passingScore == 100 and (deferredScore == 20 or deferredScore == 0) and (failingScore == 20 or failingScore == 0):
        trailing_count += 1
        outcome = "Trailing"

    #   MODULE RETRIEVER --- outcome 3
    elif (passingScore == 80 or passingScore == 60 or passingScore == 40 or passingScore == 20 or passingScore == 0) and (deferredScore == 120 or deferredScore == 100 or deferredScore == 80 or deferredScore == 60 or deferredScore == 40 or deferredScore == 20 or deferredScore == 0) and (failingScore == 60 or failingScore == 40 or failingScore == 20 or failingScore == 0):
        retriever_count += 1
        outcome = "Module Retriever"

    #   EXCLUDE --- outcome 4
    elif (passingScore == 40 or passingScore == 20 or passingScore == 0) and (deferredScore == 40 or deferredScore == 20 or deferredScore == 0) and (failingScore == 120 or failingScore == 100 or failingScore == 80):
         exclude_count += 1
         outcome = "Exclude"
    else:
        outcome = "An Error"

    print("The Progress Outcome is ", outcome)

    print("Would you like to enter another set of data?")

    # PROMPT TO CONTINUE OR QUIT
    choose = input("Enter 'q' to quit or 'y' to continue: ")
    if choose == 'q':
        break


# WIDTH OF EACH HISTOGRAM BAR
bar_width = 100

# HEIGHT OF THE BARS
bar_height = 50

# PROGRESS BAR
progress_bar = Rectangle(Point(50, 250), Point(50 + bar_width, 250 - progress_count * bar_height))      #the first point(50, 250) represents the top-left corner of the rectangle. The rec starts at position (50, 250)
progress_bar.setFill("deeppink1")      # the second point(50 + bar---) represents the bottom-right corner of the rectangle. the rec will wnd at a pixel position that is calculated by adding bar width to 50 (starting position). y position is calc by subtracting the progress count multiplied by bar height from 250
progress_bar.draw(win)

# TRAILING BAR
trailing_bar = Rectangle(Point(150, 250), Point(150 + bar_width, 250 - trailing_count * bar_height))
trailing_bar.setFill("goldenrod1")
trailing_bar.draw(win)

# RETRIEVER BAR
retriever_bar = Rectangle(Point(250, 250), Point(250 + bar_width, 250 - retriever_count * bar_height))
retriever_bar.setFill("magenta3")
retriever_bar.draw(win)

# EXCLUDE BAR
exclude_bar = Rectangle(Point(350, 250), Point(350 + bar_width, 250 - exclude_count * bar_height))
exclude_bar.setFill("palevioletred2")
exclude_bar.draw(win)

# Display the number of students and the total count
progress_label = Text(Point(50 + bar_width // 2, 260), f"Progress")
trailing_label = Text(Point(150 + bar_width // 2, 260), f"Trailer")
retriever_label = Text(Point(250 + bar_width // 2, 260), f"Retriever")
exclude_label = Text(Point(350 + bar_width // 2, 260), f"Exclude")

text_list = [progress_label, trailing_label, retriever_label, exclude_label]


for text in text_list:
    text.setSize(12)
    text.draw(win)


# Calculate the total count
total_count = progress_count + trailing_count + retriever_count + exclude_count
strngCount = str(total_count)

# Create a Text object to display the outcome
outcome_text = Text(Point(290, 290), f"The total outcomes displayed are {strngCount}")
outcome_text.setSize(12)
outcome_text.draw(win)


# Wait for the user to close the window
win.getMouse()
win.close()



print("End Of Part 1")


# -----------------------------------------------------------------------------------------
#   PART 2
#   LIST (EXTENSION)
print("PART 2 - LIST")  #Just so that the user can know why he is entering the data here

# for this part of code a group discussion was done

def empList(pass_list, defer_list, fail_list):
    #progression.append(total_count)

    pass_list.append(passingScore)
    defer_list.append(deferredScore)
    fail_list.append(failingScore)

    return pass_list,defer_list,fail_list

new_passScore, new_deferScore, new_failScore = empList([], [], [])
print(new_passScore)
print(new_deferScore)
print(new_failScore)

print("End of Part 2")   #Just so that the user can know why he is entering the data here
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#   PART 3
#   TEXT FILE (EXTENSION)

print("PART 3 - TEXT FILE") #Just so that the user can know why he is entering the data here

# Open the file in write mode
f = open('W2001181\part3file.txt', 'w')

# Write the progression data to the file
f.write('Progress: \n')
f.write('Module Trailing: \n')
f.write('Module Retriever: \n')
f.write('Exclude: ')


# Close the file
f.close()

print("Open the w2001181.txt file to see the results")  #Just so that the user can know why he is entering the data here
print("End of Part 3")  #Just so that the user can know why he is entering the data here
print("THE END OF COURSEWORK")  #Just so that the user can know why he is entering the data here









