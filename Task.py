class Task:
	def __init__(self,description,dueDate,hoursEstimate, hoursAtATime,numberOfTimesPerDay):
		#Description of task
		self.description = description
		#Due date of task
		self.dueDate = dueDate
		#User's estimate of hours to complete task
		self.hoursEstimate = hoursEstimate
		#Maximum number of hours spent at once on a single task.
		self.hoursAtATime = hoursAtATime
		#Number of times to work on a task per day.
		self.numberOfTimesPerDay = numberOfTimesPerDay
		
		#Program's estimate of how many days 
		#it will take to complete the task.
		self.PredictedTime = self.daysToComplete()
		
		#The program's estimate of the start date.
		self.predictedStartDate = self.dateToStart()
	
	#Calculates the day on which you should start the task.	
	def dateToStart(self):
		startdate = due - self.PredictedTime
		return startdate
		
	#Calculates how many days you will 
	#actually take to complete the task.
	def daysToComplete(self):
		#The number of days the user thinks it will take.
		userDays = math.ceil(float(self.hoursEstimate / (self.hoursAtATime * self.numberOfTimesPerDay)))
		
		#The number of days the program thinks it will take.
		projDays = userDays * userMult
		return projDays
		
	#Start the task.
	def start(self):
		self.started = True
		self.actualStartDate = time.strftime("%d/%m/%Y")
	
	#Complete the task.	
	def complete(self):
		self.TimeCompleted = time.strftime("%d/%m/%y")
		
	#This classes built in toString method.
	def __str__():
		return ("Text: " + text +", Due Date: " + due + ", Expected Completion Time: " + time + ", Priority: " + priority + ", Time per Day: " + interval + ", Number of Intervals per Day: " + number + "." )
		
	#Built in comparison operator. Python is stupid about these. Possibly we will need to implement others (greater than, less equal, etc) later.
	#We use this function when we order the priority queue.
	def __lt__(self,task):
		return self.predictedStartDate < task.predictedStateDate
