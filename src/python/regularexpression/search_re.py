import re
re.Match

script1 = "Hey everyone i am komal patel from Raipur. hello everyone"
# if there are more than one occurance then only first one will be returned
print(re.search("everyone",script1))
# with $ meta character
print(re.search("everyone$",script1))