# for L in[*open(0)][1:]:print(bin(sum(map(lambda v:int(v,2),L.split())))[2:]) would be too fast and boring
for c in[0]*int(input()):
 A,B=input()[::-1].split();O=''
 while A+B:a,A=int(A[:1]or 0),A[1:];b,B=int(B[:1]or 0),B[1:];r,c=(a^b^c,a&b|a&c|b&c);O=str(r)+O
 print(c*'1'+O)

