#how to fetch some unique value from a string

arn = "arn:aws:iam::123456789012:user/johndoe"
print(arn.split("/"))
print(arn.split("/")[1])

#concatenate 

str1 = "Docker"
str2 = "Container"
result = str1 + " " + str2
print(result)