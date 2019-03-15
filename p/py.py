import re
import os

bp = open("bp.txt", "r")
bp = bp.readlines()

src = open("src.txt", "r")
src = src.read()


#bp = bp.rstrip()

#print(len(bp))
try:




	i = 0
	while i < len(bp):
	 x = re.split("Part ", bp[i])
	
	 x2 = re.findall("([A-Z])\W\s", x[1])
	
	 x3 = re.findall("[A-Z]\W\s([0-9]+)\s", x[1])
	
	 a = x2[0]
	
	 #print("Part " + x2[0])
	
	 if re.search("Part " + x2[0] ,src) or re.search("PART " + x2[0] ,src):
	  #print("Part "+ x2[0] +" find")
	
	  aray= {
	 "A": "B",
	 "B": "C",
	 "C": "D",
	 "D": "E",
	 "E": "F",
	 "F": "G",
	 "G": "H",
	 "H": "I",
	 "I": "J",
	 "J": "K",
	 "K": "L",
	 "L": "M",
	 "M": "N",
	 "N": "O",
	 "O": "P",
	 "P": "Q",
	 "Q": "R",
	 "R": "S",
	 "S": "T",
	 "T": "U",
	 "U": "V",
	 "W": "X",
	 "X": "Y",
	 "Y": "Z",
	 "Z": ""
	}
	
	
	
	  x5 = re.search("PART "+ x2[0] +"([\w\W]+)PART "+ aray[x2[0]], src)
	
	
	
	  #print(x5[0])
	  f = open("file"+x2[0]+".txt", "w+")
	
	  try:
	   f.write(x5[0])
	  except:
	   print("File "+x2[0]+" Open Error")
	
	
	  f = open("file"+x2[0]+".txt", "w+")
	  x6 = f.readlines()
	  #print("\nQuestions In This Part : ", (len(x6)-3), "\n")
	
	
	
	
	 else:
	  print(x2[0], "Not Found")
	 #print(x3)
	
	 i += 1
	
	












except:
 print("Error")




i = 0
while i < len(bp):
 x = re.split("Part ", bp[i])

 x2 = re.findall("([A-Z])\W\s", x[1])

 x3 = re.findall("[A-Z]\W\s([0-9]+)\s", x[1])
 print(x3[0])
	
 a = x2[0]
 print(x2[0])

