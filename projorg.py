#!/usr/bin/python
import sys
import os
import pickle
import math
import time

####################
#Define derectory in which the projects are going to be stored
#Need to set an enviroment variable to the destination folder
path= os.environ.get("PROJECT_HOME","Not set")
if path=="Not set":
	path=os.getcwd()
print(path)

if os.path.exists('dictionary'):
	projs=pickle.load(open( os.getcwd()+ 'dictionary','r'))
else:
	projs={}
#Not needed
#else:
	#create new file
	#os.path.touch('disctionary')

#How accurate the user is. Need to update to actually reflect user's accuracy.
userMult = 1.0

class Task:
	def __init__(text,due,time,priority,interval,number):
		#Description of task
		self.text = text
		#Due date of task
		self.due = due
		#User's estimate of time to complete task
		self.time = time
		#Priority of task. Possibly used to resolve issues in scheduling.
		self.priority = priority
		#Maximum amount of time spent at once on a single task.
		self.interval = interval
		#Number of times to work on a task per day.
		self.numberOfSets = number
		#Program's estimate of how long it will take to complete the task.
		self.PredictedTime = timeToComplete()
		#The program's estimate of the start time.
		self.predictedStartTime = timeToStart()
	
	#Calculates the day on which you should start the task.	
	def timeToStart():
		startdate = due - self.PredictedTime
		return startdate
		
	def timeToComplete():
		#The number of days the user thinks it will take.
		userDays = math.ceil(float(time)/(interval*number))
		
		#The number of days the program thinks it will take.
		progDays = userDays * userMult
		return progDays
		
		
	def start():
		self.started = True
		self.actualStartDate = time.strftime("%d/%m/%Y")
		
	def __str__():
		return ("Text: " + text +", Due Date: " + due + ", Expected Completion Time: " + time + ", Priority: " + priority + ", Time per Day: " + interval + ", Number of Intervals per Day: " + number + "." )

class Project:
	def __init__(name,task,due = ''):
		self.name = name
		self.due = due
		self.tasks.append(task)
		
	def __str__():
		return ("Project name: " + name +", Project Due Date: " + due + ", Tasks: " + tasks)
		
	def nextTask():
		print (tasks[1].text)
		
	def addTask():
	##Create new task
	##add it ot the list
		test=input("Task description: ")
		
		due=input("Enter due date: ")
		
		time=input("How long do you think it will take you finish this task?")
		priority="1"
		
		task= Task(text,due,time,priority,interval,number)
		tasks.append(task)
		tasks.sort(key = lambda k: k[startTime])
		
	def completeTask(number = -1):
		if number == -1:
			print("Please choose which task you completed")
			i = 0
			for task in tasks:
				print("Task number: " + i)
				print("Task: " + task.text)
			number =input("Enter the number of the task you finished.")
		task = tasks.pop(number)
		print("The task you completed is: " + task.text +". Confirm? y/n")
		if input() == 'n':
			addTask(task)
		
def createProject(name):
	#Create new directory for the project
	try:
		os.mkdir(path+name)
		open(path+name+'/tasks','a').close()
	except:
		print("Could not create a directory")
		exit()
	due = input("Does you project have a specific due date? Enter in d/m/y format. Give full month and year. If none, hit enter.")
	if due != '':
		due = datetime.strptime(due,"%d/%B/%Y")
		newP = Project(name = name, due = due)
	else:
		newP = Project(name = name)
	projs[str(len(projs))] = newP
	

###########################################################
#Method to read the input and call a method on the chosen project
#Takes the project instance as input
#######################################################

def parseMethodName(curProject):
	if(sys.argc>1):
		cmd2=sys.argv[2]
	else:
		while True:
			cmd2=input("enter method to be called")
			if methodTable.contains_key(cmd2):
				curProj.methodTable[cmd2]()
				return
			else:
				print("Please enter again")
				
		#cmd2 is a method name
		#call this method on the current project
	
def parseProjectName(cmd):
	while True:
		if cmd in projs:
			curProj = projs[cmd]
			print("project exists!")
			parseMethodName(curProj)
			return
		else:
			name=input("project does not exist. Should I create new? y?")
			if name=="y":
				curProj=createProject(cmd)
				print("Created a new project!")
				parseMethodName(curProj)
				return
			else:
				print(projs.keys())
				cmd=raw_input("type project name")

def getInput():
	name=""
	while name=="":
		name=input("Please enter a name")
	return name				
##############################################################
#The program is called with 0 or more parameters.
#If 0 parmeters have to prompt for imput
#if 1 parameter then assume the name of project was input
#If 2 parameters name of project and the method to be called on that project
##############################################################	
#Main()	
cmd=""
#Define all methods in the dictionary
methods={
	"_add":Project.addTask, 
	"_complete":Project.completeTask,
	"_next":Project.nextTask
	}
	

	
#Main logic, very simple!
if len(sys.argv) <2 :
	name=getInput()
else:
	name=sys.argv[1]
	print("The 1st argument is",sys.argv[1])
parseProjectName(name)
		
		
##############################################################
#End of main()
###################################	##########################	



# if len(sys.argv) != 1:
	# cmd=sys.argv[1]
	# parseInput(cmd)				
# else:
	# print("no arg")
	
# val = sys.argv[1]

############################################################
#############################################################

#{"np": newProject, "cont": continueProject}[val]()


'''
projNumber = int(sys.argv[1])

#Get working project based on user input.
if projNumber in range(0,len(projs)):
	workProj = projs[projNumber]
else:
	#Possibly check if input is a project name?
	print("Not a valid project")
	quit()
	
#Task to do
if sys.argv[2] == "1" or sys.argv[2] == "nextTask":
	workProj.nextTask()
		
if sys.argv[2] == "2" or sys.argv[2] == "addTask":
	workProj.addTask()
		
if sys.argv[2] == "3" or sys.argv[2] == "finishTask":
	workProj.finishTask()
	'''
