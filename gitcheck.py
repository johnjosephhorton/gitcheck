#!/usr/bin/env python 

__author__ = 'John J. Horton'
__description__ = 'Reports counts of modified and untracked files in all git directories within a passed directory.'
__copyright__ = 'Copyright (C) 2012  John Joseph Horton'
__license__ = 'GPL v3'
__maintainer__ = 'johnjosephhorton'
__email__ = 'john.joseph.horton@gmail.com'
__status__ = 'Development'
__version__ = '0.1'

import os 
import sys 
import argparse
import subprocess 

def git_status(path): 
    '''
    Gets a git 'porcelain' status update from a repository, which is a list of 
    statuses, ??, M, D, A etc..
    '''
    try: 
        p = subprocess.Popen(["git", "--git-dir=" + os.path.join(path, ".git"), "--work-tree=" + path, "status", "--porcelain"], stdout = subprocess.PIPE)
        output , err = p.communicate()  
    except: 
        print("Problem with so-called git directory %s" % path)
        output = ""
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

def status_tally(path, verbose): 
    '''
    Gets the porcelain status of a passed directory and returns the count of 
    files of different git status types. 
    '''
    codes = [y[:2] for y in  git_status(path).split("\n")]
    if verbose: 
        return tally(codes) 
    else: 
        if ' M' in tally(codes):
            return tally(codes) 

def main(): 
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("dir", help="directory to check")
    parser.add_argument("-v", "--verbose", action = "store_true", default = False, 
                        help = "show all git statuses (default is only directories with modified files)")
    parser.add_argument("-a", "--abspath", action = "store_true", default = False, 
                        help = "show absolute path to directory (default is relative path to dir)")
    args = parser.parse_args()
    if args.dir: 
        directory = args.dir
    else: 
        directory = "." 
    for dirname, dirnames, filenames in os.walk(directory):
        for subdirname in dirnames:
            if subdirname == ".git": 
                status_message = status_tally(dirname, args.verbose)
                if status_message: 
                    if args.abspath: 
                        pretty_dirname = dirname
                    else:
                        pretty_dirname = "./" + os.path.relpath(dirname, directory)
                    modified = status_message[" M"] if " M" in status_message else 0 
                    untracked = status_message["??"] if "??" in status_message else 0 
                    print(str(modified) + " " + str(untracked) + " " + pretty_dirname)


if __name__ == '__main__':
    main() 
