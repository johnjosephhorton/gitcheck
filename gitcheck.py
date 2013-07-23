#!/usr/bin/env python 

__author__ = 'John J. Horton'
__purpose__ = 'Recursively report the statuses of git respositories nested within a passed directory'
__copyright__ = 'Copyright (C) 2012  John Joseph Horton'
__license__ = 'GPL v3'
__maintainer__ = 'johnjosephhorton'
__email__ = 'john.joseph.horton@gmail.com'
__status__ = 'Development'
__version__ = '0.1'

import os 
import sys 
import argparse
import sh
 
def git_status(path): 
    '''
    Gets a git 'porcelain' status update from a repository, which is a list of 
    statuses, ??, M, D, A etc. and the associated files.
    '''
    output = sh.git("--git-dir="+os.path.join(path, ".git"), 
                    "--work-tree="+os.path.join(path,".git"), 
                    "status", porcelain = True)
    return output

def tally(observations): 
    '''
    Returns a dictionary of the counts of the various unique items in the list
    observations. 
    '''
    d = {}
    for obs in observations: 
        if obs in d: 
            d[obs] += 1 
        else: 
            d[obs] = 1
    return d 

def status_tally(path): 
    '''
    Gets the porcelain status of a passed directory and returns the count of 
    files of different git status types. 
    '''
    status = git_status(path) 
    codes = [z[0] for z in [y.split(" ") for y in status.split("\n")]]
    return tally(codes) 

def main(): 
    dir = os.getcwd()
    for dirname, dirnames, filenames in os.walk(dir):
        for subdirname in dirnames:
            if subdirname == ".git": 
                print(dirname + ":" + str(status_tally(dirname)))

if __name__ == '__main__': 
    main() 
#!/usr/bin/env python




