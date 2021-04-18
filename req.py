file = open("config.txt", "w")
username = input("Enter the username: ")
password = input("Enter password: ")
process = username + " "+password
file.write(process)
file.close()
