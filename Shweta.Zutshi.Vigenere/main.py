###############################################
# Name: Shweta Zutshi
# Class: CMPS 5363 Cryptography
# Date: 28 July 2015
# Program 2 - Randomized Vigenere Cipher
###############################################
import argparse
import sys
import randomized_vigenere as rv

def main():

    #Parse parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed", help="Integer seed")
    args = parser.parse_args()
    
    #generating key from seed
    key = rv.keywordFromSeed(args.seed)
    #opening an input file with read mode
    input = open(args.inputFile, 'r')
    message = input.read()
        
    cipherText = ""
    plainText = ""
    if(args.mode == 'encrypt'):
        #encryption of input message
        cipherText = rv.encryption(message,key,args.seed)
        #writing to output file
        output = open(args.outputFile,'w')
        output.write(str(cipherText))
        
    else:
        #decryption of input message
        plainText = rv.decryption(message,key,args.seed)
        #writing to output file
        output = open(args.outputFile,'w')
        output.write(str(plainText))
		
if __name__ == '__main__':
	main()