str = "Amit Kumar"
str2 = " Srivastava"
print(str + str2)

print("Length of str  :: ", len(str))

print("Length of concatenate str + str2  ::  ", len(str + str2))

print(str[0],", ",str[1])
print(str2[4:14])
print(str[:len(str)])
print(str2[0:3])
print(str[-1])
print(str[-3])


strOpr = "my Name is Amit Kumar Srivastava. i'm software engineer"
print(strOpr.endswith("ava"))
print(strOpr.capitalize())  # it is create new string despite change in existing one.
print(strOpr)
print(strOpr.replace("my", "I"))
print(strOpr)
print(strOpr.find("N"))
strOpr1 = " I am Am am"
print(" am count :: ", strOpr1.count("am"))
print(" Am count :: ", strOpr1.count("Am"))