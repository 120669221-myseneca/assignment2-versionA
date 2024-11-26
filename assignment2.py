#!/usr/bin/env python3
#name: Prince Dungrani
#ID: 120669221
'''
OPS445 Assignment 2
Program: ops445-ZAA 
Name: Prince Dungrani
Semester: "Fall 2024

The python code in this file is original work written by
''Prince Dungrani. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: this thi my OPS445-Assignment-2 version A code. 

'''

import argparse
import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use is not.")
    args = parser.parse_args()
    return args
# create argparse function
# -H human readable
# -r running only

##this function will take 2 inputs- percent and lenght, which will be used to crearte graph. 
def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    ...
# percent to graph function
    num_of_hashes = int(percent * length)
    num_of_spaces = length - num_of_hashes
    return '#' * num_of_hashes + ' ' * num_of_spaces

def get_sys_mem() -> int:
    """return total system memory in kB"""
    ...
    path_of_the_file= '/proc/meminfo' 
    # will try to open the file, if cannot, will return 0
    try:
        with open(path_of_the_file, 'r') as file:  #open file
            for entry in file:  # read all line
                if 'MemTotal:' in entry: #look for MemTotal in lines
                    memory_total = int(entry.split()[1])
                    return memory_total  
    except: #except error
        return 0 #return 

def get_avail_mem() -> int:
    "return total memory that is available"
    ...
    path_of_the_file = '/proc/meminfo'
    try:
        memory_file = open(path_of_the_file, 'r') #open file
        lines = memory_file.readlines() # read line
        memory_file.close() # close file
        for line in lines: #look for memtotal line in each line
            if 'MemAvailable:' in line:
                available_mememory = int(line.split()[1])
                return available_mememory
    except : #ecpect error and return 0 if error
        return 0

def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    ...

def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the resident memory used, zero if not found"
    ...

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...
    # process args
    # if no parameter passed, 
    # open meminfo.
    # get used memory
    # get total memory
    # call percent to graph
    # print

    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.