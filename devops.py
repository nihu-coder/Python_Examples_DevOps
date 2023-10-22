#how to fetch some unique value from a string

arn = "arn:aws:iam::123456789012:user/johndoe"
print(arn.split("/"))
print(arn.split("/")[1])

