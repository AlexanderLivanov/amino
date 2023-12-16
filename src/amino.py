amino = """
gtqgkvikck aaiawktgsp lcieeievsp pkacevriqv iatcvchtdi natdpkkkal
fpvvlgheca givesvgpgv tnfkpgdkvi pffapqckrc klclspltnl cgklrnfkyp
tidqelmedr tsrftckgrs iyhfmgvssf sqytvvsean larvddeanl ervcligcgf
ssgygaaint akvtpgstca vfglgcvgls aiigckiaga sriiaiding ekfpkakalg
atdclnprel dkpvqdvite ltaggvdysl dcagtaqtlk aavdctvlgw gsctvvgakv
demtiptvdv ilgrsingtf fggwksvdsv pnlvsdyknk kfdldllvth alpfesinda
idlmkegksi rtiltf
"""
res = 1
for i in amino:
    if(i == 'a'): res *= 4  
    if(i == 'r'): res *= 6 
    if(i == 'n'): res *= 2 
    if(i == 'd'): res *= 2 
    if(i == 'c'): res *= 2 
    if(i == 'q'): res *= 2  
    if(i == 'e'): res *= 2 
    if(i == 'g'): res *= 4 
    if(i == 'h'): res *= 2 
    if(i == 'i'): res *= 3 
    if(i == 'l'): res *= 6  
    if(i == 'k'): res *= 2 
    if(i == 'm'): res *= 1 
    if(i == 'f'): res *= 2 
    if(i == 'p'): res *= 4 
    if(i == 's'): res *= 6  
    if(i == 't'): res *= 4 
    if(i == 'w'): res *= 4  
    if(i == 'y'): res *= 2 
    if(i == 'v'): res *= 4 

print(res)
