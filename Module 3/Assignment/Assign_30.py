d={
    "harsh" : 1,
    "hi" : 2,
    "jing" : 3 
}
keys1 =input("enter 1st : ")
keys2 =input("enter 2nd : ")
if keys1 and keys2 in d or keys1 in d or keys2 in d:
    print("keys are there or one key is there")
else:
    print("keys are not there")