import sys
import time
from library import lList, lNode
from tqdm import tqdm

mylist = lList()
#Range = number of iterations for the progress bar, Ascii = What characters do you want to fill the bar? Dollar signs or dots are most common
#ncols is the total number of character spaces for the progress bar
for i in tqdm (range(100), desc="Starting up...", ascii = False, ncols=75):
            time.sleep(0.01)
while True:
    item = input(">")
    if item == "quit":
        for i in tqdm (range(100), desc="Shutting down...", ascii = False, ncols=75):
            time.sleep(0.01)
        print("Goodbye...")
        break
    elif item[0:3].lower() == "add":
        mylist.addtolist(item[4:len(item)])
    elif item[0:3].lower() == "del":
        mylist.deletefromlist(mylist, item[4:len(item)])
    elif item[0:3].lower() == "get":
        mylist.getfromlist(mylist, item[4:len(item)])
    elif item[0:3].lower() == "dmp":
        mylist.printlist()
    elif item[0:3].lower() == "siz":
        mylist.sizeoflist(mylist)
    elif item[0:3].lower() == "clr":
        mylist.clearlist(mylist)
    elif item[0:3].lower() == "svf":
        mylist.savelist(mylist, item[4:len(item)])
    elif item[0:3].lower() == "ldf":
        mylist.readlist(mylist, item[4:len(item)])
    elif item[0:3].lower() == "snd":
        print("Please enter the sender's email address or 'quit' to exit: ")
        frommailaddr = input(">>")
        if frommailaddr != "quit":
            print("Please enter the recipient's email address or 'quit' to exit: ")
            tomailaddr = input(">>")
            if tomailaddr != "quit":
                 mylist.sendlist(item[4:len(item)], tomailaddr, frommailaddr)
            else:
                 print("Quitting mail tool...")
        else:
             print("Quitting mail tool...")
    else:
        print("Invalid Command")

