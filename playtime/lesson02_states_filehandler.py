
#Goal 1: Change your Lesson 2 playtime states.py to use file handling to create your lists.

#Open states.txt or states.csv

#How do get the abbreviations into one list and the state names into another?


#create empty lists for the states to go into
states = []

#create empty lists for the abbreves to go into
abbreves = []

#take txt file and read it. python will be able to read it as states_file (file handler)
with open("lesson02_states.txt", "r") as states_file:
    #in the states_file, go through it and split it at each new line and store it as a list of strings
    lines = states_file.read().split("\n")
    #check to see that each line is split up
    print lines

#for each string in the list of strings, excluding first and last string
for index in range(1, len(lines)-1):
    #store the current line of lines list as "currentString"
    currentString = lines[index]
    #manupulate that one line to pull out the abbreves
    abbreves.append(currentString[14:16])
    #manipulate that one line to pull out the state name
    states.append(currentString[17:-9])

#print everything
#print abbreves
#print states

#with open ("lesson02_states_2col", "w") as new_file:
    #new_file.write(some_string)


hugeStr = "<table> <tr> <th>Abbreviation</th> <th>State Name</th> </tr>"
#for every abbreviation and state name
for index in range(0,len(abbreves)):
    #add abbreve + state name in that row. keep adding new rows while keeping the old ones.
    #states[index] means get the element at index's value so that could be 0,1,2,3...
    hugeStr = hugeStr + "<tr> <td>" + abbreves[index] + "</td>" + "<td>" + states[index] + "</td> </tr>"
#after you're done, close the table
hugeStr = hugeStr + "</table>"

print hugeStr

#i want to open a new file named this. and call it new_file so that i can write the string "hugeStr" into it.
with open ("lesson02_states_2col.html", "w") as new_file:
    new_file.write(hugeStr)

















