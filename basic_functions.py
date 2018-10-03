#function to return the longest word(s) in a string:

def longestString(sen):
   
    #code to remove special characters
    
    wrds = ""
    for i in sen:
        if i.isalpha() or i.isspace():
            wrds += i

    #code to get the length of each word

    wrds = wrds.split()
    wrdsLens = []
    
    for i in range(len(wrds)):
        wrdsLens.append(len(wrds[i]))
        i += 1

    #code to locate and return the longest word(s)

    lngstWrd = max(wrdsLens)
    lngstWrdInd = wrdsLens.index(lngstWrd)
    
    print (wrds[lngstWrdInd])

longestString("The world is huge.")