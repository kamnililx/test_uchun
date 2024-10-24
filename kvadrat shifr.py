print("Polibius kvadratini yaratish")
M=[["a","b","c","d","e"],["f","g","h","i","k"],["l","m","n","o","p"],["q","r","s","t","u"],["v","w","x","y","z"]]
A=input("Matn kiriting: ")
a=A.lower()
T=[]
for i in a:
    if i=="j":
     T.append(14)
    elif i.isalpha():
        for j in range(5):
            for k in range(5):
                if M[j][k]==i:
                    T.append(int(str(j+1)+str(k+1)))
    elif not i.isalpha():
      T.append(i)
n=len(T)
s1=""
s2=""
for i in range(n):
    if i%2==0:
        s1=s1+T[i]
    else:
        s2=s2+T[i]
s=s1+s2
s1=""

for i in range(0,n,2):
    s1=s1+M[int(s[i])-1][int(s[i+1])-1]
print(s1)
