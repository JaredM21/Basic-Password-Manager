#Import Packages
from cryptography.fernet import Fernet

''' #Used to get a key
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

#master_pwd = input('Create your master password: ')
key = load_key() #+ master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:  # Automatically opens and closes file
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split('|')
            print('User:', user, '', 'Password: ', fer.encrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f: #Automatically opens and closes file
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input('Add password or view existing one (view, add)? Press q to quit ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode/input')
        continue #Brings user back to the while loop