#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:08:55 2020

@author: sincorchetes
"""


from subprocess import run as Execute
from os import getcwd as GetCurrentDir
from getpass import getuser as GetCurrentUser
from shutil import copy as CopySecureFiles
from os import listdir as GetFilesDir
from os import chown as ChangePermissionsFiles
import re
class RunQuery:
    def __init__(self):
        
        self.files = []
        
        if "root" == GetCurrentUser():
            var_log = GetFilesDir("/var/log")
            
            for secure in var_log:
                if "secure" in secure:
                    self.files.append("/var/log/%s" % (secure))
            
            for copy in self.files:
                CopySecureFiles(copy,GetCurrentDir())
            
            for set_perm in self.files:
                ChangePermissionsFiles(set_perm, )
        
        else:
            print("NOT OK")
            
RunQuery()