from tkinter import *
import smtplib


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saadchaudhary646@gmail.com', '65%Saadd.')
    server.sendmail('saadchaudhary646@gmail.com', to, content)
    server.close()


# sendemail('afreenchaudhary8@gmail.com','mdnhvcddavcdgsvchg')

def but(event):
    sendemail(a.get(),b.get())
    print('send')




root = Tk()
root.geometry('500x500')
root.title("SAAD EMAIL SERVICE")
root.configure(bg='#171e5e')


#store variable
a=StringVar()
b=StringVar()


# root.geometry(250*250)
Label(root, text="ENTER YOUR EMAIL ADDRESS BELOW", bg='#171e5e', fg='grey', pady=50, padx=200, font=('Helvetica', 18, 'bold'))

e1 = Entry(root, textvariable=a,font=50)
e1.insert(0, "Enter username")
c = Entry(root, font=50,textvariable=b)
d = Button(root, text="SEND", bg='grey', fg='black', pady=0, padx=200, font=('Helvetica', 18, 'bold'))
d.bind("<Button-1>",but)



#pack
e1.pack(ipadx=262)
c.pack(ipadx=262,ipady=100)
d.pack()
root.mainloop()
