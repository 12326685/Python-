import re                                                   #returns empty list if no match found                                                  
str="Example of Metacharacters in Regular Expressions"      #[] is a meta character here
x=re.findall("[ar]",str)                                    #check occurences of i and n individually
print(x) 

x=re.findall("^Exam",str)                                    #^ is a meta character
print(x)                                                     #weather source string starts with

x=re.findall("ssions$",str)                                 #$ is a meta character.....returns empty list if no match found
print(x)                                                    #weather source string ends with

x=re.findall("...ss...",str)                                #... is a meta character.....returns empty list if no match found
print(x)                                                    #every character except newline

x=re.findall("ss*",str)                                      #* is a meta character
print(x)                                                    #check for zero or no occurances

x=re.findall("s*",str)                                     
print(x)  


x=re.findall("es*",str)                                     
print(x) 

x=re.findall("er+",str)                                     #prints at one or more occurences                                   
print(x) 
