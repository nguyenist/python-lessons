days_of_week = ['Monday', 'Tuesday']

days_of_week.append('Wednesday')

print days_of_week

print len(days_of_week)

day = days_of_week.pop(2)

print day

days_of_week.insert(0, 'Sunday')

print days_of_week

address = "1133 19th St NW Washington DC 20036"

address_as_list = address.split(" ")

print address_as_list

#create a list to store addresses based on cardinal directions

nwList = []
neList = []
seList = []
swList = []

def answer ():
    address = raw_input('Enter a familiar address here: ')

    #assign address to cardinal directions list
    if 'NW' in address:
        nwList.append(address)

    if 'NE' in address:
        neList.append(address)

    if 'SE' in address:
        seList.append(address)

    if 'SW' in address:
        swList.append(address)

print nwList = []
print neList = []
print seList = []
print swList = []

answer()













