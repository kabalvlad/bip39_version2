import rsa
from cryptography.fernet import Fernet



from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#print(key)


key = b'Y3aLrMSTDSAVPpwa1iy61bo04Q6uEiBRuTyuFcDYehM='
print(key)

f= Fernet(key)
text = b'My super secret message'
encrypted_text = f.encrypt(text)
print(encrypted_text)
detext = f.decrypt(encrypted_text)
print(detext)
                
words = [b'best',b'my my my']
print(words)
enwords = list()
dewords = list()

for word in words:
    enwords.append(f.encrypt(word))
print(enwords)

for word in enwords:
      dewords.append(f.decrypt(word))
print(dewords)

with open("key.txt", "r") as t:
    text = t.read()
print(text)
e_t = f.encrypt(text.encode())
print(e_t)
d_t = f.decrypt(e_t).decode()
with open("keyd.txt", "w") as t:
    t.write(d_t)
print(d_t)
#with open("keye.txt", "w") as t:
    #t.write(str(e_t))
    
with open("keye.txt", "r") as t:
    texte = t.read()
d_td = f.decrypt(texte).decode()

    









    


    