from socket import *

client_socket=socket(AF_INET, SOCK_STREAM) #create a socket
client_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

hostIp="127.0.0.1"
portNumber= 7500

client_socket.connect((hostIp, portNumber))#connect socket with port

from tkinter import *

window=Tk()
window.title('Messanger') #give name for this programm

txt=Text(window,width=50) #to do the text area
txt.grid(row=1, column=0, columnspan=2)#give size amd place where text area will be use

txt_entr = Entry(window,width=50) #to do the entry
txt_entr.grid(column=0,row=2)#give size and place for entry

scrollbar = Scrollbar(txt) #to do the scrollbar
scrollbar.place(relheight=1, relx=0.974)#give a place and size scrollbar

def send_message():#here i did the function which can sed message if tkinter
    client_message=txt_entr.get()
    txt.insert(END,"\n"+"You: "+client_message)
    client_socket.send(client_message.encode("utf-8"))

btn= Button(window,text="Send",command=send_message)#its a button which named send
btn.grid(row=2,column=1)

def server_message():
    while True:#here i gave num how many will be repeat
        server_message = client_socket.recv(1024).decode("utf-8")
        print(server_message)
        txt.insert(END,"\n"+server_message)

from threading import *

recv_thread = Thread(target=server_message)
recv_thread.daemon = True
recv_thread.start()

window.mainloop()
