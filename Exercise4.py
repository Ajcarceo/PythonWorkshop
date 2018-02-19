file_text = open("DNA.txt").read()
x=len(file_text)
C=0
G=0

for i in range (0,x):
    if file_text[i] == 'C':
        C = C+1
    else:
        C= C+0
        
    if file_text[i] == 'G':
        G = G+1
    else:
        G = G+0
    y = C + G

    
print "There are", C, "C"
print "There are", G, "G"
print "C+G is", y
print "Th

print "The percentage of C+G over the total is", (100.0*y)/x

