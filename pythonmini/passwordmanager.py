pwd = input("what is the master password? ")

def view():
    with open('passwords.txt', 'a') as f:
        for line in f.readline():
            print(line)
            
            
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
    


while True:
    mode = input("Would you like to add a new password or view existing ones(view,add), press q to quit? ");
    if mode == "q":
      break 

    if mode == "view":
      pass 
    elif mode == "add";
      pass 

    else: 
        print("Invalid mode.")
    continue
