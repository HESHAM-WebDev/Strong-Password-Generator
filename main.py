#import string module
#save charcters as lower,upper,digits,punc
#create the loop to accept number of char more than 6 chars
#shuffle all lists by random library
# we give 30% & 20%
import string;
import random;

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


character_number = input("enter number of characters you want : ")

character_number = int(character_number)

while True:
    try:
        character_number = int(character_number)
        if character_number < 6 :
            print('please enter number more than 6 characters')
            character_number = input("please enter the number again : ")
        else:
            break
    except:
            print("please enter numbers only")
            character_number = input("enter number of characters you want : ")


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

password = "".join(password[0:])

print(password)
