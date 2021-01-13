import tkinter
import ast
import requests
root = tkinter.Tk()
root.title("Chat Bot")
root.geometry("400x500")
root.resizable(width=0, height=0)
text = tkinter.StringVar()
conversation=["        Welcome to XYZ company.       \n".center(12)]
text.set("\n".join(conversation))
chatWindow = tkinter.Label(root,textvariable=text, bd=1, bg="black",  width="15", height="8", font=("Arial", 10), foreground="#00ffff",anchor='nw',justify=tkinter.LEFT)
chatWindow.place(x=0,y=0, height=385, width=390)
messageWindow = tkinter.Entry(root, bd=0, bg="black",width="30", font=("Arial", 10), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

def ReadText():
    message=messageWindow.get()
    conversation.append("User: "+message)
    text.set("\n".join(conversation))
    chatWindow.update()

    url = 'http://localhost:5005/webhooks/rest/webhook'  ##change rasablog with your app name
    myobj = {
        "message": message,
        "sender": "User",
    }
    messageWindow.delete(0, 'end')
    x = requests.post(url, json=myobj)
    ast.literal_eval(x.text)
    print(ast.literal_eval(x.text))
    reply=""
    for i in range(len(ast.literal_eval(x.text))):
        if len(ast.literal_eval(x.text)[i]["text"].split(" ")) >9:
            for i in range(len(ast.literal_eval(x.text)[0]["text"].split(" "))//9 +1):
                reply+=" ".join(ast.literal_eval(x.text)[0]["text"].split(" ")[9 * (i - 1):9 * (i - 1) + 9]) + "\n"
        else:
            reply=ast.literal_eval(x.text)[i]["text"]
        conversation.append("Bot: " + reply)
        text.set("\n".join(conversation))

Button= tkinter.Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12),command=ReadText)
Button.place(x=6, y=400, height=88)
root.mainloop()
