#open txt file in read mode
f=open("file.txt","r")

#initialize list as below
Books=[]
MissBook=[]
RepeatBook=[]
#all Books numbers are append in Books list
for x in f:
   # print(x)
    Books.append(int(x))
#range upto last Book Number
for b in range(1,22302):
    if b not in Books:
        MissBook.append(b)
#for Repeated book number up to last book number
for c in range(1,22302):
    if Books.count(c) > 1:
        RepeatBook.append(c)

print("Missing Books:",MissBook)
print()
print("Available Books:",Books)
print()
print("Books Repeated:",RepeatBook)
print()
print("Total Missing Books:",len(MissBook))
print("Total Available Books:",len(Books))
print("Total Books Repeated:",len(RepeatBook))
