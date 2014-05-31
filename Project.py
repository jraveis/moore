class Project:

	
	def __init__(self,name,due = ''):
		self.name = name
		self.due = due
		
	def __str__():
		return ("Project name: " + name +", Project Due Date: " + due + ", Tasks: " + tasks)
		
	def nextTask():
		print (tasks[1].text)
		
	def addTask():
	##Create new task
	##add it to the DAG
		description = input("Please describe the text in one line.")
		
		dueDate = time.strptime(input("When is this task due? Enter in d/m/y format"),"%d/%m/%y")
		
		hoursEstimate = int(input("How many hours will this project take you?"))
		
		hoursAtATime = int(input("How much time do you want to work at once?"))
		
		numberOfTimesPerDay= int(input("How many times do you want to work per day?"))
		
		task = Task(description, dueDate, hoursEstimate, hoursAtATime, numberOfTimesPerDay, parentTask)
		
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
			
	def showTasks():
		print("A Whole lot of tasks")
		
	def showCompletedTasks():
		print("Not so many completed tasks") 
		
	methods={
		"_add":addTask, 
		"_complete":completeTask,
		"_next":nextTask
	}
