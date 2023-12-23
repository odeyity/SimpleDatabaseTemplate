import json
import os

if os.path.exists("db.json") == False:
    f = open("db.json", "x")
    jsonA = open("db.json", "a")
    jsonA.write("{}")
    jsonA.close()
jsonR = open("db.json", "r")
jsonStr = json.load(jsonR)
jsonR.close()




print("-------------------------")
print(" A Very Real Bank Online")
print("-------------------------")
print()
print("1> Register")
print("2> Log in")
opt = input()
if opt == "1":
    print("Register here.")
    user = input("Username: ")
    first = input("Firstname: ")
    last = input("Surname: ")
    pw = input("PIN: ")
    jsonW = open("db.json", "w")
    jsonStr[user] = {}
    jsonStr[user]["first"] = first
    jsonStr[user]["last"] = last
    jsonStr[user]["pass"] = pw
    json.dump(jsonStr, jsonW)
    jsonW.close()
else:
    print("Please log in.")
    while True:
        user = input("Enter Username: ")
        try:
            jsonStr[user]
            break

        except KeyError:
            print("Error! Username does not exist.")



    pw = input("Enter PIN: ")
    while jsonStr[user]["pass"] != pw:
        print("Incorrect PIN.")
        pw = input("PIN: ")
    print("Successfully logged in.")
    print("Welcome to A Very Real Bank Online, " + jsonStr[user]["first"].upper()[0] + " " + jsonStr[user]["last"].capitalize())
print()
print("Press any key to exit.")
input()

