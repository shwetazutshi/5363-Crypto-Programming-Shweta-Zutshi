###############################################
# Name: Shweta Zutshi
# Class: CMPS 5363 Cryptography
# Date: 28 July 2015
# Program 2 - Randomized Vigenere Cipher
###############################################
import random

#the symbols string to generate vigenere tableau
symbols = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

#calculating its length
size = len(symbols)

#function to generate vigenere
def buildVigenere(symbols,seed):
    #make the random number generator use seed
    random.seed(seed)

    n = len(symbols)
    vigenere = [[0 for i in range(n)] for i in range(n)]
    symbols = list(symbols)
    #shuffling the symbols list
    random.shuffle(symbols)
    symbols = ''.join(symbols)    
    for sym in symbols:
        random.seed(seed)
        #a unique list of random numbers
        uniqList = []
        
        #generate the matrix
        for i in range(n):
            r = random.randrange(n)
            
            if r not in uniqList:
                uniqList.append(r)
            else:
                while(r in uniqList):
                    r = random.randrange(n)
            
                uniqList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym
            
    return vigenere
    
#function to print matrix    
def printMatrix(v):
    i=0
    j=0
    k=0
    line = ""

    for i in range(size*size):
        line = line + str(v[j][k])
        k = k + 1
        if k >= size:
            print(line)
            line = ""
            k = 0
            j = j + 1

#function to retrieve key from seed value            
def keywordFromSeed(seed):
    letters = []
    seed = int(seed)
    while seed > 0:
        letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(letters)

#function to encrypt one symbol from message    
def encryptSymbol(v,k,m,ki,mi):
    #finding symbol index in matrix's first row
    i=0
    msg = m[mi]
    for j in range(size):
        if v[i][j] == msg:
            col = j
    #finding key index from matrix's first column
    j=0
    key = k[ki]
    for i in range(size):
        if v[i][j] == key:
            row = i
    return v[row][col]
	
#function to decrypt one symbol from message
def decryptSymbol(v,k,m,ki,mi):
    #finding key index from matrix's first column
    j=0
    key = k[ki]
    for i in range(size):
        if v[i][j] == key:
            row = i
    
    #finding plaintext message index from matrix's first row 
    msg = m[mi]
    i = 0
    #while(i<26):
    for i in range(size):
        if v[row][i] == msg:
            return v[0][i]

#function to encrypt the whole input message
def encryption(message,key,seed):
    #build matrix
    vigenere = buildVigenere(symbols,seed)
    #print matrix
    printMatrix(vigenere)
    #generate ciphertext
    ciphertext = ""
    for i in range(len(message)):
        mi = i
        ki = i% len(key)
        if ord(message[i]) == 32:
            ciphertext += ' ' 
        else:
            ciphertext += encryptSymbol(vigenere,key,message,ki,mi)
    return ciphertext

#function to decrypt whole input message	
def decryption(message,key,seed):
    #generate matrix
    vigenere = buildVigenere(symbols,seed)
    #print matrix
    printMatrix(vigenere)
    #generate plaintext
    plaintext = ""
    for i in range(len(message)):
        mi = i
        ki = i% len(key)
        if ord(message[i]) == 32:
            plaintext += ' ' 
        else:
            plaintext += decryptSymbol(vigenere,key,message,ki,mi)
    return plaintext