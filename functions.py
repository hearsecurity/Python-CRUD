import json 
from time import sleep

def software_info():
    """
    Function that shows info about the program. 
    """
    print("\n=================================")
    print("      Register System v.1.0        ")
    print("=================================")
    print("Author: HearSecurity")
    print("Github: https://github.com/hearsecurity ")
    print("Description: A Simple Registration system. ") 
    print("License: GNU (Open Source Project)   ")
    print("===================================\n\n")

def delete_user():

    """
     Function that deletes a user from database.
    """
    
    username = input("[*] Enter Full name: ")
    name = username.replace(" ", "").lower() 
    count = 0 
    new_json = []
    with open('data.json') as f:
        json_data = json.load(f)
        if name in str(json_data):
            print("[+] User found.\n")
            while count < len(json_data):
                if json_data[count]['name'] != name:
                  new_json.append(json_data[count])
                count = count + 1
                
            with open('data.json', 'w') as f:
                json.dump(new_json, f, indent=4)
            print("[+] User Deleted!")
        else:
            print("[-] User Not found.\n")


def update_user():
    
    """
    Function that updates user database.
    """
    username = input("[*] Enter Full name: ")
    username = username.replace(" ", "").lower()
    count = 0 
    with open('data.json') as f:
        json_data = json.load(f)
        if username in str(json_data):
            print("[+] User found.\n")
            new_firstname = input("[*] Enter new firstname: ")
            new_lastname = input("[*] Enter new lastname: ")  
            new_firstname = new_firstname.replace(" ", "").lower()
            new_lastname = new_lastname.replace(" ", "").lower()
            new_cpf = input("[*] Enter new CPF: ")
            new_email = input("[*] Enter new email: ")
            new_phone = input("[*] Enter new phone: ")

            while count < len(json_data):
                if json_data[count]['name'] == username:
                   json_data[count]['name'] = new_firstname + new_lastname 
                   json_data[count]['firstname'] = new_firstname
                   json_data[count]['lastname'] = new_lastname
                   json_data[count]['cpf'] = new_cpf
                   json_data[count]['email'] =  new_email
                   json_data[count]['phone'] = new_phone
                   
                   break
                count = count + 1
            with open('data.json', 'w') as f:
                json.dump(json_data, f, indent=4) 

            print("[+] Database updated successfully.\n")   
        else:
            print("[-] User Not found.\n")

def read_user():
    
    """
    Function that read users from database.
    """
    
    print("""
      ==========================
      #  1 -> Search by id    #
      #  2 -> Search by name  #
      ==========================
    """)

    option = int(input("[*] Enter search type: "))
    if option == 1:
       id = int(input("[*] Enter user ID: "))
       with open('data.json') as f:
           json_data = json.load(f)
           
           print("[*] Searching..")
           sleep(2)
           try: 
            
             print("\n===========================================")
             print("[+] User Information.")
             print("===========================================")
             print("[*] Nome: "+json_data[id]["firstname"])
             print("[*] Sobrenome: "+json_data[id]["lastname"])
             print("[*] CPF: "+json_data[id]["cpf"])
             print("[*] Email: "+json_data[id]["email"])
             print("[*] Phone: "+json_data[id]["phone"])
             print("===========================================")
             print("\n")
           except IndexError:
             print("[-] User not found.\n")

    elif option == 2:
       username = input("[*] Enter Full name: ") 
       username = username.replace(" ", "").lower()

       count = 0
       with open('data.json') as f:
           json_data = json.load(f)
           print("[*] Searching..")
           sleep(2)
           while count < len(json_data):
             if json_data[count]['name'] == username:
                
                print("\n===========================================")
                print("[+] User Information.")
                print("===========================================")
                print("[*] Nome: "+json_data[count]["firstname"])
                print("[*] Sobrenome: " + json_data[count]["lastname"])
                print("[*] CPF: "+json_data[count]["cpf"])
                print("[*] Email: "+json_data[count]["email"])
                print("[*] Phone: "+json_data[count]["phone"])
                print("===========================================")
                print("\n")
                break
             else:
                print("[-] User Not found..\n")
            
             count = count + 1
             
                
    else:
             print("[-] Invalid Name or ID.. ")


def create_user():
    """
    Function that creates a user.
    """
    
    firstname = input("[*] First Name: ")
    lastname = input("[*] Last Name: " )
    cpf = input("[*] CPF: " )
    email = input("[*] Email: ")
    phone = input("[*] Phone: ")

    fullname = firstname.replace(" ", "").lower() + lastname.replace(" ", "").lower()

    with open('data.json') as f:
       json_data = json.load(f)
    
    if fullname in str(json_data):
        print("[-] User already exists! Try again!\n")
        exit()

    length = len(json_data)

    data = {
        "id": length,
        "name": firstname.lower() + lastname.lower(), 
        "firstname": firstname, 
        "lastname": lastname,
        "cpf": cpf, 
        "email": email,
        "phone": phone
    }

    with open('data.json') as f:
       json_data = json.load(f)
       json_data.append(data)

    with open('data.json', 'w') as f:
        json.dump(json_data, f, indent=4)
    
    print("[+] User created successfully\n")


