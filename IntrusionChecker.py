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


class IntrussionChecker:
    def __init__(self):
        if len(shell_arguments) == 2:
            self.file = shell_arguments[1]
            self.open_file = self.open_file()
            self.convert = self.str_to_list(self.open_file)
            self.counting = self.counting(self.convert)
            self.show_counting_values(self.counting)
            
        elif len(shell_arguments) == 3:
            self.file = shell_arguments[1]
            self.write_file = shell_arguments[2]
            self.open_file = self.open_file()
            self.convert = self.str_to_list(self.open_file)
            self.counting = self.counting(self.convert)
            self.create_csv(self.write_file,self.counting)
        elif len(shell_arguments) > 3:
            self.sintax()
            exit()
        else:
            self.sintax()
            exit()
        
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
    #IntrussionChecker()
    RunQuery()
            
