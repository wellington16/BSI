


if ay1 < by1 and by2 < ay1:


if ax1 >=bx1 and bx2 > ax1:
    print("0")
with open("E1.in","r")as fin:
    retaA= fin .readline()
    retaA =retA.split()
    retaB = fin readline()
    retB=  retB.split()
    ax1 = float(retA[0])
    by1 = float(retB[1])
    ax2 = float(reM
                
    |y2
    |

if ax1<=bx1:
    if ax2 > bx1:
        if ay1 <= by1:
            colide="1"
            else:
                colide="0"
            else:
                if ay1 <= by2:
                    colide ="1"
                    else:
                        colide="0"
        else:
            colide ="0"
else:
    if  ax1 <= bx2 :
        if ay1<=by1:
            if ay2 >by1:
                colide= "1"
            else:
                colide ="0"
        else:
            colide ="0"
            
with open("E2.out","w") as fout:
    fout.write(colide +"\n")
    
