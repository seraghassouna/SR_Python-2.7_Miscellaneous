#Author: Serag Hassouna
#Purpose: Load an AutoLISP file (here named "linedraw.lsp") to a specified drawing (here named "TestDwg.dwg")
#A resolved issue related to the comtypes module:
#https://stackoverflow.com/questions/52111215/get-the-running-autocad-application-using-comtypes-in-python-2-7
#Originally posted on:
#https://forums.autodesk.com/t5/visual-lisp-autolisp-and-general/postcommand-doesn-t-read-autolisp-expression-python-2-7-amp/m-p/8240696#M373595

#Import needed modules
import os
import comtypes.client
from comtypes import COMError
from comtypes.client import CreateObject, GetModule, GetActiveObject

#Uncomment it if you need to load these type libraries.
'''
#Load all needed type libraries
GetModule("C:/Windows/System32/stdole2.tlb")
import comtypes.gen.stdole as ole
print "stdole2 successfully loaded"
GetModule("C:/Program Files/Common Files/Autodesk Shared/acax20enu.tlb")
import comtypes.gen._4E3F492A_FB57_4439_9BF0_1567ED84A3A9_0_1_0 as acax
print "acax20enu successfully loaded"
GetModule("C:/Program Files/Common Files/Autodesk Shared/AcSmComponents20.tlb")
import comtypes.gen._ED125AFF_6294_4BE4_81E2_B98DCBBA214E_0_1_0 as AcSm
print "AcSmComponents20 successfully loaded"
'''

def main():
    #1- Get the AutoCAD instance
        try:
            acad = GetActiveObject("AutoCAD.Application.20")
            print "AutoCAD is Active"
            print "########"
        except(OSError, COMError): #If AutoCAD isn't running, run it
            acad = CreateObject("AutoCAD.Application.20",dynamic=True)
            print "AutoCAD is successfuly Opened"
            print "########"

    #2- Get the paths to the lisp file and the dwg file
    directory_name = "E:\\Dir1\\Dir2" #replace it with a real path, use "\\" as directory delimiters.
    '''
    Note that "\\" is transformed automatically to "\", & in order to comply with
    the AutoLISP "load" function, every "\" must be transformed again to "/".
    '''

    temp=""
    for char in directory_name:
        if char == "\\":
            temp += "/"
        else:
            temp += char
    directory_name = temp
    filename = directory_name + "/TestDWG.dwg"
    lispfile = directory_name + "/linedraw.lsp"

    #3- Open the drawing file
    print "Opening Drawing File ..."
    doc = acad.Documents.Open(filename)
    print "Drawing is successsfuly Opened"
    print "########"

    #4- Construct the AutoLISP expression that loads AutoLISP files
    command_str = '(load ' + '"' + lispfile + '")' + " "

    #5-Execute the AutoLISP expression
    print "Sending AutoLISP Expression ..."
    print "Expression: " + command_str
    doc.SendCommand("(setq *LOAD_SECURITY_STATE* (getvar 'SECURELOAD)) ")
    doc.SendCommand("(setvar \"SECURELOAD\" 0) ")
    doc.SendCommand(command_str)
    doc.SendCommand("(setvar \"SECURELOAD\" *LOAD_SECURITY_STATE*) ")
    print "AutoLISP Expression is successfuly sent"
    print "########"

    #6- Close the drawing file and AutoCAD application
    doc.Save()
    doc.Close()
    acad.Quit()

    print "Process Finished"
    print "__________"

if __name__ == '__main__':
    main()
