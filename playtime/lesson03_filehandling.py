
#states_file = open("lesson02_states.txt", "r")
#states = states_file.read()
#states_file.close()
#print states

#states_file = file("lesson02_states.txt", "r")

#define enumerate: to mention a number of things one by one. itemlize.

#splitting file into a list at each line
#one list of strings
with open("lesson02_states.txt", "r") as states_file:
    states = states_file.read().split("\n")

#individually splitting each line into a list by the commas
#one list of lists

#for each #, STATE pair that you have when you call enumerate on the set of strings (states)...
enumStates = enumerate(states)
for index in enumStates:
    print enumStates[index]
    #for index, state in enumerate(states):
        #states[index] = state.split(",")

#print states

