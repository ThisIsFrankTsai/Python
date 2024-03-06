#字串比對，如果有中，則回傳index，否則回傳0

txt =  "AABAACAADAABAABA"
pat =  "AABA"
k=0
l=[]
for i in range(len(txt)-1):
    j=0
    k=i
    while j<=len(pat)-1 and txt[i]==pat[j] :

        if i-k==len(pat)-1:
            l.append(k)
        i+=1
        j+=1
    
print(l)

