a=[];b=[];sum=[];msum=[]
print("enter the first array")
r=int(input("enter no of rows"))
c=int(input("no of coloumns"))
for i in range(r):
  print(f"enter the {i+1}st row elemts")
  b=[]
  for j in range(c):
    v=int(input("=>"))
    b.append(v)
  a.append(b)
print("enter the second array")
q=[];w=[]
for i in range(r):
  print(f"enter the {i+1}st row elemts")
  w=[]
  for j in range(c):
    v=int(input("=>"))
    w.append(v)
  q.append(w)
print(a)
print(q)
for i in range(len(a)):
  sum=[]
  for j in range(len(q)):
    c=a[i][j]+q[i][j]
    sum.append(c)
  msum.append(sum)
print(msum)


