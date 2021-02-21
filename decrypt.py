import hashlib
from os import system

#Create the main process

def main():
    print('Welcome, remember to rename your dictionary like "dictionary.txt", if you dont do that the script wont work')
    input('Press enter to continue...')
    system ('cls')
    print('Welcome to decrypt for MD5, sha1, sha224, sha256, sha384, sha512')
    print('Choose the type of encrypt that you want to decrypt:')
    print('1. MD5')
    print('2. sha1')
    print('3. sha224')
    print('4. sha256')
    print('5. sha384')
    print('6. sha512')
    print('7. Exit.')
    option = int(input('Type an option: '))
    if option == 7:
        print('Thanks for using, if you have a suggestion or you want contact with me, you can find me at https://github.com/josephmonsalve')
        exit()
    resolve = str(input('Type the hash that do you want to find: '))
    resolved= open('dictionary.txt', 'r',encoding='utf-8')
    if option == 1:
        hashMd5(resolve,resolved)
    if option == 2:
        hashSha1(resolve,resolved)
    if option == 3:
        hashSha224(resolve,resolved)
    if option == 4:
        hashSha256(resolve,resolved)
    if option == 5:
        hashSha384(resolve,resolved)
    if option == 6:
        hashSha512(resolve,resolved)
    


def hashMd5(resolve,resolved):
    k = False
    for x in resolved:
        a = x.strip('\n')
        a = hashlib.md5(a.encode('utf-8')).hexdigest()
        if a == resolve:
            print('Found, the hash {}, corresponding to {} '.format(resolve,x)) #Encontrado, el hash digitado {}, corresponde a {}
            k = True
            break
            
    if k == False:
        print('could not find the password, please try with another dictionary') #No encontrado, por favor, intente con otro diccionario.

def hashSha1(resolve,resolved):
    k = False
    for x in resolved:
        a = x.strip('\n')
        a = hashlib.sha1(a.encode('utf-8')).hexdigest()
        if a == resolve:
            print('Found, the hash {}, corresponding to {}'.format(resolve,x))
            k = True
            break
    
    if k == False:
        print('could not find the password, please try with another dictionary')

def hashSha224(resolve,resolved):
    k = False
    for x in resolved:
        a = x.strip('\n')
        a = hashlib.sha224(a.encode('utf-8')).hexdigest()
        if a == resolve:
            print('Found, the hash {}, corresponding to {}'.format(resolve,x))
            k = True
            break

    if k == False:
        print('could not find the password, please try with another dictionary')


def hashSha256(resolve,resolved):
    k = False
    for x in resolved:
        a = x.strip('\n')
        a = hashlib.sha256(a.encode('utf-8')).hexdigest()
        if a == resolve:
            print('Found, the hash {}, corresponding to {}'.format(resolve,x))
            k = True
            break
    if k == False:
        print('could not find the password, please try with another dictionary')

def hashSha384(resolve,resolved):
    k = False
    for x in resolved:
        a = x.strip('\n')
        a = hashlib.sha384(a.encode('utf-8')).hexdigest()
        if a == resolve:
            print('Found, the hash {}, corresponding to {}'.format(resolve,x))
            k = True
            break
            
    if k == False:
        print('could not find the password, please try with another dictionary')

def hashSha512(resolve,resolved):
    k = False
    for x in resolved:
        a = x.strip('\n')
        a = hashlib.sha512(a.encode('utf-8')).hexdigest()
        if a == resolve:
            print('Found, the hash {}, corresponding to {}'.format(resolve,x))
            k = True
            break

    if k == False:
        print('could not find the password, please try with another dictionary')

if __name__ == '__main__':
    main()