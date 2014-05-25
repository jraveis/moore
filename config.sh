#!/bin/bash

#########################################
#This script should "install" the projorg.py
#script on the user's machine. For now, this
#means creating a folder (in the home directory)
#to store their projects. The script must also
#place the script within their PATH, so that it
#can be called as just "projorg", rather than
#"python projorg.py".
#########################################

#Find the location of this script.
pwd=$(pwd)

#Assume the user is the owner of this script.
#Get the user
user=$(ls -l $pwd/config.sh | awk '{print $3}')

#Check if the user already has a Projects folder.
#If they don't, create it.
if [ ! -d "/home/$user/Projects" ]
	then
		mkdir /home/$user/Projects
fi

#Check if the user already has a folder
#to store the projorg data. If they don't,
#create it.
if [ ! -d "/home/$user/Projects/.obj" ]
	then
		mkdir /home/$user/Projects/.obj
fi

#Modify the projorg file to reference
#the user.
sed -i -e 's/USERNAMEREPLACE/'$user'/g' $pwd/projorg.py
