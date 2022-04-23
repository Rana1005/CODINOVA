def SeatAllocation(l1,l2,l3,i):
    output=[]

    if i==4:
        if sum(l1[2:6])==0:
            output=['1c','1d','1e','1f']
            l1[2]=l1[3]=l1[4]=l1[5]=1
            return output
        elif (sum(l1[0:2])+sum(l1[6:8]))==0:
            output=['1a','1b','1g','1h']
            l1[0]=li[1]=li[6]=li[7]=1
            return output

        elif sum(l2[2:6])==0:
            output=['2c','2d','2e','2f']
            l2[2]=l2[3]=l2[4]=l2[5]=1
            return output
        elif (sum(l2[0:2])+sum(l2[6:8]))==0:
            output=['2a','2b','2g','2h']
            l2[0]=l2[1]=l2[6]=l2[7]=1
            return output

        elif sum(l3[2:6])==0:
            output=['3c','3d','3e','3f']
            l3[2]=l3[3]=l3[4]=l3[5]=1
            return output
        elif (sum(l3[0:2])+sum(l3[6:8]))==0:
            output=['3a','3b','3g','3h']
            l3[0]=l3[1]=l3[6]=l3[7]=1
            return output
        

    elif i==3:
        if sum(l1[2:5])==0:
            output=['1c','1d','1e']
            l1[2]=l1[3]=l1[4]=1
            return output
        elif sum(l2[2:5])==0:
            output=['2c','2d','2e']
            l2[2]=l2[3]=l2[4]=1
            return output
        elif sum(l3[2:5])==0:
            output=['3c','3d','3e']
            l3[2]=l3[3]=l3[4]=1
            return output

    elif i==2:
        if sum(l1[0:2])==0:
            output=['1a','1b']
            l1[0]=l1[1]=1
            return output
        elif sum(l1[6:8])==0:
            output=['1g','1h']
            l1[6]=l1[7]=1
            return output

        if sum(l2[0:2])==0:
            output=['2a','2b']
            l2[0]=l2[1]=1
            return output

        elif sum(l2[6:8])==0:
            output=['2g','2h']
            l2[6]=l2[7]=1
            return output

        if sum(l3[0:2])==0:
            output=['3a','3b']
            l3[0]=l3[1]=1
            return output

        elif sum(l3[6:8])==0:
            output=['3g','3h']
            l3[6]=l3[7]=1
            return output
        
    else:
        dic={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h'}
        if sum(l1) < 8:
            zeroindex=l1.index(0)
            return ['1'+dic[zeroindex]]

        elif sum(l2) < 8:
            zeroindex=l2.index(0)
            return ['2'+dic[zeroindex]]

        elif sum(l3) < 8:
            zeroindex=l3.index(0)
            return ['3'+dic[zeroindex]]
 



l1=[0 for i in range(8)]
l2=[0 for i in range(8)]
l3=[0 for i in range(8)]

no_of_pass_input = [4,3,3,2,2,4,1]

for i in no_of_pass_input:
    li=SeatAllocation(l1,l2,l3,i)
    print(li)


