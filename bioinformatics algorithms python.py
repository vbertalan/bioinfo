# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


# Reproduce the PatternCount function on the following line from Replication.py.
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1    
    return array

# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {} #initializing the dictionary
    skew[0] = 0
    n = len(Genome)
    for i in range(1,n+1):
        if Genome[i-1]=="G":
            skew[i] = skew[i-1]+1
        elif Genome[i-1]=="C":
            skew[i] = skew[i-1]-1
        else:
            skew[i] = skew[i-1]
    return skew

# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    array = Skew(Genome)
    min_value = min(array.values())
    positions = [key for key, value in array.items() if value == min_value]
    return positions

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
       if p[i] != q[i]:
         count+=1
    return count

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    tamanho = len(Pattern)
    distancia = 0
    for i in range(len(Text)-tamanho+1):
      distancia = HammingDistance(Pattern,Text[i:i+tamanho])
      if(distancia<=d):
        positions.append(i)
    return positions

# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    tamanho = len(Pattern)
    distancia = 0
    for i in range(len(Text)-tamanho+1):
      distancia = HammingDistance(Pattern,Text[i:i+tamanho])
      if(distancia<=d):
        count+=1
    return count
