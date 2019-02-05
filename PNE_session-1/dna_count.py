seq = input( "Please enter a DNA sequence: " )

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
print("The number of 'A' bases is:", number_A)
print("The number of 'T' bases is:", number_T)
print("The number of 'C' bases is:", number_C)
print("The number of 'G' bases is:", number_G)