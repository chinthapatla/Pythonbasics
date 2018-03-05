student = {
    "name" : "Sandeep" ,
    "student_id" : 13135903 ,
    "feedback" : None
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding key")


print("exception handled successfully")