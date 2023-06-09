import threading
import time
from flask import Flask, render_template, redirect

app = Flask(__name__)

heart = "❤"

@app.route('/')
def home():
    text = "<span style='font-family: cursive;'>lemme smash???</span>"
    return render_template('index.html', text=text, heart=heart)

@app.route('/smash1') #u might wanna use ur own dc here
def smash1():
    return redirect('https://discord.com/users/466114601046638593')

@app.route('/smash2') #and here unless u wanna give me the consent to smash
def smash2():
    return redirect('https://discord.com/users/466114601046638593')

def animate_heart(): #no wörk but idc, fix my skill issue if u wanna
    global heart
    while True:
        time.sleep(0.5)
        heart = heart[-1] + heart[:-1]
        if heart[0] == " ":
            heart = heart[1:]
            heart += " "
            if heart[-1] == " ":
                heart = " " + heart[:-1]

heart_thread = threading.Thread(target=animate_heart)
heart_thread.start()

if __name__ == '__main__':
    app.run()
