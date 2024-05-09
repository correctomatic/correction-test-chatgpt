import socket
import sys
import _thread
import signal
import datetime
import g4f
import asyncio
import os
import json
import random
import string

print(g4f.Provider.Ails.params)

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    c.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
i = 0

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

def get_current_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    weekday = weekdays.get(now.weekday(), "Unknown")
    month = months.get(now.month, "Unknown")
    day = now.day
    year = now.year
    ampm = 'pm' if hour > 12 else 'am'
    if hour == 0:
        hour = 12
    elif hour > 12:
        hour -= 12
    time = f"{hour}:{minute if minute < 10 else str(minute).zfill(1)} {ampm}"
    return f"It is {time} on {weekday}, {month} {day}, {year} in [location, removed for privacy]\n"


def main(c, numOfThread):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    c.send("\nWelcome to BurgerBot.\n".encode())
    c.send(get_current_time().encode())
    c.send("\n   Type EXIT at any time to log out.\n\n".encode())
    messages = [{"role": "user", "content": "You are BurgerBot, an AI language model that specializes in burgers and owns a fictional burger restraunt named 'Burger Haven'. Answer all questions to the best of your ability."}]
    userid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    with open("conversations/" + userid + '.txt', 'w') as outfile:
        json.dump(messages, outfile)
    while True:
        c.send("> ".encode())
        try:
            rcvdData = str(c.recv(1024).decode()).rstrip()
        except UnicodeDecodeError:
            print("[Thread " + str(numOfThread) + "] Disconnected. Destroying thread.")
            break
        print("[Thread " + str(numOfThread) + "] (IN) " + rcvdData)
        if rcvdData.lower() == "quit" or rcvdData.lower() == "exit":
            print("[Thread " + str(numOfThread) + "] Disconnected. Destroying thread.")
            c.send("\nDisconnecting from server. Goodbye!\n\n".encode())
            break
        sys.stdout = open(os.devnull, "w")
        messages.append({"role": "user", "content": rcvdData})
        try:
            response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, messages=[
                            messages], stream=True)
        except:
            c.send("Something went horribly wrong. Cannot continue.\n".encode())
            print("[Thread " + str(numOfThread) + "] Exception thrown. Destroying thread.")
            break
        sys.stdout = sys.__stdout__
        finaloutput = ""
        for message in response:
            c.send(message.encode())
            finaloutput = finaloutput + message
        finaloutput = finaloutput.rstrip()
        messages.append({"role": "system", "content": finaloutput})
        print("[Thread " + str(numOfThread) + "] (OUT) " + str(finaloutput))
        with open("conversations/" + userid + '.txt', 'w') as outfile:
            json.dump(messages, outfile)
    c.close()

path = "conversations/"
isExist = os.path.exists(path)
if not isExist:
   os.makedirs(path)

while True:
    c, addr = s.accept()
    print("Incoming connection from:", addr)
    _thread.start_new_thread(main, (c, i,))
    i += 1
