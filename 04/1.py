a,*b=open('i').read().split('\n\n');a=a.split(',');b=[[c.split()for c in a.split('\n') if c]for a in b];c=lambda e,f:any(all(i in a[:f] for i in g)for g in e);m=lambda n,h:c(n,h)+c(zip(*n),h);d=lambda h=1:sum(int(k)for g in b if m(g,h)for l in g for k in l if k not in a[:h])*int(a[h-1])if any(m(z,h)for z in b)else d(h+1);print(d())