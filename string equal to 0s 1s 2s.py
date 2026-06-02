s= input()
n=len(s)
count=0
for i in range(n):
    zero=0
    one=0
    two=0
    for j in range(i,n):
        if s[j] == "0":
            zero += 1
        elif s[j] == "1":
            one += 1
        elif s[j] == "2":
            two += 1

        if zero == one and one == two:
            count += 1
print(count)


#090890
#090
#908
#089
