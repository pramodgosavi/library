f=open("LibraryBooksDATA.txt","r")
Books=[]
MissBook=[]
RepeatBook=[]
for x in f:
   # print(x)
    Books.append(int(x))

for b in range(1,22302):
    if b not in Books:
        MissBook.append(b)

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
