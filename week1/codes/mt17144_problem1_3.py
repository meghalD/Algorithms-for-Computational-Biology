from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna,IUPAC
import csv
index=1
new_fasta=[]
for record in SeqIO.parse('H:/Mtech stuff/sem1/acb/asignments/one/assignment-1_12880/final/mtb.gb', 'genbank'):
    if record.features:
        for feature in record.features:
            if feature.type == "CDS":
                protein_id=str(feature.qualifiers["protein_id"])
                new_fasta.append('>1c1|%s_prot_%s_%s' % (record.id,protein_id[2:-2], index))
                index+=1
                if 'gene' in feature.qualifiers:
                    q=str(feature.qualifiers["gene"])
                    new_fasta.append(' [gene=%s]' % q[2:-2])
                if 'product' in feature.qualifiers:
                    q=str(feature.qualifiers["product"])
                    new_fasta.append(' [protein=%s]' % q[2:-2])
                if 'protein_id' in feature.qualifiers:
                    new_fasta.append(' [protein_id=%s]' % protein_id[2:-2])
                new_fasta.append(" [location="+str(feature.location.start) + ".." + str(feature.location.end)+"]\n")

                #transcription occur here:
                dna=str(feature.location.extract(record).seq)
                coding_dna=Seq(dna)
                m_rna = str(coding_dna.transcribe())

                #reading codon file
                #new_fasta.append(m_rna+'\n')
                for i in range(0,len(m_rna)-3,3):
                    cod=str(m_rna[i]+m_rna[i+1]+m_rna[i+2])
                    #i+=3
                    with open("codon_table.tsv") as codon_file:
                        tsvreader = csv.reader(codon_file, delimiter="\t")
                        for line in tsvreader:
                            if line[0] == cod:
                                new_fasta.append(line[1])
                                print(line[1])
                new_fasta.append("\n")
with open('protein_output3.fasta', 'w') as f:
    f.write(''.join(new_fasta))