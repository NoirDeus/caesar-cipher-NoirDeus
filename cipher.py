#LowerAlpha = "abcdefghijklmnopqrstuvwxyz"
#LAlphaNum = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
#UpperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#UAlphaNum = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]


Input = input("Please enter text to be encrypted:") #Take input from user and pass it into variable Input
Output = ""                                         #Create variable to print

for C in Input:                                     #Cycle through the Input variable
    if ord(C) >= 65 and ord(C) <= 90:               #Test the ord(C) if it is within the range of the ord(UppercaseCharacters)
        y = ord(C) + 5                              #Generate the shifted ord value and passes it to variable y
        if y > 90:                                  #Test to see if y is higher than highest value of the ord(UppercaseCharacters)
           y = (ord(C) - 26) + 5                    #Subtracting total # of characters in the alphabet from ord(C) and adding 5 to get the shift then passes it to variable y
        elif y == 86:                               #Test to see if ord(C) is 86 to account for uppercase "V" not working
            y = 65                                  #Assigns the ord of the letter A to y
        Output += chr(y)                            #Append chr(y) to the end of variable Output
    elif ord(C) >= 97 and ord(C) <= 122:            #Test to orc(C) if it is within the range of the ord(LowercaseCharacters)
        y = ord(C) + 5                              #Generate the shifted ord value and passes it to variable  y
        if y > 122:                                 #Test to see if y is higher than highest vale of the ord(LowercaseCharacters)
            y = (ord(C) - 26) + 5                   #Subtracting total # of characters in the alphabet from ord(C) and adding 5 to get the shift
        elif y == 118:                              #Testing to see if ord(C) is 118 to account for lowercase "v" not working
            y = 97                                  #Assigns the ord of the letter a to y
        Output += chr(y)                            #Append chr(y) to the end of variable Output 
    else:                                           #Test if orc(C) is anything other than the ranges for uppercase or lowercase characters
        y = ord(C)                                  #Pass ord(C) to y
        Output += chr(y)                            #Append chr(y) to the end of variable Output
print("The enrypted message is:" + Output)                                       #Print out Output to get encrypted(shifted) version of Input



# VVV Didn't Work Graveyard  VVV

# Take input to be encrypted from user and adds it to variable
#Input = input("Please enter text to be encrypted:")
# Create variable for output
#Output = ""
# Create variable with string of the alphabet
#Alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#AlphaString = "abcdefghijklmnopqrstuvwxyz"
#AlphaCaps = " "
#AlphaNull = " "
# Create temporary variable
#x = ""
#y = ""
#z = ""
#for L in Input:
        #if L != L.isnumeric() and L.isdigit():
        #if (not L.isnumeric() and not L.isdigit()): 
#        if L == str(" "):
      
#            Output += L
#        else:
#            y = AlphaString.index(L) + 5
#            if y > len(AlphaString):
#                #if AlphaString.index(L) == "v":
#                    #y = AlphaString.index(L)
#                y = (AlphaString.index(L) - len(AlphaString)) + 5
#                #y = (AlphaString.index(L) - 26) + 5
#            Output += AlphaString[y]                
#print(Output)



# Variable for encrypted message
#Output = ""
# Create Dict variable assigning a number as key to each letter of the alphabet as value
#Dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#x = ""
#for L in Input:
#    Dict[L] = x
#    print(x)
    
    #if Dict[value] == L:

#print(Dict)



#print(Output)


#Numbers = range(26)
#Alpha = []
#print(list(Numbers))

#for i in range(ord('a'), ord('z')+1):
#    Alpha.append(i)

#print(list(Alpha))