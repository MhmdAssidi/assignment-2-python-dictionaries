def mergedFunction(dict1,dict2):
    mergedDict={}
    
    y=list(dict2.keys())
    for i in dict1:
        if i in dict2:
            mergedDict[i]=dict2[i]
        else:
            mergedDict[i]=dict1[i]
    for j in dict2: #add the keys that are in second dictionary
        if j not in mergedDict:
            mergedDict[j]=dict2[j]

    return mergedDict


dict1 = {
    "a": 1,
    "b": 2,
    "c": 3}
dict2 = {
    "b": 10, 
    "d": 4
    }
print(mergedFunction(dict1,dict2))

sentence=input("enter a sentence to print how many times each word repeated: ")
words =sentence.split()
# print(words)
count=0
wordAppearDict={}
for word in words:
    for w in words:
        if word==w:
            count=count+1
    wordAppearDict[word]=count
    count=0
print (wordAppearDict)            



