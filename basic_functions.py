#function to return the longest word(s) in a string:

def longest_word(sen):

    words = ""

    #code to remove special characters
    
    for i in sen:
        if i.isalpha() or i.isspace():
            words += i

    #variable declarations

    words = words.split()
    words_lengths = []
    max_words = []
    max_words_str = ""

    #code to get the length of each word and the max length

    for i in range(len(words)):
        words_lengths.append(len(words[i]))

    max_length = max(words_lengths)

    #code to locate and return the longest word(s)

    for i in range(len(words)):
        if len(words[i]) == max_length:
            max_words.append(words[i])

    max_words_str = " ".join(max_words)

    if len(max_words) == 1:
        print ("The longest word is: %s." %(max_words_str))

    if len(max_words) > 1:
        print ("The longest words are: %s." %(max_words_str))

#function for calculating the first factorial of a number:

def firstFactorial(num):

    if isinstance(num, int) and num > 0:
        
        factorial = 1
        
        for i in range(num):
            factorial += factorial * i
        
        print ("The first factorial of %d is : %d" %(num,factorial))
    
    else:
    
        print ("Please enter a rounded number greater than zero.")

#function to reverse a string:

def reverseStr(str):
    
    revStr = ""
    
    for i in range(len(str)):
        
        revStr += str[len(str) -1]
        str = str[0:len(str) -1]
    
    print (revStr)

#function to remove vowels from a string:

def removeVowels(str):
    
    newStr = ""
    
    for i in str:
        i = i.lower()
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            newStr += i
    
    print (newStr)

#function to calculate the sum of positive integers from one to a given number:

def adder(num):
    
    if isinstance(num, int) and num > 0:
    
        sum = 0
        
        for i in range(num):
            if i < num:
                num += i
            
        print (num)

    else:
        print("Please enter a rounded number greater than zero.")

#function to capitalise the first letter of each word in a string

def formatName(str):
    
    str = str.title()
            
    print (str)

#function to sort a list numerically:

def sortAscending(nums):
    
    nums.sort()
    
    print (nums)
    
#function to create a new numerically sorted list from a list:

def createSortAscending(nums):
    
    ascendingList = sorted(nums)
    
    print (ascendingList)
    
#function to sort a list numerically descending:

def sortDescending(nums):
    
    nums.sort(reverse=True)
    
    print (nums)
    
#function to create a new numerically descending sorted list from a list:

def createSortDescending(nums):
    
    descendingList = sorted(nums, reverse=True)
    
    print (descendingList)