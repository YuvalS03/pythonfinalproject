import re

data = open("email.txt","r")
text = data.read()

outputText = re.sub("someone", "Kora", text)


outputFile = open("emailREDACTED.txt", "w")
outputFile.write(outputText)
outputFile.close()