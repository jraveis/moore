#!/usr/bin/python
import sys
import os
import pickle
import math
import time
import getpass
###################
#Use getpass to find the user, create 
#the subfolder in their home directory.
#For now, run script every time.
#Later, modify file to include value.

if exists('dictionary'):
	projs=pickle.load(open('/home/james/Projects/Moore/dictionary','r'))
else:
	#create new file
	os.touch('disctionary')

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
		tasks.append(task)
		tasks.sort(key = lambda k: k[startTime])
		
	def completeTask(number = -1):
		if number == -1:
			print("Please choose which task you completed")
			i = 0
			for task in tasks:
				print("Task number: " + i)
				print("Task: " + task.text)
			print("Enter the number of the task you finished.")
			number = raw_input()
		task = tasks.pop(number)
		print("The task you completed is: " + task.text +". Confirm? y/n")
		if raw_input() == 'n':
			addTask(task)
		
def createProject(name):
	#Create new directory for the project
	try:
		os.mkdir('/home/james/Projects/'+name)
		open('/home/james/Projects/'+name+'/tasks','a').close()
	except:
		print("Project already exists")#is that the only reason it fail?
		exit()
	print("Does you project have a specific due date? Enter in d/m/y format. Give full month and year. If none, hit enter.")
	due = getInput()
	if due != '':
		due = datetime.strptime(due,"%d/%B/%Y")
		newP = Project(name = name, due = due)
	else:
		new = Project(name = name)
	projs[str(len(projs))] = newP
	

###########################################################
#Method to read the input and call a method on the chosen project
#Takes the project instance as input
#######################################################

def parseMethodName(curProject):
	if(sys.argc>1)
		cmd2=sys.argv[2]
	else:
		while True:
			print("enter method to be called")
			cmd2=raw_input()
			if methodTable.contains_key(cmd2)
				curProj.methodTable[cmd2]()
				return
			else:
				print("Please enter again")
				
		#cmd2 is a method name
		#call this method on the current project
	
def parseProjectName(cmd):
	while True:
		if projs.contains_key(cmd):
			curProj = projs[cmd]
			print("project exists!")
			parseMethodName(curProj)
			return
		else:
			print("project does not exist. Should I create new? y?")
			if (name=raw_input())=="y":
				curProj=createProject(cmd)
				print("Created a new project!")
				parseMethodName(curProj)
				return
			else:
				print(projs.keys())
				print("type project name")
				cmd=raw_input()

def getInput():
	(input=raw_input())!=""
	return input				
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
	"_add":addTask, 
	"_complete":completeTask,
	"_next":nextTask
	}
	

	
#Main logic, very simple!
if sys.argc<1 :
	print("enter project name")
	name=getInput()
else:
	name=sys.argv[1]
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
