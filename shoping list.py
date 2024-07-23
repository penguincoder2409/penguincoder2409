s_list=[ ]
answer = ""
while answer != "end":
    answer = input("Enter what you want to add to your shoping list,or enter <end> to stop adding items\n")
    if answer != "end":
        s_list.append(answer)
    
for s in s_list:
    print(s)
 









