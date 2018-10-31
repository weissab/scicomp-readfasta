import sys

def read_fasta(filename):
    sequence = ''
    f = open ('ae.fa')
    for line in f:
        line = line.strip()
        if not'>' in line:
            sequence = sequence + line
    f.close() 
    return sequence
print (read_fasta('sys.argv[1]'))
#  python read_fasta_v2.py
# sys.arg
#  ['read_fasta_v2.py', 'ae.fa']
