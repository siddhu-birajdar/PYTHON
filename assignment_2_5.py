#write a python program that calculas the electricty bill  based on the number  of units used.
#up to 100 units=5 Rs per unit.
#101 to 300 units =7 Rs per unit.
#Above 300 units =10 Rs per unit.

#Siddheshwar birajdar 
#F.Y.B Tech CSE (DS)
#Roll No= 123

units=int (input('Enter the number of units used ;'))

if units <=100:
    Bill= units*5 #First 100 units RS 5 per unit 
elif units >100 and units <=300:
    Bill =(100 *5)+((units - 100 )*7)
else:
    Bill=(100 *5)+(200 *7) +((units -300)*10)

print('you have used',units,'unit and your electricty bill is',Bill)

