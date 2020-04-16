# ==============================================================
# PROGRAM FOR CALCULATE EDTA - TITRATION
# The program was written for HOBBY
#
# Coded By  : MUHAMMAD ISRO
# Email     : isro_xp[at]student.ub.ac.id
#
#
# Date : 4/16/2020
#
# =============================================================

K1 = 1.02e-2
K2 = 2.14e-3
K3 = 6.92e-7
K4 = 5.50e-11


out_name =  "{0:>1.5f} {1:>15.6e} {2:>15.6e} {4:>15.6e} {5:>15.6e} {6:>15.6e} \n"
f = open("result-edta.txt","w")
for pH in range (1,1400001):
    i = pH*0.00001
    D = ((10**-(i))**4+(K1*(10**-(i))**3)+(K1*K2*(10**-(i))**2)+(K1*K2*K3*10**-(i))+(K1*K2*K3*K4))
    
    a0  = ((10**-(i))**4)/D
    a1  = (K1*(10**-(i))**3)/D
    a2  = (K1*K2*(10**-(i))**2)/D
    a3  = (K1*K2*K3*10**-(i))/D
    a4  = (K1*K2*K3*K4)/D
    print out_name.format(i,D,a0,a1,a2,a3,a4)
    f.write(out_name.format(i,D,a0,a1,a2,a3,a4))
    print i
    
f.close()
