import random
import sys

#sym = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-_+=/\,.()[]{}#$%&'
sym = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gen(dlin):
    passArr = ''
    for i in range(10):
        for j in range(dlin):
            #print(sym[int(random.uniform(0,33))])
            passArr += sym[int(random.uniform(0,len(sym)))]
        print(passArr)
        passArr = ''
    
    
if __name__ == "__main__":
    gen(int(sys.argv[1]))