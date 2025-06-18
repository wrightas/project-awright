# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#Weekly Reporter Function
def weeklyHabitsTasksReporter(habitsDict,tasksDict,inputFile):
    #Habit Reporter
    n=0
    print(f"{inputFile}: Habit Report\n")
    habitsL = list(habitsDict.keys())
    if len(habitsL) == 0:
        print("No habits in database!")
    else:
        for h in habitsL:
            for day in days:
                if not habitsDict[h][day] == False:
                    n += 1
            print(f"Habit {h} completed {n} times out of seven")
            n=0
    #Task Reporter
    print(f"Task Report\n")
    tasksL = list(tasksDict.values()) #check for existence of tasks
    if tasksL == [{}, {}, {}, {}, {}, {}, {}]:
        print("No tasks to report!")
    else:
        print(f"Completed Tasks\t\t\t\t Uncompleted Tasks")
        for x in days:
            if not tasksDict[x] == {}:
                for key in tasksDict[x].keys():
                    if tasksDict[x][key] == True:
                        print(f"{key} completed ({x})")
                    else:
                        print(f"\t\t\t\t\t{key} not completed ({x})")

# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.


# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = []
for x in range(10):
    file_list.append(f"dictionaries_{x+1}.txt")

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        weeklyHabitsTasksReporter(data[0], data[1], file_name)