def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
 
    lps = [0]*M
    j = 0 #pat的指針
    i = 0 #txt的指針
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
 
      # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
 
def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
    lps[0] = 0  # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    KMPSearch(pat, txt)




def computeLPSArray(pat, M, lps):
    i=1
    len=0
    lps[0]=0

    while i<M:
        if pat[len]==pat[i]:
            len+=1
            lps[i]=len
            i+=1
        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1

def KMPSearch(pat, txt):
    M=len(pat)
    N=len(txt)

    lps = [0]*M
    j = 0  
    i = 0  
    computeLPSArray(pat,M,lps)

    while (N - i) >= (M - j):
        if pat[j]==txt[i]:
            i+=1
            j+=1
        
        if j==M:
            print("Found the pattern:",i-j)
            j = lps[j-1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
            










