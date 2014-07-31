#create a list to store addresses based on cardinal directions

nwList = []
neList = []
seList = []
swList = []

#Use raw_input() to allow a user to type an address

def addressGame ():
    address = raw_input('Enter a familiar address here: ')
    print address

    #If that address contains a quadrant (NW, NE, SE, SW), then add it to that quadrant's list.

    if 'NW' in address:
        nwList.append(address)
        print nwList

    if 'NE' in address:
        neList.append(address)
        print neList

    if 'SE' in address:
        seList.append(address)
        print seList

    if 'SW' in address:
        swList.append(address)
        print swList

#Allow user to enter 3 addresses; after three, print the length and contents of each list.

def runApp ():
    for i in range(3):
        print "here we are " + str(i)
        addressGame ()

    print nwList
    print neList
    print seList
    print swList

runApp()

#finished!!!




