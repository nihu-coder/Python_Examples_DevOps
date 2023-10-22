#how to fetch some unique value from a string

arn = "arn:aws:iam::123456789012:user/johndoe"
print(arn.split("/"))
print(arn.split("/")[1])

#concatenate 

str1 = "Docker"
str2 = "Container"
result = str1 + " " + str2
print(result)

#finding the length 

text = "Python with DevOps is Awesome"
length = len(text)
print("Length of the string:", length)

#convert to lowercase/Uppercase

text = "Python is dynamic"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#Replacing the word in string 

text = "kubernetes is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

#Strip

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

#substring

text = "Python have inbult functions"
substring = "inbuilt"
if substring in text:
    print("found in the text", substring)