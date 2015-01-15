#python v2.7
import string
l=list(string.ascii_uppercase)
l.insert(0,'-')
str="YRIRY GJB CNFFJBEQ EBGGRA"
result=""
for x in str:
    if x==' ':
        result+=' '
    else:
        for y in range(0,26):
            if x==l[y]:
                if y<14:
                    i=y+13
                    result+=l[i]
                elif y>=14:
                    i=y-13
                    result+=l[i]
print result
