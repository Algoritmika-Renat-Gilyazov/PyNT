import time
import os

PATH = "C:\\Users\\renat\\OneDrive\\Рабочий стол\\pyproject"

print\
("PyNT 1.0")
while True:
    cd = input("<" + PATH + "> ")
    if cd == "compile":
        time.sleep(1)
        print(">> Compile\n\t> Compiling lib")
        time.sleep(10)
        print("\t> Compiling Daemon")
        time.sleep(2)
        print("Task was ready!")
    elif cd == "console.write":
        text = input("Text: ")
        print(text)
    elif cd == "cd":
        PATH = input("Enter path: ")
    elif cd == "help":
        print("""
            PyNT 1.0:
                compile - compile local directory
                cd - change local directory
                console.write - write the text
                help - get help
                file - work with files
        """)
    elif cd == "file":
        try:
            action = input("Enter create/delete/write/read: ")
            if action == "create":
                filename = input("Enter a filename: ")
                path = open(PATH + '\\' + filename, "w")
                path.close()
                print("File " + filename + " created in " + PATH)
            elif action == "write":
                filepath = input("Enter filepath with filename: ")
                f = open(filepath, "w")
                text = input("Enter data to write: ")
                f.write(text)
                f.close()
            elif action == "read":
                filepath = input("Enter filepath with filename: ")
                f = open(filepath, "r")
                print(f.read())
                f.close()
            elif action == "delete":
                filepath = input("Enter filepath with filename: ")
                os.remove(filepath)
            else:
                print("Error!")
        except:
            print("Error!")
    else:
        print("Command " + '"' + cd + '"' + " not found!")
