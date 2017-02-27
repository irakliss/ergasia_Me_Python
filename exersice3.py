x=input("Provide list...")
y=x.split()
length_y=len(y)
output=list()

for i in range(length_y):
	if y[i]!='0':
		output.append(y[i])
		
length_o=len(output)

diff=length_y-length_o

if diff>0 :
	for i in range(diff):
		output.append('0')

print(output)