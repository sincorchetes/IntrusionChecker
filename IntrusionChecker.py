#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:12:36 2020

@author: sincorchetes
@blog: https://echemosunbitstazo.es
@license: GPLv2
"""


from sys import argv as shell_arguments
from collections import Counter
from re import escape as Filter
from shutil import copy as CopySecureFiles
from getpass import getuser as GetCurrentUser
from os import getcwd as GetCurrentDir
from os import listdir as GetFilesDir
from os import stat as GetPerm
from os import chown as ChangePerm
from os import remove as RemoveFile
from subprocess import run as FilterFile
from os import path as Path

class IntrussionChecker:
    def __init__(self):
        
        self.file = "users"
        self.file_to_csv = "users.csv"
        
        if len(shell_arguments) == 2 and shell_arguments[1] == "--copy-files":
            if "root" == GetCurrentUser():
                self.generate_files()
                
            else:
                print("You are not root, please run this script as root with su - or sudo")
        
        elif len(shell_arguments) == 2 and shell_arguments[1] == "--remove-files":
            pass
        elif len(shell_arguments) == 2 and shell_arguments[1] == "--show-users":
           pass
            
        elif len(shell_arguments) == 4 and shell_arguments[1] == "--generate-csv":
            pass
        elif len(shell_arguments) > 3:
            self.sintax()
            exit()
        else:
            self.sintax()
            exit()
            
    def generate_files(self):
        self.var_log = GetFilesDir("/var/log")
        self.copy_files = []
        self.working_perm = GetPerm(".")
        self.data_log = ""
        
        
        for secure in self.var_log:
            if "secure" in secure:
                self.copy_files.append("/var/log/%s" % (secure))
                        
        for copy in self.copy_files:
            CopySecureFiles(copy,GetCurrentDir())
            print("File %s was copied." % (copy))
                
        for file in GetFilesDir("."):
            if "secure" in file:
                ChangePerm(file,self.working_perm.st_uid,self.working_perm.st_gid)
                print("Set user and group perm for this file: %s" % (file))
                
        for file in GetFilesDir("."):
            if "secure" in file:
                with open(file,"r") as log:
                    read = log.read()
                    self.data_log += read
        with open(self.file,mode="w") as users:
            users.write(self.data_log)
    
        FilterFile("cat users | grep 'Invalid user' | awk '{print $8}' | sort >> user_log",shell=True)
        
        
    def delete_files(self):
        for file in GetFilesDir("."):
            if "secure" in file:
                RemoveFile(file)
                print("%s as deleted" % (file))
            elif "users" in file:
                RemoveFile(file)
                print("%s as deleted" % (file))
            elif "users_log" in file:
                RemoveFile(file)
                print("%s as deleted" % (file))
            else:
                pass
        
    def show_users(self):
        if Path.isfile("user"):    
            self.open_file = self.open_file()
            self.convert = self.str_to_list(self.open_file)
            self.counting = self.counting(self.convert)
            self.show_counting_values(self.counting)
        else:
            print("No exist")
    def generate_csv(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        self.open_file = self.open_file()
        self.convert = self.str_to_list(self.open_file)
        self.counting = self.counting(self.convert)
        self.create_csv(self.file_to_csv,self.counting)
        
    def open_file(self,mode="r"):
        try:
            with open(self.file,mode) as file_to_open:
                self.read_file = file_to_open.read()
                return self.read_file
        except FileNotFoundError:
            print("File is not exist.")
        except PermissionError:
            print("File is not readed because does not have read perms.")
        except OSError:
            print("Please, you have to insert filename.")
        
    def str_to_list(self,string):
        if string == None or string == "":
            print("String is empty")
        else:
            self.convert = string.split()
            return self.convert
    
    def counting(self,count):
        if count == None or count == "":
            print("Count is empty")
        else:
            self.counting = Counter(count)
            return self.counting
    
    def show_counting_values(self,count):
        if count == None or count == "":
            print("Count is empty")
        else:
            print("INTRUSION ATTEMPTS")
            for key in count.keys():
                print("User: %s \n"
                      "Connection tries: %i \n" % (Filter(key),count[key]))
            print("## END OF LOG ##")
    
    
    def create_csv(self,write_file,count):
        
        try:
            with open(self.write_file,"w") as csv:
                for key in count.keys():
                    csv.write("%s %i \n" % (Filter(key),count[key]))
            print("File was generated successfully")
        except FileNotFoundError:
            print("File is not exist.")
        except PermissionError:
            print("You cannot write file here, because does not have write permissions.")
        except AttributeError:
            print("Source file does not exist")
            
    
    def sintax(self):
        print("How to use:\n"
              ">>> If you only want print info, just only run:\n\n"
              "./IntrusionCounter.py file_to_query\n\n"
              
              ">>> If you want convert to .csv too:\n\n"
              "./IntrusionCounter.py file_to_query file_to_convert\n\n"
              
              ">>> If you don't have permissions in directory, file won't created.")

    def __del__(self):
        pass
    
if __name__ == '__main__':
    IntrussionChecker()
    
            
