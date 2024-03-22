import re

txt = "Power of thousand sun"

# findall() function is case sensitive
a1 = re.findall("power",txt)
print(a1)
a2 = re.findall("Power",txt)
print(a2)

# findall() find pattern in a linear fashion
text = "awawawawawawawawk"
a3 = re.findall("awaw",text)
print(a3)

"""Using meta characters"""

script1 = "I watch anime. I have watched Demon Slayer, JJk Spy Family etc ... . anime is fun"
a4 = re.findall("^I",script1)
print(a4)

script2 = "ommmmm ommmmmm ommmmmm oppppppp"
# * checks for 0 or more occurance
a5 = re.findall("om*",script2)
print(a5)

# + checks for 1 or more occurance
a6 = re.findall("om+",script2)
print(a6)

# ? checks for 0 or 1 occurance
a7 = re.findall("om?",script2)
print(a7)

# . hold a singe character 
script3 = "a a2 a3 a4 a5 a6"
a8 = re.findall("a.",script3)
print(a8)

# $ matches the end of string
script4 = "komal14march2002@gmail.com"
a9 = re.findall("@gmail.com",script4)
print(a9)

script5 = "komal@gmail.com nitin@gmail.com sorav@gmail.com"
a10 = re.findall("@gmail.com$",script5)
print(a10)

script6 = "i am a coder"
a11 = re.findall("..",script6)
print(a11)

