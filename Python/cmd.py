import time
txt="Command Line"
hack=0
ip=0
oni=0
print(txt.center(210,"-"))
username=input("Enter your Username:")
i=0
while i == 0:
    if "$" in username:
        print("For list of commands type 'help'")
        msg=input("Enter commands:")
        if msg.lower() == "exit":
            print("Exiting command line....")
            i=1
        elif msg.lower() == "help":
            print("List of Commands:\nHIDEIP: Hides IP address.\nONION: Creates High level Security and Privacy.\nHACK: Finds and Hacks Nearby Device.\nVIRUS: Creates A virus copy and asks for sending it to nearby computer.\nVERIFY: Verifies whether IP address is Hidden.\nHELP:Shows the list of commands.\nEXIT: Exits the command line.\nSTEAL: Takes Personal Information from a nearby computer.\n")
        elif msg.lower() == "hideip":
            print("Hiding IP....")
            for s in range(10, 0, -1):
                print(s, end=' \r')
                time.sleep(1)
            print("IP hidden.")
            ip=1
        elif msg.lower() == "onion":
            print("Applying Onion....")
            for s in range(10, 0, -1):
                print(s, end=' - \r')
                time.sleep(1)
            print("ONION Applied.")
            oni=1
        elif msg.lower() == "hack":
            print("hacking....")
            for s in range(10, 0, -1):
                print(s, end=' - \r')
                time.sleep(1)
            print("Hacked a nearby computer.")
            hack=1
        elif msg.lower() == "virus":
            print("creating a copy of virus....")
            for s in range(10, 0, -1):
                print(s, end=' - \r')
                time.sleep(1)
            print("Virus Created.")
            send=input("Send or delete?:")
            if send.lower() == "send" and hack == 1:
                print("Sending....")
                for s in range(10, 0, -1):
                    print(s, end=' - \r')
                    time.sleep(1)
                print("Sent to a nearby computer.")
            elif send.lower() == "send" and hack == 0:
                print("hacking....")
                for s in range(10, 0, -1):
                    print(s, end=' - \r')
                    time.sleep(1)
                print("Hacked a nearby computer.")
                print("Sending....")
                for s in range(10, 0, -1):
                    print(s, end=' - \r')
                    time.sleep(1)
                print("Sent to a nearby computer.")
            else:
                print("VIRUS DELETED")
        elif msg.lower() == "verify":
            print("verifying....")
            for s in range(10, 0, -1):
                print(s, end=' - \r')
                time.sleep(1)
            if ip == 1 or onion == 1:
                print("IP is hidden as per the protocols.")
            else:
                print("IP is not hidden")
        elif msg.lower() == "steal":
            a=0
            if hack == 1:
                    print("Extracting....")
                    for s in range(10, 0, -1):
                        print(s, end=' - \r')
                        time.sleep(1)
                    print("Stole the data.")
                    a=1
            elif hack == 0:
                print("hacking....")
                for s in range(10, 0, -1):
                    print(s, end=' - \r')
                    time.sleep(1)
                print("Hacked a nearby computer.")
                print("Extracting....")
                for s in range(10, 0, -1):
                        print(s, end=' - \r')
                        time.sleep(1)
                print("Stole the data.")
        else:
            print(msg,"is not a command.")
    else:
        print("Access Denied.")
        username=input("Enter your Username:")
