import os
import platform
def print_tree(directory, indent=""):
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            print(indent + "|-- " + item)
            if os.path.isdir(item_path):
                print_tree(item_path, indent + "    ")
    except PermissionError:
        print(indent + "|-- [Access Denied]")
def error(a):
    print(a,"is not a valid command.")
def print_system_details():
    print("System Details:")
    print("OS: " + platform.system() + " " + platform.release())
    print("Architecture: " + platform.architecture()[0])
    print("Machine: " + platform.machine())
    print("Processor: " + platform.processor())
    print("Python Version: " + platform.python_version())
    user = os.environ.get('USERNAME') or os.environ.get('USER')
    print("User: " + user)
    print("Current Working Directory: " + os.getcwd())
lock=False
command_list={"IPCONFIG":"GETS INFO ABOUT YOUR IP ADDRESS.","OSINFO":"INFO ABOUT OS","EXIT":"EXITS THE PROGRAM","IPHIDE":"LOCKS IP ADDRESS.","IPSHOW":"UNLOCKS IP ADDRESS.","HACK":"TYPES CODES LIKE HACKING"}
print("Nirwan Corporation [Version 2.0.0001]")
print("Copyright 2024 Nirwan Corporation. All rights reserved.")
prompt=input("Enter Username:")
while True:
    if "$" in prompt:
        print("ACCESS GRANTED.")
        print("Type \Help for list of commands.")
        break
    elif prompt.lower()=="exit":
        exit()
    else:
        print("ACCESS DENIED.")
        prompt=input("Enter Username:")
while True:
    prompt=input("C:/Users>")
    if prompt.lower()=="\help":
        print("For more information on any command type HELP and command name.\n")
        for name, use in command_list.items():
            print("Command Name:",name,"Command's Function:",use)
    elif prompt.startswith("help-"):
        cmd=prompt[5:].upper()
        if cmd in command_list:
            print("Command Name:",cmd,"Command's Function:",command_list[cmd])
        else:
            error()
    elif prompt.lower()=="exit":
        print("Exiting Application.")
        break
    elif prompt.lower()=="ipconfig" and lock==False:
        output = os.popen('ipconfig' if os.name == 'nt' else 'ifconfig').read()
        print(output)
    elif prompt.lower()=="ipconfig" and lock==True:
        print("IP Address is locked.")
    elif prompt.lower()=="iphide":
        print("IP is locked.")
        lock=True
    elif prompt.lower()=="ipshow":
        print("IP is unlocked.")
        lock=False
    elif "hack" in prompt.lower():
        while True:
            print("Initializing Hack Attempt.....")
            output = os.popen('ipconfig' if os.name == 'nt' else 'ifconfig').read()
            print(output)
            print("IP ADDRESS STATUS:","OK")
            root_dir = os.getcwd()
            print("Directory tree for:", root_dir)
            print_tree(root_dir)
            print_system_details()
            print("Hack Attempt Successful")
            break
    elif prompt.lower()=="osinfo":
        print_system_details()
    else:
        error(prompt)
