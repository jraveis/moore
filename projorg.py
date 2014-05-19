#!/usr/bin/python
import sys
import os
import cPickle
import math
import time


projs=cPickle.load(open('/home/james/Projects/Moore/dictionary','r'))
I_mod_it
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
		
	def addTask(task):
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
		
def create(name):
	if name == "":
		print("Name of new Project?")
		name = raw_input()
	try:
		os.mkdir('/home/james/Projects/'+name)
		open('/home/james/Projects/'+name+'/tasks','a').close()
	except:
		print("Project already exists")
		exit()
	print("Does you project have a specific due date? Enter in d/m/y format. Give full month and year. If none, hit enter.")
	due = raw_input()
	if due != '':
		due = datetime.strptime(due,"%d/%B/%Y")
		new = Project(name = name, due = due)
	else:
		new = Project(name = name)
	projs[str(len(projs))] = new

def newProject():
	print("new")

def continueProject():
	print("continue")

val = sys.argv[1]

{"np": newProject, "cont": continueProject}[val]()


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
