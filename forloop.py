#allows one to loop over stuff

friends=["Jim", "Karen", "Yoyo"]

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")
#for friend in friends:
 #   print(friend)

#for index in range(len(friends)):
 #   print(friends[index])
   # print(index)



def raise_to_power(base_num, pow_num):
     result = 1
     for index in range(pow_num):
         result= result*base_num
     return result
print(raise_to_power(2,2))