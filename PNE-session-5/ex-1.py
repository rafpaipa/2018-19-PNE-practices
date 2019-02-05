seq = 'ACGATGCATGCTTTCAGCTAGCAT'


number_A = 0
number_T = 0
number_G = 0
number_C = 0


for i in range(len(seq)):
   if seq[i] == "A":
       number_A = number_A + 1
   if seq[i] == "C":
       number_C = number_C + 1
   if seq[i] == "T":
       number_T = number_T + 1
   if seq[i] == "G":
       number_G = number_G + 1

print("The total number of bases is: ", len(seq))
print("")
print("The number of 'A' bases is:", number_A)
print("The percentage of 'A' basis is:", number_A/len(seq)*100, "%")
print("")
print("The number of 'T' bases is:", number_T)
print("The percentage of 'T' basis is:", number_T/len(seq)*100, "%")
print("")
print("The number of 'C' bases is:", number_C)
print("The percentage of 'C' basis is:", number_C/len(seq)*100, "%")
print("")
print("The number of 'G' bases is:", number_G)
print("The percentage of 'G' basis is:", number_G/len(seq)*100, "%")
