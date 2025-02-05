import string
import time

def ui():
    print("enter content")
    content = input(";")
    innerworkings(content)
    return content

def innerworkings(content):
    amnt = content.count("e")
    print(amnt)
    time.sleep(1)
    ui()

ui()

