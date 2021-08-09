def print_rangoli(size):
    n = size
    abc=list(map(chr,range(97,123)))
    
    mid = abc[n -1 :: -1] + abc[1 : n ]

    m = len("-".join(mid))

    for i in range(1,n):
        print("-".join(abc[n-1:n-i:-1]+abc[n-i:n]).center(m,"-"))
    for i in range(n,0,-1):
        
        print("-".join(abc[n-1:n-i:-1]+abc[n-i:n]).center(m,"-"))
    

print_rangoli(5)