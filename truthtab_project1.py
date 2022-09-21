
##A=0x00
##B=0x00
##S= 0x00
##R= 0x00
##P=0x00
##Q=0x00
#Y = ((A & B1)((S & R) | (P1 & Q)))
# y = ((Q& R1)&(S& T1)) | (P1 & F))
for i in range(0, 64):
    #print("the hex numbers are " +hex(i))
    P=i &(0x20)
    Q=i & (0x10)
    R=i & (0x08)
    S=i & (0x04)
    T=i & (0x02)
    F=i & (0x01)
    P1= i ^ (0x20)
    R1= i^ (0x08)
    T1= i^ (0x02)
   # print(bin(B))
   # print(bin(B1))
   # print(bin(P1))
    if(i & (0x20) == 32):
        P= 0b1
    else: P =0b0
    if(i & (0x10) ==16):
        Q =0b1
    else: Q=0b0
    if(i & (0x08) == 8):
        R = 0b1
    else: R=0b0
    if(i & (0x04) == 4):
        S= 0b1
    else: S =0b0
    if(i & (0x02) ==2):
        T = 0b1
    else: T=0b0
    if(i & (0x01) == 1):
        F =0b1
    else: F=0b0
    if(P1 & (0x20) ==32):
        P1 = 0b1
    else: P1=0b0
    if(R1 & (0x08) == 8):
        R1 = 0b1
    else: R1=0b0
    if(T1 & (0x02) == 2):
        T1 = 0b1
    else: T1=0b0
##    h = (S & R)
##    I = (A & B1)
##    print((h  | I)&(A & B1))
    print("printing positions ", +i,((Q& R1)&(S& T1)) | (P1 & F))
    
    
    
    


        
    
