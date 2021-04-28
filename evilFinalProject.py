import os, configparser, sys, time
from tkinter import *
import hashlib
# from scapy.all import *
#Ethical Hacking Python Application

#function declarations




#MitM Section








#Packet Sniff





#if packet is successful, get hash as a string and compare it to dictionary

#dictionary files
english_password_list = 

#GUI Rigging
window =Tk() #create tkinter GUI object
window.title("Group 1 Final Project")#Project Title
window.geometry('300x200')#Set size of the pane

#Elements of the GUI

#Label for chosen interface
labelInterface = Label(window,text="Select Interface")
labelInterface.grid(column=0,row=0)

#Text input for chosen interface
textInterface = Entry(window,width=20)
textInterface.grid(column=1,row=0)

#Label for victim IP input
labelVictimIP = Label(window,text="Victim IP")
labelVictimIP.grid(column=0,row=2)

#Text input for victim IP
textVictimIP = Entry(window,width=20)
textVictimIP.grid(column=1,row=2)

#Label for router IP input
labelRouterIP = Label(window,text="Router IP")
labelRouterIP.grid(column=0,row=3)


#Text Input for router IP
textRouterIP = Entry(window,width=20)
textRouterIP.grid(column=1,row=3)

#Button for handling execute call
buttonHack = Button(window,text="Hack!",command="confirm")
buttonHack.grid(column=0, rows=4)

#Button for closing the application
buttonClose= Button(window,text="Quit",command="close")
buttonClose.grid(column=1,row=4)
window.mainloop()#keeps window open