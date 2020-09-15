from Bio import SeqIO
for seq_record in SeqIO.parse("region_AA_output1.fasta", "fasta"):
    count1=seq_record.seq.count('G')
    count2 = seq_record.seq.count('C')
    count =count1 + count2
    length=len(seq_record)
    composition = (count/length)*100
    print(composition)
