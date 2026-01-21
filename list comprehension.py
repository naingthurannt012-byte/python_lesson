square =[x**2 for x in range(10)]
print(square)

for i in range(5):
    print('loop no =',i)

j = 0
while j < 5:
    print('Loop no =',j)
    j+=1

for row in range (3):
    for col in range(3):
        print('#')
    print() #new line(break line) after each row
for row in range (4):
    for col in range(8):
        print('*',end='') # to avoid new line after each column
    print() #new line(break line) after each row

for row in range(7):
 for col in range(10):
   if row==0 or row==6:
    print('*',end='')

   if row>0 and row<6:
     if col==0 or col==9:
       print('*',end='')
     else:
      print(' ',end='')
 
 print()

for row in range(10):
 for col in range(10):
   if row==0 or row ==4 or row==9:
    print('*',end='')

   if row>0 and row<4 or row>4 and row<9:
     if col==0 or col==9:
       print('*',end='')
     else:
      print(' ',end='')
 
 print()


 for row in range(10):
    for col in range(20):
      if row==0 or row ==4 or row==9:
       print('*',end='')

      if row>0 and row<4:
        if col==0 or col == 4 or col==19:
          print('*',end='')
      else:
       print(' ',end='')
      if row>4 and row<9:
        if col==0 or col==19:
         print('*',end='')
      else:
         print(' ',end='')
 
    print()