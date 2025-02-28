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

# b:
def totNumEmp(dict):
    count=0
    for i in dict.values():
        for j in i:
            count+=1
    return count        




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

# ex3:
company_employees = {
"Engineering": {
"Alice": {"age": 30, "role": "Software Engineer"},
"Bob": {"age": 28, "role": "DevOps Engineer"}
},
"HR": {
"Charlie": {"age": 35, "role": "HR Manager"}
}
}
#a:
print(company_employees)

print("before adding david the number of employees in all the company is: ",totNumEmp(company_employees))

company_employees["Engineering"]["David"]={"age":27,"role":"Data Scientist"}

print("after adding the employee David, the dictionary is: ",company_employees)

# b:
print("after adding david the number of employees in all the company is: ",totNumEmp(company_employees))

# c:
dict={"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}

tempDict={}
for i in dict.values():
    tempDict[i]=[]
    for key,j in dict.items():
        if i==j:
            tempDict[i].append(key)
print(tempDict)



