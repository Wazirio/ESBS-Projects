# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:17:24 2022

@author: Antoine LAMBERT
"""
"""
AIM : calculate some characteristics of a protein knowing its sequence and other stuff.
Nothing is really accurate, the most important is for the idea, a rough estimate.
The last part of the code refers to a practical concerning Protein Purification, starting with a specific sample. 
"""

name=(input("Give the Name : "))
seq=input("Give the sequence : ")
MW=input("Give the Molecular Weight (Da) : ")
count=0
dict={"C":0}
#summing up which AA we have in the prot, collected in dict
for i in range (len(seq)):
#    print(seq[i])
    if seq[i] not in dict:
        dict[seq[i]]=1
    else:
        dict[seq[i]]+=1
        
for j in dict:
    count=count+dict[j]
print("nb of AA " + str(count))

#tests
#print(dict["K"])
#print(dict["R"])
#print(dict["H"])

"""
Here, calculation of the E0.1%, the E1%, the extinction coefficient E280, at 280 nm.
The method has been tested on protein whose coefficients were known. Results were satisfying. 
"""
#need the number of C, Y, W.
#just to know
print("C = " + str( dict["C"]))
print("W="+str(dict["W"]))
print("Y="+str(dict["Y"]))

A01=(dict["W"]*5500+dict["Y"]*1490+dict["C"]*125)/int(MW)
print("E0.1% = "+str(A01))

A1=A01*10
print("E1% = "+str(A1))

e280=(dict["W"]*5500+dict["Y"]*1490+dict["C"]*125)
print("E280 = ",e280)

"""
Now, an approximation of the concentration, using the extinction coefficient at 280nm.
Need a measurement, of course.
"""

abs=input("Abs at 280 nm : ")
#Beer-Lambert law

C=float(abs)/e280
print("Concentration in tube : ",C," mol/L.")

"""
Calculation of the quantity, in g, in mol, in the sample.
"""

V=input("Vol in total (mL) of the sample : ")

V=float(V)*(10**(-3))
n=C*V
print("Number of mole in sample : ",n)

"""
Adapt the code from what you begun with.
"""

#starting Volume of Sample : 500µL.
#from a 2mg/mL sample = 1000µg = 1mg

mm={" ":0, "G":75.07, "H":155.15, "A": 89.09, "R":174.20, "N":132.12, "D":133.10, "E":147.13, "Q":146.14, "K":146.19, "M":149.21, "F":165.19, "P":115.13, "S":105.09, "T":119.12, "W":204.23, "Y":181.19, "V":117.15, "L":131.17, "I":131.17, "C":121.16}
tmm=0 #for Total Molar Mass
for m in dict:    
    tmm=tmm+dict[m]*mm[m]
#    print(dict[m],tmm,mm[m])
print("Total molar mass : ",tmm)

Ninitial=0.001/tmm
print("Initial number of moles : ",Ninitial)
yld=n/Ninitial
print("YIELD : ", yld)

    

    




















