
# Defining the gene
gene = "TCAGACTGGTGCCGTGGTGCTCTCGCCCGATGTGACGTCGACCGCCAGCGGCGCGATGACGCCGAGGATTTCCGTGATCGTTTCGGAGGGCACGCCGGCTGCGGTCAGCGCGTCGGCCAAGTGTCCGGCGACCAGGCTGAAGTGGTGCATGGTAATTCCGCGCCCCTGATGGACTTGCTTCATCGGCGCACCGGTATAGGGCTCGGGCCCGCCAAGCGCGGCCGCGAAAAACTCCACCTGCTTGCCCTTGAGGCGGCTCATGTTCGTACCGCTGAAGAAGGCCGATAGTTGGTCATCGGCAAGCACACGAACATAGAAGTCCTCGACGACGACTTCGATGGCCTCATGCCCGCCGATCTTGTCGTAGATGCTGATCGGCTCACGTTTGCGCAAGCGTGACAGTAGTCCCATTTTTATA"
# Finding the complement of the gene
def complement(seq):
  intab = "ATCG"
  outtab = "TAGC"
  transtab = seq.maketrans(intab, outtab)
  comp_seq = seq.translate(transtab)
  return "Complement: " + comp_seq + "\n"
# Finding the reverse of the gene
def reverse(seq):
  comp_seq = seq[::-1]
  return "Reverse: " + comp_seq + "\n"
# Finding the reverse compliment of the gene
def reverse_complement(seq):
  intab = "ATCG"
  outtab = "TAGC"
  transtab = seq.maketrans(intab, outtab)
  comp_seq = seq.translate(transtab)
  return "Reverse Complement: " + comp_seq[::-1] + "\n"
# Wrapping all of the functions in one function
def init(seq):
  print("Gene: " + gene + "\n")
  print(complement(seq))
  print(reverse(seq))
  print(reverse_complement(seq))
# Finally, print the results
init(gene)