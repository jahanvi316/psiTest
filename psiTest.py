
def countChars(string, numOfLetters):   # method to count the number of characters; number of each character in a string
    chars = {}
    i=0
    for x in string:
        x = string[i:i+numOfLetters]
        keys = chars.keys()
        if x in keys:
            chars[x] += 1
        else:
            chars[x] = 1
        i+=numOfLetters
    return chars
 
def totalChars(string): # method returning total length of string
   return len(string)


def frequency(string, numOfLetters): # method returning frequencies of each character
    chars = countChars(string, numOfLetters)
    length = totalChars(string)
    freq = {}
    for x in chars:
        freq[x] = chars[x] / length
    return freq

def psi(string, numOfLetters): # method returning the PSI calculated using the frequency method (sum of frequencies squared)
    freq = frequency(string, numOfLetters)
    psi = 0
    for x in freq:
        psi += freq[x] * freq[x]
    return psi

# testString = "this is a test"
# print("Character Count: ", countChars(testString))
# print("Total Characters: ", totalChars(testString))
# print("Frequency: ", frequency(testString))
# print("PSI Test: ", psi(testString))

f = open("alice_permuted.txt", "r")

#set alicePerm variable to file; tested on a small string, comment line 43 and uncomment 44 to test on test string
alicePerm = f.read()
#alicePerm = "this is a test"

grouping = 1
totalCharsInt = totalChars(alicePerm)
print("\033[1m Total Characters:  \033[0m", totalCharsInt)
print(" ") 

print("\033[1m GROUPING OF \033[0m", grouping)
print("\033[1m Character Count: \033[0m", countChars(alicePerm, grouping))
print("\033[1m Frequency:  \033[0m", frequency(alicePerm, grouping))
print("\033[1m PSI Test:  \033[0m", psi(alicePerm, grouping))
print(" ") 

# uncomment lines 58-64 to do all groupings; groupings will go up to total length of text; for more detail, also uncomment lines 60-61
# while(grouping < totalCharsInt):
#     print("\033[1m GROUPING OF \033[0m", grouping)
#     # print("\033[1m Character Count: \033[0m", countChars(alicePerm, grouping))
#     # print("\033[1m Frequency:  \033[0m", frequency(alicePerm, grouping))
#     print("\033[1m PSI Test:  \033[0m", psi(alicePerm, grouping))
#     print(" ") 
#     grouping +=1
