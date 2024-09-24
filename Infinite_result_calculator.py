print("="*10,"infinte result calculator","="*10)

number=[]
sub=int(input("How many Subjects :"))
print("="*50)
total=sub*100
for i in range(sub):
	print(i+1,end=' ')
	n=int(input("Sub :"))
	number.append(n)
obt=sum(number)

def division(x,y):
	d=x/y
	return d

def persent(x):
	d=x*100
	return d

div_res=division(obt,total)
persent=persent(div_res)

print("="*50)
print("list :",number)
print("Sum :",obt)

print("Persentage :",persent,"%")

if 100 >= persent >= 80 :
	print("A+")
elif persent >=70:
	print("A")
elif persent>=60:
	print("B")
elif persent >=50:
	print("C")
else:
	print("F")
