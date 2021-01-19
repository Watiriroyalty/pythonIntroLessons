#This is a structure that can be used to store lists of information
friends= ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
print(friends[-1])
print(friends[1:])
print(friends[1:3])

friends[1]="Tiri"
print(friends[1])

#List Functions
lucky_number= [3,5,4,32,12,34,54]
#friends.extend(lucky_number)
#print(friends)

friends.append("Yonce")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

#print(friends.index("Oscar"))
friends.sort()
print(friends)

lucky_number.reverse()
print(lucky_number)

#print(friends.count("Jim"))

friends2 = friends.copy()
print(friends2)
