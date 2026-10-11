Question1 = '''  University Student Skills
Three departments maintain sets of student skills:
CSE = {"Python", "Java", "SQL", "AI", "Cloud"}
ECE = {"Python", "Embedded", "IoT", "AI"}
ME = {"Python", "CAD", "Robotics", "IoT"}
Write a program to:
•	Find skills common to all departments. 
•	Find skills unique to CSE. 
•	Find skills used by CSE or ECE but not both. 
•	Find the complete set of skills. 
•	Identify skills shared by exactly two departments '''


CSE = {"Python", "Java", "SQL", "AI", "Cloud"}
ECE = {"Python", "Embedded", "IoT", "AI"}
ME = {"Python", "CAD", "Robotics", "IoT"}
a = CSE.intersection(ECE,ME)
print(a)

b =CSE-ECE-ME
print(b)

c = CSE^ECE
print(c)

d = CSE.union(ECE,ME)
print(d)

e = CSE.intersection(ECE) - ME
print(e)