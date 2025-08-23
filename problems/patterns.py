# --> Patterns printing

# #  1 2 3
# #  1 2 3
# #  1 2 3

# row=int(input("Enter number of rows: "))
# colum= int (input("Enter number of columns: "))

# for i in range(1,row+1):
#     for j in range(1,colum+1):
#         print(j, end = " ")
#     print()  # Move to the next line after each row

# -----> 2:-

#     0 1 2 3 4
# 0--># # # # # 
# 1--># # # # # 
# 2--># # # # #
# 3--># # # # #
# 4--># # # # #

# for i in range(5):    #  0 1 2 3 4
#     print (i, end="-->")      
#     for j in range(5):   # 0 1 2 3 4 
#         print("#", end=" ")
#     print()

# -----> 3:-

# j -->    0  1  2  3               
#  i     0 #  #  #  #
#        1 #  #  #
#        2 #  #
#        3 #

# for i in range(5):    #  0 1 2 3 4
#     print (i, end="-->")      
#     for j in range(5-i):      
#         print("#", end=" ")
#     print()


# -----> 4:-

#    0 1 2 3
#  0 #
#  1 # #
#  2 # # #
#  3 # # # #
# for i in range(5):    #  0 1 2 3 4
#     print (i, end="-->")      
#     for j in range(i+1):    
#         print("#", end=" ")
#     print()


