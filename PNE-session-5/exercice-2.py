seq1 = input( "Please enter the first DNA sequence: " )
seq2 = input( "Please enter the second DNA sequence: " )


number_A1 = 0
number_T1 = 0
number_G1 = 0
number_C1 = 0

number_A2 = 0
number_T2 = 0
number_C2 = 0
number_G2 = 0


for i in range(len(seq1)):
   if seq1[i] == "A":
       number_A1 = number_A1 + 1
   if seq1[i] == "C":
       number_C1 = number_C1 + 1
   if seq1[i] == "T":
       number_T1 = number_T1 + 1
   if seq1[i] == "G":
       number_G1 = number_G1 + 1

for i in range(len(seq2)):
    if seq2[i] == "A":
        number_A2 = number_A2 + 1
    if seq2[i] == "C":
        number_C2 = number_C2 + 1
    if seq2[i] == "T":
        number_T2 = number_T2 + 1
    if seq2[i] == "G":
        number_G2 = number_G2 + 1

print("The total number of bases in the second sequence is: ", len(seq2))
print("")
print("The number of 'A' bases is:", number_A2)
print("The percentage of 'A' basis is:", number_A2 / len(seq2) * 100, "%")
print("")
print("The number of 'T' bases is:", number_T2)
print("The percentage of 'T' basis is:", number_T2 / len(seq2) * 100, "%")
print("")
print("The number of 'C' bases is:", number_C2)
print("The percentage of 'C' basis is:", number_C2 / len(seq2) * 100, "%")
print("")
print("The number of 'G' bases is:", number_G2)
print("The percentage of 'G' basis is:", number_G2 / len(seq2) * 100, "%")


print("The total number of bases in the first sequence is: ", len(seq1))
print("")
print("The number of 'A' bases is:", number_A1)
print("The percentage of 'A' basis is:", number_A1/len(seq1)*100, "%")
print("")
print("The number of 'T' bases is:", number_T1)
print("The percentage of 'T' basis is:", number_T1/len(seq1)*100, "%")
print("")
print("The number of 'C' bases is:", number_C1)
print("The percentage of 'C' basis is:", number_C1/len(seq1)*100, "%")
print("")
print("The number of 'G' bases is:", number_G1)
print("The percentage of 'G' basis is:", number_G1/len(seq1)*100, "%")