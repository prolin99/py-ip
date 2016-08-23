import socket
from tkinter import *

def getmyip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    return (s.getsockname()[0])
    s.close()

def get_mac_address():
    import uuid
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac
class My_GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.displayText = Label(self, width="30" , height="3" )
        self.displayText["text"] = "電腦登記"
        self.displayText.grid(row=0, column=0 , columnspan=6 )

        self.inputText = Label(self , width="30" , height="2" )
        self.inputText["text"] = "IP:" + getmyip()
        self.inputText.grid(row=1, column=0, columnspan=6)
        self.inputText2 = Label(self,  width="30" , height="2")
        self.inputText2["text"] = "MAC:" + get_mac_address()
        self.inputText2.grid(row=2, column=0, columnspan=6)

        self.inputText3 = Label(self, height="2")
        self.inputText3["text"] = "使用者:"
        self.inputText3.grid(row=3, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=3, column=1, columnspan=5)

        self.inputText4 = Label(self, height="2")
        self.inputText4["text"] = "位置:"
        self.inputText4.grid(row=4, column=0)
        self.inputField2 = Entry(self)
        self.inputField2["width"] = 50
        self.inputField2.grid(row=4, column=1, columnspan=5)

        self.send = Button(self )
        self.send["text"] = "送出資料"
        self.send.grid(row=5, column=3)
        self.send["command"] =  self.sendMethod



    def sendMethod(self):
        #self.displayText["text"] = "This is send button."
        user = self.inputField.get()
        place = self.inputField2.get()
        if user ==""   or place=="" :
            self.displayText["text"]=" 不可以留空白"
        else:

            file = open('urllink.txt', 'r')
            web = file.read() + "&user="+user +"&place=" + place
            file.close()
            self.displayText["text"]= web
            import urllib.request
            with urllib.request.urlopen(web) as response:
                html = response.read()


if __name__ == '__main__':
    root = Tk()
    app = My_GUI(master=root)
    app.mainloop()
