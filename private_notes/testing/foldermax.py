import os
import sys

# have a folder created for every user
# if user upload pics or video, save it to their folder
# render olnly one thing at a time, by clciking on saved files,
# allow user to delete file = s.remove(location, file)
# tie all together tomorrow with made app
# make app look nice

# script_path = os.path.realpath(__file__)
# new_abs_path = os.path.join(script_path, 'fol_near_script')
# this ok
#if not os.path.exists('fol_in_pwd'):
#    os.mkdir('fol_in_pwd')

# souce : https://www.geeksforgeeks.org/os-module-python-examples/
path = "static/uploads"
dir_list = os.listdir(path) 
  
print("Files and directories in '", path, "' :") 
  
# print the list 
print(dir_list) # this create a list of files in 
# a user directory, make a clickable list to view file