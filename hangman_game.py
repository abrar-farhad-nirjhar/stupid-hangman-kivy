import linecache
import random

f = open('words.txt', 'r')
number_of_words = 0
for i in f:
    number_of_words+=1







# def punishment(i):
#     if i==1:
#         print(" O ")
    
#     elif i==2:
#         print(" O ")
#         print("/")

#     elif i==3:
#         print(" O ")
#         print("/|")
#     elif i==4:
#         print(" O ")
#         print("/|\\")
#     elif i==5:
        
#         print(" O ")
#         print("/|\\")
#         print("/")
#     elif i==6:
        
#         print(" O ")
#         print("/|\\")
#         print("/ \\")

max_len = -1

def get_word():
    r = random.randint(0,number_of_words)
    return linecache.getline("words.txt",r)

def get_max_len():
    max_len=-1

    f = open('words.txt', 'r')
    for i in f:
        # print(len(i))
        if len(i)>max_len:
            print(len(i))
    # return linecache.getline("words.txt",r)
            max_len = len(i)
    return max_len





def game():
    word = get_word()
    print(word[0])
    letters = list('_')*len(word)
    print(letters)

    



# game() 

print("This is the max",get_max_len())