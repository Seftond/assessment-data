#opening file um-server-01.txt and storing in log_file variable
log_file = open("um-server-01.txt")

#defines a function called sales_report that takes in a file parameter
def sales_reports(log_file):
    #for loop that loops through each line in the file
    for line in log_file:
        #removing whitespace at the end of each line
        line = line.rstrip()
        #creates a new variable day that stores the first 3 letters of the line
        day = line[0:3]
        #checks if day is equal to Tue
        if day == "Mon":
            #prints the line to the console if true
            print(line)

#stores results into sales_reports file
sales_reports(log_file)
