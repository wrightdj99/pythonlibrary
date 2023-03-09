#Special thanks to this link for help with Google's stringent new security standards:
#https://stackoverflow.com/questions/72478573/how-to-send-an-email-using-python-after-googles-policy-update-on-not-allowing-j

import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

class lNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class lList:
    #Our list does not have a head until we assign it one
    def __init__(self):
        self.head = None

    def printlist(self):
        valtoprint = self.head
        while valtoprint is not None:
            print(valtoprint.data)
            valtoprint = valtoprint.next

    def addtolist(self, data):
        nodetoadd = lNode(data)
        #Checking for a node head
        if self.head == None:
            self.head = nodetoadd
            return
        #In any case, we're adding nodetoadd after the last value in the list, which
        #we presume to be the head, but will loop through the list until we find it.
        lastval = self.head
        while(lastval.next):
            lastval = lastval.next
        lastval.next = nodetoadd

    def deletefromlist(self, paramlist, valtorem):
        paramlist = self
        iteratornode = paramlist.head
        if iteratornode is not None:
            if iteratornode.data == valtorem:
                self.head = iteratornode.next
                iteratornode = None
                return
            while iteratornode is not None:
                if iteratornode.data == valtorem:
                    break
                prev = iteratornode
                iteratornode = iteratornode.next
            
            if iteratornode == None:
                return

            prev.next = iteratornode.next
            iteratornode = None

    def getfromlist(self, paramlist, valtoget):
        if paramlist.head != None:
            paramlist = self
            indexcounter = 0
            iteratornode = paramlist.head
            while(iteratornode.next):
                if iteratornode.data == valtoget:
                    print("'",valtoget,"'", "is at index #", indexcounter)
                    break
                iteratornode = iteratornode.next
                indexcounter += 1
            if(iteratornode.next is None):
                if iteratornode.data == valtoget:
                    print("'",valtoget,"'", "is at index #", indexcounter)
                else:
                    return


    def sizeoflist(self, paramlist):
        if paramlist.head == None:
            counter = 0
            print(counter)
            return
        else:
            iteratornode = paramlist.head
            counter = 1
            while(iteratornode.next):
                counter+=1
                iteratornode = iteratornode.next
            print(counter)

    def clearlist(self, paramlist):
        paramlist = self
        if paramlist.head is None:
            return
        else:
            iteratornode = paramlist.head
            while(iteratornode.next):
                paramlist.deletefromlist(paramlist, iteratornode.data)
                iteratornode = iteratornode.next
            paramlist.deletefromlist(paramlist, iteratornode.data)
            return
        
    #To demonstrate Python's "Swiss Army Knife" capabilities, we'll be doing a couple of different things from here on out.
        #We'll be saving the list in this method to a file specified by the end-user when they type "svf *filename*"
        #Next, we'll be writing another method that loads the file contents to the current working library when the user types "ldf *filename*"
        #Finally, we'll be writing one last method that sends files containing library content over email through a server!
    def savelist(self, paramlist, filename):
        paramlist = self
        iteratornode = paramlist.head
        file = open(filename, 'w')
        while(iteratornode.next):
            file.writelines(iteratornode.data + '\n')
            iteratornode = iteratornode.next
        if(iteratornode.next is None):
            file.writelines(iteratornode.data + '\n')
        file.close()

    def readlist(self, paramlist, filename):
        paramlist = self
        iteratornode = paramlist.head
        file=open(filename, 'r')
        readlist = file.readlines()
        for i in readlist:
            i = i[:len(i) - 1]
            self.addtolist(i)

    def sendlist(self, filename, recipientmail, sendermail):
        #Instance of the multipart class
        msg = MIMEMultipart()
        #Storing the sender's email addr
        msg['From'] = sendermail
        #Storing the recipient email addr
        msg['To'] = recipientmail
        #Storing the subject in the msg object
        msg['Subject'] = "You've been sent a Library from: " + sendermail + "!"
        #String to store the body of the mail
        body = "To open this Python-made Library, click on the sent attachment and enjoy!"
        #Attach the body with the msg instance and make it in plain text
        msg.attach(MIMEText(body, 'plain'))
        #Open up the file to be sent.
        #Python might not be the heavyweight champion that C/C++ is when it
        #comes to low-level or kernel development, but it's great for simple tasks like file management!
        filepath = os.path.basename(filename)
        attachment = open(filepath, "rb")
        #Instance of MIMEBase and named as p (Multipurpose Internet Mail Extension)
        p = MIMEBase('application', 'octet-stream')
        #To change the payload into encoded form so that we can transmit all these objects we're setting up
        p.set_payload((attachment).read())
        #Encode into base64
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
        #Attach the instance 'p' to instance 'msg'
        msg.attach(p)
        #Create SMTP session (Secure Mail Transfer Protocol), now that we've got our MIME payload built, time to send it!
        s = smtplib.SMTP("smtp.gmail.com", 587)
        #Start TLS for security purposes
        s.starttls()
        #Authentamacation -- Intentional misspelling :)
        s.login(sendermail, "vrqajwqsvudosekg")
        #Converting the multipart message to a string
        text = msg.as_string()
        #Send the message!
        s.sendmail(sendermail, recipientmail, text)
        s.quit() 
        #Confirmation message
        print("Library sent to: ", recipientmail, "!")








