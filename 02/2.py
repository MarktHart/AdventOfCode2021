b=c=d=0;exec(';'.join(f"{['c+','c-',f'b+=c*{e};d+'][ord(a)&3]}={e}"for a,*_,e,_ in open('i')));print(d*b)