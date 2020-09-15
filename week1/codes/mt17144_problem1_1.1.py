from Bio import SeqIO
index=1
new_fasta=[]
for record in SeqIO.parse('H:/Mtech stuff/sem1/acb/asignments/one/assignment-1_12880/final/mtb.gb', 'genbank'):
    if record.features:
        for feature in record.features:
            if feature.type == "CDS":
                new_fasta.append('>1c1|%s_gene_%s' % (record.id, index))
                index+=1
                if 'gene' in feature.qualifiers:
                    q=str(feature.qualifiers["gene"])
                    new_fasta.append(' [gene=%s]' % q[2:-2])
                if 'locus_tag' in feature.qualifiers:
                    q=str(feature.qualifiers["locus_tag"])
                    new_fasta.append(' [locus_tag=%s]' % q[2:-2])
                new_fasta.append(" [location="+str(feature.location.start) + ".." + str(feature.location.end)+"]\n")
                q=str(feature.location.extract(record).seq)
                print(q)
                new_fasta.append(q+'\n')

with open('region_AA_output1.fasta', 'w') as f:
    f.write(''.join(new_fasta))