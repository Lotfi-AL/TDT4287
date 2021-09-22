def lcs(X, Y):
    m = len(X)
    n = len(Y)
    

    L = [[0] * (n+1) for i in range(m+1)]
    b = [[0] * (n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):        
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

            if L[i][j] == L[i-1][j]:
                b[i][j] = 0
            elif L[i][j] == L[i][j-1]:
                b[i][j] = 1
            elif L[i][j] == L[i-1][j-1] +1:
                b[i][j] = 2
                
    for i in range(m+1):
        for j in range(n+1):
            print_lcs(b,X,i,j)
        
    return (L[m][n],b)

def print_lcs(b,S,i,j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 2:
        print_lcs(b,S,i-1,j-1)
        print(S[i])
    elif b[i][j] == 0:
        print_lcs(b,S,i-1,j)
    else:
        print_lcs(b,S,i,j-1)
def f(r,s):
    if r==s:
        return 1
    else:
        return 0
    
X = "AGGTAB"
Y = "GXTXAYB"

L,b = lcs(X,Y)

print(L)
print(b)
