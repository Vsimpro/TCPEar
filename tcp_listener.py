import os
import time
import subprocess

blacklist = input("Your own ip: ").replace(" ", "")

def banner():
    print(""" 
████████╗ ██████╗██████╗               ███████╗ █████╗ ██████╗ 
╚══██╔══╝██╔════╝██╔══██╗              ██╔════╝██╔══██╗██╔══██╗
   ██║   ██║     ██████╔╝    █████╗    █████╗  ███████║██████╔╝
   ██║   ██║     ██╔═══╝     ╚════╝    ██╔══╝  ██╔══██║██╔══██╗
   ██║   ╚██████╗██║                   ███████╗██║  ██║██║  ██║
   ╚═╝    ╚═════╝╚═╝                   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                                                          
    -- Handcraftef with love, by Vsimpro <3
    """)

def port22():
    command = 'sudo tcpdump -nlq "tcp[13] == 2 and dst port 22" | while read x; do echo "${x}"; echo -en \\a; done'
    os.system("clear")
    banner()
    inward = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
    while True:
        line = inward.stdout.readline()
        line = line.decode("utf-8")
        if line:
            log_dict(line, "22")
    
def write(data):
    print("[+]", data)
    with open("log.txt", "a+", encoding="utf-8") as file:
        file.write(data)

def log_dict(echo, port):
    if echo == "\n":
        return
    if echo == "-en a\n":
        return
    if echo == " ":
        return

    data = {}
    datapoint = echo.split(" ")
    time = datapoint[0]
    ip = datapoint[2]
    if blacklist in ip:
        return
    ip = ip.split(".")    
    n_ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}"
    write(f"{n_ip}:{port} -- {time}\n")
