def enc(stru):
    b = len(stru) 
    if len(stru) <= 10:
      print(stru)
    else:
      print(stru[0] + str(b-2) + stru[b-1])
    

n = int(input()) 
for i in range(n):
     stru = input("enter a word")
     enc(stru)
    