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
import os

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2023")
    
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    
    parser.add_argument("-H", "--human-readable", action="store_true", help="Prints sizes in human-readable format")
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
        with open(path_of_the_file, 'r') as file:  
            for entry in file:  
                if 'MemTotal:' in entry: 
                    memory_total = int(entry.split()[1])
                    return memory_total  
    except: 
        return 0 

def get_avail_mem() -> int:
    "return total memory that is available"
    ...
    path_of_the_file = '/proc/meminfo'
    try:
        memory_file = open(path_of_the_file, 'r') 
        lines = memory_file.readlines() 
        memory_file.close() 
        for line in lines: 
            if 'MemAvailable:' in line:
                available_mememory = int(line.split()[1])
                return available_mememory
    except : 
        return 0

def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    try:
        command_for_pid = f'pidof {app_name}' 
        output_of_pid = os.popen(command_for_pid).read().strip() 
        if output_of_pid: 
            list_of_pid = output_of_pid.split() 
        else:
            list_of_pid = [] 
        return list_of_pid
    except: 
        print(f"getting errors PIDs for {app_name}")
        return []

def rss_mem_of_pid(proc_id: str) -> int:
    "takes process id and gives memory used or 0 "
    try:
        f = open(f'/proc/{proc_id}/status', 'r') 
        for line in f: 
                if 'VmRSS:' in line: 
                    return int(line.split()[1])  
    except ValueError: 
        return 0

def bytes_to_human_r(kilobibytes: int, decimal_places: int = 2) -> str:
    "turning 1024 KBs into 1 MiB, for example"
    if kilobibytes <= 0:
        return "0 KiB"  
    
    all_suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suffix_count = 0
    result = kilobibytes  
    while result > 1024 and suffix_count < len(all_suffixes) - 1:  
        result /= 1024
        suffix_count += 1
    
    string_result = f'{result:.{decimal_places}f} '
    string_result += all_suffixes[suffix_count]
    return string_result


if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...
if __name__ == "__main__":
    args = parse_command_args()
    
    # if user does not provide any arguments, it will show system memory used
    if not args.program:
        total_memory = get_sys_mem()
        available_memory = get_avail_mem()
        used_memory = total_memory - available_memory
        memory_percent_used = used_memory / total_memory
        
        print(f"Memory         [{percent_to_graph(memory_percent_used, args.length)} | {int(memory_percent_used * 100)}%] {used_memory}/{total_memory}")
    
    # memory percentage per specific program.
    else:
        pids = pids_of_prog(args.program)
        if not pids:
            print(f"{args.program} not found.")
        else:
            total_used_memory = 0
            for pid in pids:
                memory_used = rss_mem_of_pid(pid)
                total_used_memory += memory_used
                percent_used = memory_used / get_sys_mem()
                
                print(f"{pid}         [{percent_to_graph(percent_used, args.length)} | {int(percent_used * 100)}%] {memory_used}/{get_sys_mem()}")
            
            # total percentage of memory used
            total_percent_used = total_used_memory / get_sys_mem()
            if args.human_readable:
                print(f"{args.program}        [{percent_to_graph(total_percent_used, args.length)} | {int(total_percent_used * 100)}%] {bytes_to_human_r(total_used_memory)}/{bytes_to_human_r(get_sys_mem())}")
            else:
                print(f"{args.program}        [{percent_to_graph(total_percent_used, args.length)} | {int(total_percent_used * 100)}%] {total_used_memory}/{get_sys_mem()}")