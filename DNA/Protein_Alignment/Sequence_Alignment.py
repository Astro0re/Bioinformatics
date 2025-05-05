# Source(ME) Check out https://github.com/Astro0re/Biological-Codes/blob/master/Sequence%20Alignment.py
def s_a(seq1,seq2):
    print("Running analysis...")
    same=[]
    for i in seq1:
        for j in seq2:
            if i == j:
                same.append(i)
    same_per = (len(same)*2)/(len(seq1)+len(seq2)) * 100
    print( "The percentage of similarity is", same_per)
    if same_per >= 40:
        print( "Sequences are Homologous")
    elif  20 <= same_per < 40:
        print( "Sequences are in the Twilight Zone of Homology")
    elif same_per < 20:
        print( "Sequences are in the Midnight Zone of Homology")




def relational(seq1,seq2):
    print("Running analysis...")
    if len(seq1) == len(seq2):
        print("Sequence is relational")
    elif len(seq1) - len(seq2) >= 20 or -20 :
        print("Sequence is not relational")

x = ['a','d','f','e','p','w','r']
y = ['a','d','f','e','b','w','r']

s_a(x,y)

relational(x,y)

# Multiple Sequences
def ms_a(seq1,seq2,seq3,seq4):
    print("Running analysis...")
    s_seq1 = set(seq1)
    s_seq2 = set(seq2)
    s_seq3 = set(seq3)
    s_seq4 = set(seq4)
    same=[]
    for i in seq1:
        for j in seq2:
            for k in seq3:
                for l in seq4:
                    if i == j and i == k and i == l :
                        same.append(i)
    same_per = (len(same)*len(ms_a))/(len(seq1)+len(seq2)+len(seq3)+len(seq4)) * 100
    print( "The percentage of similarity is", same_per)
    if same_per >= 40:
        print( "Sequences are Homologous")
    elif  20 <= same_per < 40:
        print( "Sequences are in the Twilight Zone of Homology")
    elif same_per < 20:
        print( "Sequences are in the Midnight Zone of Homology")

d = ['a','d','f','e','p','a','h']
s = ['a','d','n','e','b','m','r']
z = ['y','s','f','e','p','n','r']
k = ['a','d','f','e','b','w','r']

ms_a(d,s,z,k)

def Sequence_Analysis(seq1,seq2):
    s_a(seq1,seq2)
    relational(seq1,seq2)

# Run Code of FASTA files
FAS_1=['A','T','G','G','C','T','A','C','A','G','T','C','A','G','C','A','C','A','C','A','G','C','G','G','T','C','G','T','A']
FAS_2=['A','T','G','G','C','C','A','A','G','A','T','C','A','A','C','A','C','C','C','A','A','T','A','C','T','C','C','C','A']

s_a(FAS_1,FAS_2)
relational(FAS_1,FAS_2)