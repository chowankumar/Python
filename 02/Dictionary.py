studend = {
    "name":"chowan",
    "fname":"vikram",
    "rollno": 102,
    "subject": "english"
}


studend["subject"] = "maths"
print(studend)

#studend.pop("fname")
#studend.popitem("fname")



#for loppppp
for data in studend:
    print(data,studend[data])

     

for key,value in studend.items():
    print(key,value)




# conditonal check
if "name" in  studend:
    print("chowan is available")


#dictionary inside dictionary
team ={
    "CEO" : {"name":"chowan","age":22},
    "MANAGER": {"name":"amrat","age":"19"}
}

print(team["CEO"])
print(team["CEO"]["name"])


sqaure_num = {x:x**2 for x in range(6)}
print(sqaure_num)
sqaure_num.clear()




