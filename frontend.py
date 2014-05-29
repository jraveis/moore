################
#This script will only parse the user input.
################


#!/usr/bin/python
import sys
import os
import pickle
import math
import time
import getpass
import Project as project
import Task as task
import subprocess

#How accurate the user is. Need to update to actually reflect user's accuracy.
userMult = 1.0
	
		
def createProject(name):
	#Check if the path is taken.
	if not os.path.exists(pathToFolder + "/" + name):
		#If it isn't, create the folder,
		os.mkdir(path+"/"+name);
		dueDate = input("Does your project have a specific due date? Enter in d/m/y format. Give full month and year. If none, hit enter.\n")
		if dueDate != '':
			dueDate = time.strptime(dueDate,"%d/%m/%Y")
			newProject = project.Project(name, due=dueDate)
		else:
			newProject = project.Project(name)
			
		projects[str(len(projects))] = newProject
		print(projects.items());
		return newP
			
	#If the path is taken, ask for a different name.
	else:
		newName = input("Try a different project name. This one is taken."+ 
		"Possibly by something that isn't a project")
		createProject(newName)
	

###########################################################
#Method to read the input and call a method on the chosen project
#Takes the project instance as input
#######################################################

def parseMethodName(project):
	if(len(sys.argv)>1):
		cmd2=sys.argv[2]
	else:
		while True:
			cmd2=input("Enter method to be called.\n")
			if cmd2 in methods:
				tempFunc = methods[cmd2]
				curProj.tempFunc()
				return
			else:
				print("Please enter again.\n")
				
		#cmd2 is a method name
		#call this method on the current project
	
def parseProjectName(cmd):
	while True:
		if cmd in projects:
			curProj = projects[cmd]
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
				print(projects.keys())
				cmd=raw_input("type project name")

def getInput():
	name=""
	while name=="":
		name=input("Please enter a name.\n")
	return name				
##############################################################
#The program is called with 0 or more parameters.
#If 0 parameters have to prompt for input
#if 1 parameter then assume the name of project was input
#If 2 parameters name of project and the method to be called on that project
##############################################################	
#Main()
#Will find the current user, find their projects directory
#and then execute user commands on that directory.
##############################################################

#Define the current user.
currentUser = getpass.getuser()

#Define the path to the Projects directory.
pathToProjects = "/home/" + currentUser + "/Projects"

#Check if Projects exists. Create it if it doesn't.
if not os.path.isdir(pathToProjects):
	if not os.path.exists(pathToProjects):
		os.mkdir(pathToProjects)
	#On the offchance the user has a file or symlink or something
	#located at pathToProjects.
	else:
		print("You have a file (or something that isn't a folder)"
		+" located at " + pathToProjects +". Please rename it.")
		exit()

if os.path.exists(pathToProjects + "/" + 'dictionary'):
	projects=pickle.load(open( os.getcwd()+ 'dictionary','r'))
else:
	projects={}
	os.path.touch('dictionary')

if os.path.exists(pathToFile):
	print("hi")

cmd=""
#Define all methods in the dictionary
methods={
	"_add":project.Project.addTask, 
	"_complete":project.Project.completeTask,
	"_next":project.Project.nextTask
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
