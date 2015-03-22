from tkinter import *
import tkinter.messagebox
import os
class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        
        bottomframe = Frame(root)
        bottomframe.pack( side = BOTTOM )
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack()

        self.encryption = Button(bottomframe, text="Encrypt file", command=self.encrypt)
        self.decryption = Button(bottomframe, text="Decrypt file", command=self.decrypt)
        self.encryption.pack(side=LEFT)
        self.decryption.pack(side=RIGHT)
        self.nameLabel = Label(frame,text="File Name:").pack()
        self.file = Entry(frame, bd =5)
        self.file.pack()
        self.key = Entry(frame, bd =5)
        self.key.pack(side = BOTTOM)
        self.keyLabel = Label(frame,text="Key:").pack(side = BOTTOM)
        
    def quits(self):
        self.root.destroy()
    
    def encrypt(self):
        filename = self.file.get()
        text = ''
        etext = ''
        temptotal = []
        keyvalue = 0
        a = []
        key = self.key.get()
        if filename == '':
            tkinter.messagebox.showerror('DONE','Enter File Name!!!')
        else:
            if os.path.isfile(filename):
                with open(filename) as f:
                    while True:
                        c = f.read(1)
                        if not c:
                            break
                        if len(str(ord(c))) == 2:
                            text = text + '0'+ str(ord(c))
                            
                        elif len(str(ord(c))) == 1:
                            text = text + '00'+ str(ord(c))
                        else:
                            text = text + str(ord(c))
                        
                for c in key:
                    keyvalue = keyvalue + ord(c)
                
                for i in range(0, len(text), len(str(keyvalue))):
                               temp = text[i:i+len(str(keyvalue))]
                               temp = str(int(temp) + keyvalue)

                               temptotal.append(temp)
                for item in temptotal:
                    for c in item :
                        
                        c = str("{0:b}".format(int(c)))
                        if len(c) == 3:
                            c = '0' + c
                        elif len(c) == 2:
                            c = '00' + c
                        elif len(c) == 1:
                            c = '000' + c
                         
                        p1 = (c[:int(len(c)/2)])
                        p2 = (c[int(len(c)/2):])
                        a.append(p1)
                        a.append(p2)
                for item in a:
                    if item == '00':
                        etext = etext + 'A'
                    elif item == '01':
                        etext = etext + 'C'
                    elif item == '10':
                        etext = etext + 'G'
                    else:
                        etext = etext + 'T'
                f = open(filename,'w') 
                f.write(etext)
                tkinter.messagebox.showinfo('DONE','File '+ filename + ' is encrpyted')
            else:
                tkinter.messagebox.showerror('DONE','File Name Doesnt Exist!!')
    def decrypt(self):
        filename = self.file.get()
        text = ''
        dtext = ''
        asci = ''
        temp = ''
        a = []
        temptext = ''
        temptotal = []
        digts = '1'
        key = self.key.get()
        keyvalue = 0
        if filename == '':
            tkinter.messagebox.showerror('DONE','Enter File Name!!!')
        else:
            if os.path.isfile(filename):
                with open(filename) as f:
                    while True:
                        
                        c = f.read(1)
                        if not c:
                            break
                        if c == 'A':
                            digts = digts + '00'
                        elif c == 'C':
                            digts = digts + '01'
                        elif c == 'G':
                            digts = digts + '10'
                        else:
                            digts = digts + '11'
                
                for i in range(1, len(digts),4):
                    
                    temptext = temptext +str(int(digts[i:i+4], 2))
                    
                for c in key:
                    keyvalue = keyvalue + ord(c)
                for i in range(0, len(temptext), len(str(keyvalue))):
                               temp = temptext[i:i+len(str(keyvalue))]
                               
                               temp = str(int(temp) - keyvalue)
                               if len(temp) == len(str(keyvalue)) -1:
                                   temp = '0' + temp
                                   
                               temptotal.append(temp)
                               
                for item in temptotal:
                    asci = asci + item
                   
                '''test = int(asci[0:0+3])
                if test > 255:
                    asci = '0'+asci
                '''
                asci = [asci[i:i+3] for i in range(0, len(asci), 3)] 
              
                for item in asci:
                    try:
                        if chr(int(item)):
                            dtext = dtext + chr(int(item))
                    except:
                        dtext = dtext + 'E'
                f = open(filename, 'w')
                #f.write(filename + ' Decrypted:\n')
                #dtext = str(dtext.encode('ascii', 'replace'))
                f.write(dtext)
                tkinter.messagebox.showinfo('DONE','File '+ filename + ' is decrpyted and Saved as DecryptedFile.txt')
                
            else:
                tkinter.messagebox.showerror('DONE','File Name Doesnt Exist!!')
root = Tk()
app = App(root)
root.mainloop()
root.destroy()

