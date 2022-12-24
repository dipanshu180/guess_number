# winning_num=23 #first we assingned a number
# guess=1 #then we put the value of guess so that we can give how many time we can  guess the number
# num=int(input("enter the number: "))
# game_over= False #we put the variable  game_over to make while loop work
# while not game_over: # the while loop will run until user not guess the number
#     if num==winning_num:
#         print(f"you Win, and guess the number in {guess} time ") 
#         game_over= True
#     else:
#         if num<winning_num:
#             print("too low")
#             guess+=1
#             num=int(input("enter number again:"))

#         else: 
#             print("too high")
#             guess+=1
#             num=int(input("enter number again:"))
            
            
            
#   <<<<<<< .........................................other way...............................................>>>>>>>>>>>
# winning_num=23 
# guess=1
# num=int(input("enter the number: "))
# game_over= False
# while not game_over: 
#     if num==winning_num:
#         print(f"you Win, and guess the number in {guess} time ") 
#         game_over= True
#     else:
#         if num<winning_num:
#             print("too low")
           
#         else: 
#             print("too high")
#         guess+=1
#         num=int(input("enter number again:"))




#   <<<<<<< .........................................other way...............................................>>>>>>>>>>>
winning_num=23 
guess=1

while True:
    num=int(input("enter the number: ")) 
    if num==winning_num:
        print(f"you Win, and guess the number in {guess} time ") 
        break
    else:
        if num<winning_num:
            print("too low")   
        else: 
            print("too high")
        guess+=1
        # num=int(input("enter number again:"))
        continue
         