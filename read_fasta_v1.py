def read_fasta(filename):
    sequence = ''
    f = open ('ae.fa')
    for line in f:
        line = line.strip()
        if not'>' in line:
            sequence = sequence + line
    f.close() 
    return sequence
print (read_fasta('ae.fa'))
