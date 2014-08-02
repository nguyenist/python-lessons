#This will print 0-9
#for number in range (10):
#    print number


#Create a list for days of the week
days_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

months_in_year = ['January','February','March','April','May','June','July','August','September','October','November','December']

#Print all of the days of the week once
#for day in days_of_week:
#    print day

#Print days of the week 1-5
#for week in range(1, 5):
#    print "Week {0}".format(week)

#This will print Week #1 - Mon, Tu, We, Th, Fri x 4
#for week in range(1, 5):
#    print "Week {0}".format(week)
#    for day in days_of_week:
#        print day

#Massive list: Month, number of weeks in month, days of week in each week

for month in months_in_year:
    print month

    for week in range(1, 5):
        print "Week {0}".format(week)

        for day in days_of_week:
            print day






