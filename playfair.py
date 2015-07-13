###############################################
# Name: Shweta Zutshi
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################
import pprint
import re

def generateAlphabet():
        #Create empty alphabet string
        alphabet = ""

        #Generate the alphabet
        for i in range(0,26):
            alphabet = alphabet + chr(i+65)

        return alphabet
        
def cleanString(s,options = {'up':1,'reDupes':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
        """
        Cleans message by doing the following:
        - up            - uppercase letters
        - spLetters     - split double letters with some char
        - reSpaces      - replace spaces with some char or '' for removing spaces
        - reNonAlphaNum - remove non alpha numeric
        - reDupes       - remove duplicate letters
        @param   string -- the message
        @returns string -- cleaned message
        """
        if 'up' in options:
            s = s.upper()

        if 'spLetters' in options:
            #replace 2 occurences of same letter with letter and 'X'
            s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)

        if 'reSpaces' in options:
			#remove spaces
            space = options['reSpaces']
            s = re.sub(r'[\s]', space, s)

        if 'reNonAlphaNum' in options:
			#remove non alphanumeric
            s = re.sub(r'[^\w]', '', s)

        if 'reDupes' in options:
			#remove duplicate letters
            s= ''.join(sorted(set(s), key=s.index))
            
		
        return s
        
def generateSquare(key):
    """
    Generates a play fair square with a given keyword.

    @param   string   -- the keyword
    @returns nxn list -- 5x5 matrix
    """
    row = 0     #row index for sqaure
    col = 0     #col index for square
    
    #Create empty 5x5 matrix 
    playFair = [[0 for i in range(5)] for i in range(5)]
    
    alphabet = generateAlphabet()
    
    #uppercase key (it meay be read from stdin, so we need to be sure)
    key = cleanString(key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})
    
    #replacing 'J' in key with 'I'
    key = key.replace("J","I")
    #print(key)
    
    #Load keyword into square
    for i in range(len(key)):
        playFair[row][col] = key[i]
        alphabet = alphabet.replace(key[i], "")
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    #Remove "J" from alphabet
    alphabet = alphabet.replace("J", "")
    
    #Load up remainder of playFair matrix with 
    #remaining letters
    for i in range(len(alphabet)):
        playFair[row][col] = alphabet[i]
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    return playFair

def getCodedMsg(message, playFair):
	#clean the message
	#making it uppercase, removing spaces and non-alphanumerics, splitting duplicate double letters with 'X'
	message = cleanString(message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':1})
	
	#replacing 'J' in message with 'I'
	message = message.replace("J","I")
	
	#if length of message is odd, add 'X' at the end
	if len(message)%2 ==1:
		message += 'X'
		
	#print(message)
	l= 0
	newmsg = ''
	#looping till l reaches end of the message
	while(l<len(message)):
		#get locations of the digraph
		x1,y1 = getLocation(message[l],playFair)
		x2,y2 = getLocation(message[l+1],playFair)
		#print(e)
		#print(x1,y1)
		#print(x2,y2)
		
		#if both letters in digraph are in same row
		if(x1 == x2):
			newmsg += playFair[x1][(y1+1)%5]
			newmsg += playFair[x2][(y2+1)%5]
		
		#if both letters in digraph are in same column
		elif(y1 == y2):
			newmsg += playFair[(x1+1)%5][y1]
			newmsg += playFair[(x2+1)%5][y2]
			
		#if both letters in digraph are in different row and column
		else:
			newmsg += playFair[x1][y2]
			newmsg += playFair[x2][y1]
		#incrementing count by 2 for next digraph	
		l+=2
	return newmsg
	
	
def getLocation(letter,playFair):
	#get location of the letter in the matrix
    row = 0
    col = 0

    for i in range(5):
        for j in range(5):
            if (playFair[i][j] == letter):
                row = i
                col =j
    return row,col
	
def getDecodedMsg(message, playFair):	
	l= 0
	newmsg = ''
	#looping till l reaches end of the message
	while(l<len(message)):
		#get locations of the digraph
		x1,y1 = getLocation(message[l],playFair)
		x2,y2 = getLocation(message[l+1],playFair)
		#print(e)
		#print(x1,y1)
		#print(x2,y2)
		
		#if both letters in digraph are in same row
		if(x1 == x2):
			newmsg += playFair[x1][(y1-1)%5]
			newmsg += playFair[x2][(y2-1)%5]
			
		#if both letters in digraph are in same column
		elif(y1 == y2):
			newmsg += playFair[(x1-1)%5][y1]
			newmsg += playFair[(x2-1)%5][y2]
			
		#if both letters in digraph are in different row and column
		else:
			newmsg += playFair[x1][y2]
			newmsg += playFair[x2][y1]
		#incrementing count by 2 for next digraph
		l+=2
	return newmsg
	
print("PlayFair Encryption Tool (P.E.T.)")
print("Written By: Shweta Zutshi")
print("*********************************")
print("Enter")
print("1: Encryption")
print("2: Decryption")
print("3:Quit")
x = input()
print("*********************************")
flag =1

while flag ==1:
    if x == '1':
        print("Enter Your Message:")
        message = input()
        print()
        print("*********************************")
        print("Enter Your Key:")
        key = input()
        playFair = generateSquare(key)  
        print()
        #print("*********************************")
        #for list in playFair:
        #    print(list)
        #print()
        print("*********************************")
        print("Your Encrypted Message is:")
        coded = getCodedMsg(message,playFair)
        print(coded)
        print()
        print("*********************************")
        flag =0
    elif x == '2':
        print("Enter Your Encrypted Message:")
        message = input()
        print()
        print("*********************************")
        print("Enter Your Key:")
        key = input()
        playFair = generateSquare(key)  
        print()
        #print("*********************************")
        #for list in playFair:
        #    print(list)
        #print()
        #print("*********************************")
        print("Your Decrypted Message is:")
        decoded = getDecodedMsg(message,playFair)
        print(decoded)
        print()
        print("*********************************")
        flag =0
    elif x == '3':
        print("Thank you for using this program")
        flag =0
    else:
        print("Wrong Choice !!! Please enter again...")
        print("Enter 1 for Encryption, 2 for Decryption and 3 for Quit:")
        x = input()
