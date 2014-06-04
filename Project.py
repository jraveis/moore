import queue
import time
import Task as task

class Project:
	
	def __init__(self,name,due = ''):
		self.name = name
		self.due = due
		self.tasks = queue.PriorityQueue()
		
	def __str__(self):
		return ("Project name: " + self.name +", Project Due Date: " + self.due)
		
	def nextTask(self):
		print (tasks[1].text)
		
	def addTask(self):
	##Create new task
	##add it to the DAG
		description = input("Please describe the text in one line.")
		
		loop = True
		while loop:
			try:
				dueDate = time.strptime(input("When is this task due? Enter in d/m/Y format"),"%d/%m/%Y")
				loop = False
			except ValueError:
				print("That isn't a valid date. Example of a valid date: June 12, 1994 is 12/6/1994.")
		
		hoursEstimate = int(input("How many hours will this project take you?"))
		
		hoursAtATime = int(input("How much time do you want to work at once?"))
		
		numberOfTimesPerDay= int(input("How many times do you want to work per day?"))
		
		newTask = task.Task(description, dueDate, hoursEstimate, hoursAtATime, numberOfTimesPerDay, parentTask)
		
		tasks.put(newTask)
		
	#Complete a specific task. Move it to the list of completed tasks.
	#Calculate the accuracy of the prediction.
	def completeTask(self,number = -1):
		if number == -1:
			print("Please choose which task you completed")
			self.showTasks()
			number = input("Enter the number of the task you completed.")
		task = tasks.pop(number)
		print("The task you completed is: " + task.text +". Confirm? y/n")
		if input() == 'n':
			self.addTask(task)
			self.completeTask()
			
	def showTasks(self):
		i = 0
		for task in self.tasks:
			print("Task number: " + i)
			print("Task: " + task.text)
		
	def showCompletedTasks():
		print("Not so many completed tasks") 
		
	methods={
		"_add":addTask, 
		"_complete":completeTask,
		"_next":nextTask
	}
