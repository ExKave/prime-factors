
print(1)
n=int(input("Enter the number upto which primefactors to be calculated:"))
for i in range(2,n):
	p=True
	for j in range(2,i):
		if i%j==0:
			p=False
			k=j
		    #print("this is",i)
			break
	
	if p:
		print(i," (prime)")
		
	else:	
		print(i, k,end="")
		f=i//k
		
		m=2
		while m<=f:
			if f%m==0:
				print("x",m,end="")
				f=f//m
				m=2
			else:
				m+=1
		print()
