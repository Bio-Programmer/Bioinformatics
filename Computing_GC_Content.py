#Sophia Longo
#Created: July 14, 2017, Compelted: July 15, 2017
#Title: Rosalind: Computing GC Content

def percentGC(aSeq): #calculates percent GC of a given sequence
    gcCount = 0
    seqLen = 0
    for i in range(0, len(aSeq)):
        if(aSeq[i] == "G" or aSeq[i] == "C"):
            gcCount += 1
        if(aSeq[i] != "\n"):
            seqLen += 1
    percent = (gcCount/seqLen) * 100
    return percent

def assemble(file): #assembles dictionary of seqName:percentGC from file
    fileGC = {}
    name = ""
    seq = ""
    with open(file) as f:
        for line in f:
            #extracts sequences while accounting for file formatting
            if(line[0] == ">"):
                if(seq != ""):
                    #sequence name a corresponding % GC content is added to a dictionary (of sequences with corresponding % GC)
                    fileGC[name] = percentGC(seq)
                    name = ""
                    seq = ""
                name = line.replace(">", "").replace("\n", "")
                seq = ""
            else:
                seq += line
    fileGC[name] = percentGC(seq) #ensures last section isn't left out of dictionary
    return fileGC
            
def findMax(gcDict): #finds sequence within file that has the most GC content
    maximum = max(gcDict, key = gcDict.get)
    return(str(maximum) + "\n" + str(gcDict[maximum]))

print(findMax(assemble("RosalindGC.txt")))
