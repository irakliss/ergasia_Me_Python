x=input("Provide string...")

y=list(x)

r=set('!')

y1=[None] * len(x)

for i in range(len(x)):
    if y[i] == '!':
        if set(x[i+1:])<=r:
            y1[i]=y[i]
        else:
            y1[i]=''
    else:
        y1[i] = y[i]

print(''.join(y1))
