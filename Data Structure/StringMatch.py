def match(pat,txt):
    lastt=len(txt)-1
    lastp=len(pat)-1
    endmatch=lastp
    start=0 #txt的index

    while endmatch <=lastt:

        if txt[endmatch]==pat[lastp]:  #先比較最後一個字元，有中的話，再建立兩個指針從頭開始匹配其他字元是否有匹配
            j=0
            i=start
            while j<lastp and txt[i]==pat[j]: #從頭開始匹配
                i+=1  #i指針 用來指向txt的字元，因為是由左向右 所以是+=1
                j+=1  #j指針 用來指向pat的字元，因為是由左向右 所以是+=1

            if j==lastp:
                return start
            
        endmatch+=1 #逐步，往右邊推進
        start+=1    

    return -1 


if __name__ == '__main__' :
    txt="xyz78517851abcukabcfsecgr"
    pat="abc"

    index=match(pat,txt)  #只會回傳遞一個中的index
    print(index)


