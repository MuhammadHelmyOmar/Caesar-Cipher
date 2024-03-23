#This function asks the user for a text and a shift so it can encrypt the text with caesar cipher
def encrypt(texte,shifte):
    shifte=int(shifte)
    l1=[]
    for i in texte:
        if i.isalpha():
            num=ord(i)+shifte
            if i.isupper():
                if num>ord('Z'):
                    num-=26
                    l1.append(chr(num))
                elif num<=ord('Z'):
                    l1.append(chr(num)) 
            else:
                if num>ord('z'):
                    num-=26
                    l1.append(chr(num))
                elif num<=ord('z'):
                    l1.append(chr(num))                
        else:
            l1.append(i)
    text=''.join(l1)
    return text

#This function decrypts a text encrypted with caesar cipher if the shift is known
def decrypt(textd,shiftd):
    shiftd=int(shiftd)
    l2=[]
    for i in textd:
        if i.isalpha():
            num=ord(i)-shiftd
            if i.isupper():
                if num<ord('A'):
                    num+=26
                    l2.append(chr(num))
                elif num>=ord('A'):
                    l2.append(chr(num)) 
            else:
                if num<ord('a'):
                    num+=26
                    l2.append(chr(num))
                elif num>=ord('a'):
                    l2.append(chr(num))                
        else:
            l2.append(i)
    text=''.join(l2)           
    return text

#We use this function to know the shift of an encrypted text
def shift(x):
    textletters=[]
    for i in x:
        if i.isalpha():
            if i not in textletters:
                textletters.append(i)    
    if len(textletters)<13 or len(x)<=150:
        import tkMessageBox
        tkMessageBox.showinfo("Error","Your text is too small. Please enter a larger text to help us find the key.")        
    else:
        mins={}
        MAX={}
        newdict={}
        main=[]
        maxs={}
        minmain=[]
        key=[]
        val=[]
        key_1=[]
        val_1=[]
        for i in x:
            if i.isalpha():
                if i not in MAX:
                    MAX[i]=1
                else:
                    MAX[i]+=1
        for (letter,value) in MAX.items():
            if value in newdict:
                newdict[value].append(letter)
            else:
                newdict[value]=[letter]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('e')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('t')
            if v<0:
                v+=26                
            main.append(v)  
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('a')
            if v<0:
                v+=26
            main.append(v)  
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('o')
            if v<0:
                v+=26        
            main.append(v)  
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('i')
            if v<0:
                v+=26        
            main.append(v)  
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('n')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('s')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('r')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('h')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('d')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('l')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)
        for k in newdict[f]:
            v=ord(k)-ord('u')
            if v<0:
                v+=26        
            main.append(v)     
        for k in newdict[f]:
            v=ord(k)-ord('c')
            if v<0:
                v+=26        
            main.append(v)
        del newdict[f]
        d=newdict.keys()
        f= max(d)                
        for l in main:
            if l not in maxs:
                maxs[l]=1
            else:
                maxs[l]+=1
        for i in maxs:
            key_1.append(i)
            val_1.append(maxs[i])
        shift_max= key_1[val_1.index(max(val_1))]
        return shift_max

'''GUI'''
from Tkinter import *
import Tkinter as tk
from winsound import PlaySound,SND_FILENAME
from PIL import ImageTk, Image
import tkMessageBox
import os

def DecryptWindow3_ex():
    DecryptWindow1.destroy()
    PlaySound('button-30.wav',SND_FILENAME)
    global DecryptWindow3
    DecryptWindow3=tk.Tk()
    DecryptWindow3.title("Decription")
    DecryptWindow3.geometry('1400x1600')
    menubar = Menu(DecryptWindow3)
    menubar.add_command(label="Back",command=DecryptWindow1_ex4)      
    DecryptWindow3.config(menu=menubar)     
    label1=Label(DecryptWindow3,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow3,text='Please enter the text...',fg='Black',font=('Times',15)).place(x=70,y=60)
    decr_text1=Text(DecryptWindow3,bg='white',bd='20',fg='black',cursor='xterm',relief=RIDGE,width='50',height='35')
    decr_text1.place(x=0,y=100)
    label3=Label(DecryptWindow3,text='Your text decrypted',fg='Black',font=('Times',15)).place(x=1000,y=60)
    decr_text2=Text(DecryptWindow3,bd='20',fg='black',bg='white',cursor='xterm',width='63',height='35',relief=RIDGE)
    decr_text2.place(x=810,y=100)
    def ShowDecrypt():
        decr_text2.delete('1.0',END)
        x=decr_text1.get("1.0","end-1c")
        if x.strip()=='':
            tkMessageBox.showinfo("Error","Please enter a text.")        
        else:
            textd=decr_text1.get("1.0","end-1c")
            shiftd=shift(x)
            finaltext=decrypt(textd,shiftd)
            PlaySound('button-39.wav', SND_FILENAME)
            decr_text2.insert(END,finaltext)      
    button=Button(DecryptWindow3,text='Decrypt',height="2",width="8",fg='orange',bg='red4', font=('Times',15,'bold'),cursor='hand2',relief=RIDGE,command=ShowDecrypt).place(x=575,y=100)   
    img=Image.open("caesarcipher2.gif")
    img=img.resize((360,600), Image.ANTIALIAS)
    panel_pic=ImageTk.PhotoImage(img)
    panel=tk.Label(DecryptWindow3,image=panel_pic)
    panel.place(x=445,y=163)    
    DecryptWindow3.mainloop()

def DecryptWindow1_ex5():
    window2.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow1
    DecryptWindow1=tk.Tk()
    DecryptWindow1.title("Decription")
    DecryptWindow1.geometry('1400x1600')
    menubar = Menu(DecryptWindow1)  
    menubar.add_command(label="Back",command=start_ex2)      
    DecryptWindow1.config(menu=menubar)     
    label1=Label(DecryptWindow1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow1,text='Decrypt with...',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(DecryptWindow1,text='Known shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow2_ex)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(DecryptWindow1,text='Unknown shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow3_ex)
    button2.pack(side='right',ipadx=300,ipady=500)
    DecryptWindow1.mainloop()

def DecryptWindow1_ex4():
    DecryptWindow3.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow1
    DecryptWindow1=tk.Tk()
    DecryptWindow1.title("Decription")
    DecryptWindow1.geometry('1400x1600')
    menubar = Menu(DecryptWindow1)  
    menubar.add_command(label="Back",command=start_ex2)      
    DecryptWindow1.config(menu=menubar)     
    label1=Label(DecryptWindow1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow1,text='Decrypt with...',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(DecryptWindow1,text='Known shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow2_ex)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(DecryptWindow1,text='Unknown shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow3_ex)
    button2.pack(side='right',ipadx=300,ipady=500)
    DecryptWindow1.mainloop()

#Decryption with unknown key window
def DecryptWindow3():
    DecryptWindow1.destroy()
    PlaySound('button-30.wav',SND_FILENAME)
    global DecryptWindow3
    DecryptWindow3=tk.Tk()
    DecryptWindow3.title("Decription")
    DecryptWindow3.geometry('1400x1600')
    menubar = Menu(DecryptWindow3)
    menubar.add_command(label="Back",command=DecryptWindow1_ex4)      
    DecryptWindow3.config(menu=menubar)     
    label1=Label(DecryptWindow3,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow3,text='Please enter the text...',fg='Black',font=('Times',15)).place(x=70,y=60)
    decr_text1=Text(DecryptWindow3,bg='white',bd='20',fg='black',cursor='xterm',relief=RIDGE,width='50',height='35')
    decr_text1.place(x=0,y=100)
    label3=Label(DecryptWindow3,text='Your text decrypted',fg='Black',font=('Times',15)).place(x=1000,y=60)
    decr_text2=Text(DecryptWindow3,bd='20',fg='black',bg='white',cursor='xterm',width='63',height='35',relief=RIDGE)
    decr_text2.place(x=810,y=100)
    def ShowDecrypt():
        decr_text2.delete('1.0',END)
        x=decr_text1.get("1.0","end-1c")
        if x.strip()=='':
            tkMessageBox.showinfo("Error","Please enter a text.")        
        else:
            textd=decr_text1.get("1.0","end-1c")
            shiftd=shift(x)
            finaltext=decrypt(textd,shiftd)
            PlaySound('button-39.wav', SND_FILENAME)
            decr_text2.insert(END,finaltext)      
    button=Button(DecryptWindow3,text='Decrypt',height="2",width="8",fg='orange',bg='red4', font=('Times',15,'bold'),cursor='hand2',relief=RIDGE,command=ShowDecrypt).place(x=575,y=100)   
    img=Image.open("caesarcipher2.gif")
    img=img.resize((360,600), Image.ANTIALIAS)
    panel_pic=ImageTk.PhotoImage(img)
    panel=tk.Label(DecryptWindow3,image=panel_pic)
    panel.place(x=445,y=163)    
    DecryptWindow3.mainloop()

def DecryptWindow1_ex3():
    DecryptWindow2.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow1
    DecryptWindow1=tk.Tk()
    DecryptWindow1.title("Decription")
    DecryptWindow1.geometry('1400x1600')
    menubar = Menu(DecryptWindow1)  
    menubar.add_command(label="Back",command=start_ex2)      
    DecryptWindow1.config(menu=menubar)     
    label1=Label(DecryptWindow1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow1,text='Decrypt with...',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(DecryptWindow1,text='Known shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow2_ex)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(DecryptWindow1,text='Unknown shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow3)
    button2.pack(side='right',ipadx=300,ipady=500)
    DecryptWindow1.mainloop()

#Decryption with Known key window
def DecryptWindow2():
    DecryptWindow1.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow2
    DecryptWindow2=tk.Tk()
    DecryptWindow2.title("Decription")
    DecryptWindow2.geometry('1400x1600')
    menubar = Menu(DecryptWindow2)  
    menubar.add_command(label="Back",command=DecryptWindow1_ex3)      
    DecryptWindow2.config(menu=menubar)     
    label1=Label(DecryptWindow2,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow2,text='Please enter the text...',fg='Black',font=('Times',15)).place(x=70,y=60)
    decr_text1=Text(DecryptWindow2,bg='white',bd='20',fg='black',cursor='xterm',relief=RIDGE,width='50',height='35')
    decr_text1.place(x=0,y=100)
    label3=Label(DecryptWindow2,text='Please enter the key...',fg='black',font=('Times',15)).place(x=500,y=100) 
    decr_key=Entry(DecryptWindow2,width="5",fg='black',bg='white',font=('Times', 11),cursor='xterm',relief=RIDGE)
    decr_key.place(x=560,y=130)
    label4=Label(DecryptWindow2,text='Your text decrypted',fg='Black',font=('Times',15)).place(x=1000,y=60)
    decr_text2=Text(DecryptWindow2,bd='20',fg='black',bg='white',cursor='xterm',width='63',height='35',relief=RIDGE)
    decr_text2.place(x=810,y=100)
    def ShowDecrypt():
        decr_text2.delete('1.0', END)
        textd=decr_text1.get("1.0","end-1c")
        shiftd=decr_key.get()
        if textd.strip()=='':
            tkMessageBox.showinfo("Error","Please enter a text.")
        else:
            try:
                shiftd=int(shiftd.strip())
                if shiftd>26:
                    tkMessageBox.showinfo("Error","The limit of shifting is 26.")
                elif shiftd<0:
                    tkMessageBox.showinfo("Error","It is better to use the positive numbers from 0 to 26.")
                else:
                    finaltext=decrypt(textd,shiftd)
                    PlaySound('button-39.wav', SND_FILENAME)
                    decr_text2.insert(END,finaltext)         
            except:
                tkMessageBox.showinfo("Error","Please enter a valid key.")                   
    button=Button(DecryptWindow2,text='Decrypt',height="2",width="8",fg='gray88',bg='gray35', font=('Times',15,'bold'),cursor='hand2',relief=RIDGE,command=ShowDecrypt).place(x=530,y=170)
    img=Image.open("julius-caesar2.jpg")
    img=img.resize((350,500), Image.ANTIALIAS)
    panel_pic=ImageTk.PhotoImage(img)
    panel=tk.Label(DecryptWindow2,image=panel_pic)
    panel.place(x=445,y=235)    
    DecryptWindow2.mainloop()

def DecryptWindow1_ex2():
    DecryptWindow2.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow1
    DecryptWindow1=tk.Tk()
    DecryptWindow1.title("Decription")
    DecryptWindow1.geometry('1400x1600')
    menubar = Menu(DecryptWindow1)  
    menubar.add_command(label="Back",command=start_ex2)      
    DecryptWindow1.config(menu=menubar)     
    label1=Label(DecryptWindow1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow1,text='Decrypt with...',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(DecryptWindow1,text='Known shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow2_ex)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(DecryptWindow1,text='Unknown shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow3_ex)
    button2.pack(side='right',ipadx=300,ipady=500)
    DecryptWindow1.mainloop()

def DecryptWindow2_ex():
    DecryptWindow1.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow2
    DecryptWindow2=tk.Tk()
    DecryptWindow2.title("Decription")
    DecryptWindow2.geometry('1400x1600')
    menubar = Menu(DecryptWindow2) 
    menubar.add_command(label="Back",command=DecryptWindow1_ex2)      
    DecryptWindow2.config(menu=menubar)     
    label1=Label(DecryptWindow2,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow2,text='Please enter the text...',fg='Black',font=('Times',15)).place(x=70,y=60)
    decr_text1=Text(DecryptWindow2,bg='white',bd='20',fg='black',cursor='xterm',relief=RIDGE,width='50',height='35')
    decr_text1.place(x=0,y=100)
    label3=Label(DecryptWindow2,text='Please enter the key...',fg='black',font=('Times',15)).place(x=500,y=100) 
    decr_key=Entry(DecryptWindow2,width="5",fg='black',bg='white',font=('Times', 11),cursor='xterm',relief=RIDGE)
    decr_key.place(x=560,y=130)
    label4=Label(DecryptWindow2,text='Your text decrypted',fg='Black',font=('Times',15)).place(x=1000,y=60)
    decr_text2=Text(DecryptWindow2,bd='20',fg='black',bg='white',cursor='xterm',width='63',height='35',relief=RIDGE)
    decr_text2.place(x=810,y=100)
    def ShowDecrypt():
        decr_text2.delete('1.0', END)
        textd=decr_text1.get("1.0","end-1c")
        shiftd=decr_key.get()
        if textd.strip()=='':
            tkMessageBox.showinfo("Error","Please enter a text.")
        else:
            try:
                shiftd=int(shiftd.strip())
                if shiftd>26:
                    tkMessageBox.showinfo("Error","The limit of shifting is 26.")
                elif shiftd<0:
                    tkMessageBox.showinfo("Error","It is better to use the positive numbers from 0 to 26.")
                else:
                    finaltext=decrypt(textd,shiftd)
                    PlaySound('button-39.wav', SND_FILENAME)
                    decr_text2.insert(END,finaltext)         
            except:
                tkMessageBox.showinfo("Error","Please enter a valid key.")                   
    button=Button(DecryptWindow2,text='Decrypt',height="2",width="8",fg='gray88',bg='gray35', font=('Times',15,'bold'),cursor='hand2',relief=RIDGE,command=ShowDecrypt).place(x=530,y=170)
    img=Image.open("julius-caesar2.jpg")
    img=img.resize((350,500), Image.ANTIALIAS)
    panel_pic=ImageTk.PhotoImage(img)
    panel=tk.Label(DecryptWindow2,image=panel_pic)
    panel.place(x=445,y=235)    
    DecryptWindow2.mainloop()

def DecryptWindow1_ex1():
    window2.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow1
    DecryptWindow1=tk.Tk()
    DecryptWindow1.title("Decryption")
    DecryptWindow1.geometry('1400x1600')
    menubar = Menu(DecryptWindow1)  
    menubar.add_command(label="Back",command=start_ex2)      
    DecryptWindow1.config(menu=menubar)     
    label1=Label(DecryptWindow1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow1,text='Decrypt with...',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(DecryptWindow1,text='Known shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow2_ex)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(DecryptWindow1,text='Unknown shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow3)
    button2.pack(side='right',ipadx=300,ipady=500)
    DecryptWindow1.mainloop()

def start_ex3():
    window1.destroy()
    PlaySound('button-30.wav', SND_FILENAME)    
    global window2
    window2=tk.Tk()
    window2.title("Caesar Cipher")
    window2.geometry('1400x1600')
    menubar = Menu(window2)
    menubar.add_command(label="Back",command=home_ex)
    window2.config(menu=menubar)         
    label1=Label(window2,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(window2,text='What do you want to do?',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(window2,text='Encrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=EncryptWindow)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(window2,text='Decrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow1_ex5)
    button2.pack(side='right',ipadx=300,ipady=500)
    window2.mainloop()

def start_ex2():
    DecryptWindow1.destroy()
    PlaySound('button-30.wav', SND_FILENAME)    
    global window2
    window2=tk.Tk()
    window2.title("Caesar Cipher")
    window2.geometry('1400x1600')
    menubar = Menu(window2)
    menubar.add_command(label="Back",command=home_ex)
    window2.config(menu=menubar)         
    label1=Label(window2,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(window2,text='What do you want to do?',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(window2,text='Encrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=EncryptWindow)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(window2,text='Decrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow1_ex5)
    button2.pack(side='right',ipadx=300,ipady=500)
    window2.mainloop()
    
#Main decryption window
def DecryptWindow1():
    window2.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global DecryptWindow1
    DecryptWindow1=tk.Tk()
    DecryptWindow1.title("Encryption")
    DecryptWindow1.geometry('1400x1600')
    menubar = Menu(DecryptWindow1)  
    menubar.add_command(label="Back",command=start_ex2)      
    DecryptWindow1.config(menu=menubar)     
    label1=Label(DecryptWindow1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(DecryptWindow1,text='Decrypt with...',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(DecryptWindow1,text='Known shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow2)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(DecryptWindow1,text='Unknown shift',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow3)
    button2.pack(side='right',ipadx=300,ipady=500)
    DecryptWindow1.mainloop()

def start_ex1():
    EncrWindow.destroy()
    PlaySound('button-30.wav', SND_FILENAME)    
    global window2
    window2=tk.Tk()
    window2.title("Caesar Cipher")
    window2.geometry('1400x1600')
    menubar = Menu(window2)
    menubar.add_command(label="Back",command=home_ex)
    window2.config(menu=menubar)         
    label1=Label(window2,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(window2,text='What do you want to do?',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(window2,text='Encrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=EncryptWindow)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(window2,text='Decrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow1_ex5)
    button2.pack(side='right',ipadx=300,ipady=500)
    window2.mainloop()

#Encryption window
def EncryptWindow():
    window2.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global EncrWindow
    EncrWindow=tk.Tk()
    EncrWindow.title("Encryption")
    EncrWindow.geometry('1400x1600')
    menubar = Menu(EncrWindow)  
    menubar.add_command(label="Back",command=start_ex1)      
    EncrWindow.config(menu=menubar)     
    label1=Label(EncrWindow,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(EncrWindow,text='Please enter the text...',fg='Black',font=('Times',15)).place(x=70,y=60)
    Encr_text1=Text(EncrWindow,bg='white',bd='20',fg='black',cursor='xterm',relief=RIDGE,width='50',height='35')
    Encr_text1.place(x=0,y=100)    
    label3=Label(EncrWindow,text='Please enter the key...',fg='black',font=('Times',15)).place(x=500,y=100)  
    Encr_key=Entry(EncrWindow,width="5",fg='black',bg='white',font=('Times', 11),cursor='xterm',relief=RIDGE)
    Encr_key.place(x=560,y=130)
    label4=Label(EncrWindow,text='Your text encrypted',fg='Black',font=('Times',15)).place(x=1000,y=60)
    Encr_text2=Text(EncrWindow,bd='20',fg='black',bg='white',cursor='xterm',width='63',height='35',relief=RIDGE)
    Encr_text2.place(x=810,y=100)
    def ShowEncrytp():
        Encr_text2.delete('1.0', END)
        texte=Encr_text1.get("1.0","end-1c")
        shifte=Encr_key.get()
        if texte.strip()=='':
            tkMessageBox.showinfo("Error","Please enter a text.")
        else:
            try:
                shifte=int(shifte.strip())
                if shifte>26:
                    tkMessageBox.showinfo("Error","The limit of shifting is 26.")
                elif shifte<0:
                    tkMessageBox.showinfo("Error","It is better to use the positive numbers from 0 to 26.")
                else:
                    finaltext=encrypt(texte,shifte)
                    PlaySound('button-39.wav', SND_FILENAME)
                    Encr_text2.insert(INSERT,finaltext)            
            except:
                tkMessageBox.showinfo("Error","Please enter a valid key.")
    button=Button(EncrWindow,text='Encrypt',height="2",width="8",fg='black',bg='IndianRed4', font=('Times',15,'bold'),cursor='hand2',relief=RIDGE,command=ShowEncrytp).place(x=530,y=170)     
    img=Image.open("caesar-opener.jpg")
    img=img.resize((350,500), Image.ANTIALIAS)
    panel_pic=ImageTk.PhotoImage(img)
    panel=tk.Label(EncrWindow,image=panel_pic)
    panel.place(x=445,y=235)    
    EncrWindow.mainloop()    

def start_ex():
    window1.destroy()
    PlaySound('button-30.wav', SND_FILENAME)    
    global window2
    window2=tk.Tk()
    window2.title("Caesar Cipher")
    window2.geometry('1400x1600')
    menubar = Menu(window2)
    menubar.add_command(label="Back",command=home_ex)
    window2.config(menu=menubar)         
    label1=Label(window2,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(window2,text='What do you want to do?',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(window2,text='Encrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=EncryptWindow)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(window2,text='Decrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow1_ex1)
    button2.pack(side='right',ipadx=300,ipady=500)
    window2.mainloop()

def home_ex():
    window2.destroy()
    PlaySound('button-30.wav', SND_FILENAME)
    global window1
    window1=tk.Tk()
    window1.title("Caesar Cipher")
    window1.geometry('1400x1600')
    image1=tk.PhotoImage(file="image.gif")
    panel1=tk.Label(window1,image=image1)
    panel1.place(relx=0.5,rely=0.5,anchor=CENTER)
    label1=Label(window1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    start_button=Button(window1,text="Let's Start",height="17",width="30",fg='black',bg='white', font=('Times',25),cursor="hand2",relief=RIDGE,command=start_ex3).place(x=0,y=45)
    def help():
        tkMessageBox.showinfo("Help","This programe helps you to encrypt texts using Caesar Cipher or decrypt texts that was encrypted with Caesar Cipher prior. Use this link to learn more about Caesar Cipher: https://www.youtube.com/watch?v=sMOZf4GN3oc")
        os.system("CC-Khan-Academy.mp4") 
    info_label=Label(window1,text="Need Help..!!",height="3",width="41",fg='black',bg='Light Blue',font=('Times',15,'bold')).place(x=850,y=45)
    info_button=Button(window1,fg='black',bg='Light Blue',height="610",width="492",command=help,cursor='hand2',bitmap='question').place(x=850,y=121)
    window1.mainloop()


#2nd window
def start():
    window1.destroy()
    PlaySound('button-30.wav', SND_FILENAME)    
    global window2
    window2=tk.Tk()
    window2.title("Caesar Cipher")
    window2.geometry('1400x1600')
    menubar = Menu(window2)
    menubar.add_command(label="Back",command=home_ex)
    window2.config(menu=menubar)         
    label1=Label(window2,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    label2=Label(window2,text='What do you want to do?',fg='black',font=('Times',15),bg='gold')
    label2.pack(fill=X,ipady=50)
    button1=Button(window2,text='Encrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=EncryptWindow)
    button1.pack(side='left',ipadx=300,ipady=500)
    button2=Button(window2,text='Decrypt',fg='black',bg='olive',font=('Times',15,'bold'),cursor='hand2',command=DecryptWindow1)
    button2.pack(side='right',ipadx=300,ipady=500)
    window2.mainloop()
    
#1st window
def home():
    global window1
    window1=tk.Tk()
    window1.title("Caesar Cipher")
    window1.geometry('1400x1600')
    image1=tk.PhotoImage(file="image.gif")
    panel1=tk.Label(window1,image=image1)
    panel1.place(relx=0.5,rely=0.5,anchor=CENTER)
    label1=Label(window1,text='Caesar Cipher',fg='black',font=('Times',25,'bold italic'),bg='Navajowhite4')
    label1.pack(fill=X)
    start_button=Button(window1,text="Let's Start",height="17",width="30",fg='black',bg='white', font=('Times',25),cursor="hand2",relief=RIDGE,command=start).place(x=0,y=45)
    def help():
        tkMessageBox.showinfo("Help","This programe helps you to encrypt texts using Caesar Cipher or decrypt texts that was encrypted with Caesar Cipher prior.")
        os.system("CC-Khan-Academy.mp4") 
    info_label=Label(window1,text="Need Help..!!",height="3",width="41",fg='black',bg='Light Blue',font=('Times',15,'bold')).place(x=850,y=45)
    info_button=Button(window1,fg='black',bg='Light Blue',height="610",width="492",command=help,cursor='hand2',bitmap='question').place(x=850,y=121)   
    window1.mainloop()
home()

#encrypt('In the aftermath of Mrs May’s election humiliation Mr Williamson was the most enthusiastic supporter of an agreement. He argued that without the DUP’s ten MPs Mrs May could not hope to run a successful minority government and was backed by Sir Jeremy Heywood, the cabinet secretary.',12)

#x='Uz ftq mrfqdymft ar Yde Ymk’e qxqofuaz tgyuxumfuaz Yd Iuxxumyeaz ime ftq yaef qzftgeumefuo egbbadfqd ar mz msdqqyqzf. Tq mdsgqp ftmf iuftagf ftq PGB’e fqz YBe Yde Ymk oagxp zaf tabq fa dgz m egooqeergx yuzadufk sahqdzyqzf mzp ime nmowqp nk Eud Vqdqyk Tqkiaap, ftq omnuzqf eqodqfmdk.'