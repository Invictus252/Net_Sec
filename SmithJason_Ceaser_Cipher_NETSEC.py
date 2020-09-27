# -----------------------------------------------------------
# Author: Jason Smith
# Description:  Encrypts a text file with a Ceaser Cipher
#
# Outputs:
#   key
#   plaintext
#   ciphertext
#
# email js5986@mcla.edu
# -----------------------------------------------------------

import random,os,sys

def prepareFiles():
  os.system('touch ciphertext')
  os.system('touch plaintext')
  os.system('touch key')
  plainPath = "plaintext"
  cipherPath = "ciphertext"
  keyPath = "key"
  maPath = "ma.txt"
  plainTxtFile = open(plainPath,'r')
  cipherTxtFile = open(cipherPath,'r')
  maTxtFile = open(maPath,'r')
  keyTxtFile = open(keyPath,'r')
  plaintext=plainTxtFile.read()
  ciphertext=cipherTxtFile.read()
  ma = maTxtFile.read()

def createRandomKey(x):
  key = random.sample(x,len(x))
  return key

def runProgram(this_key):
  os.system("echo '" + ''.join(this_key) + "' > key")
  os.system('cat ma.txt | tr [:upper:] [:lower:] | tr -d [:digit:] | tr "[]"  " " | tr -s "   " | tr "a-z" "' +''.join(this_key) +'" > ciphertext')
  os.system('cat ciphertext | tr "' +''.join(this_key) +'" "a-z" > plaintext')

prepareFiles()
key = createRandomKey('abcdefghijklmnopqrstuvwxyz')
runProgram(key)
