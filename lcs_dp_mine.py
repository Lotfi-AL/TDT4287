
def lcs(S,R):
    a = [[0]*(len(R)+1) for i in range(len(S)+1)]
    
    for row in range(1,len(S)+1):
        for col in range(1,len(R)+1): 
            a[row][col] = max(a[row-1][col], a[row][col-1], a[row-1][col-1]+f(S[row-1],R[col-1]))
    return a[len(S)][len(R)]

def lcs_with_backtrack(S,R):
    a = [[0]*(len(R)+1) for i in range(len(S)+1)]
    b = [[0]*(len(R)+1) for i in range(len(S)+1)]
    for row in range(1,len(S)+1):
        for col in range(1,len(R)+1): 
            a[row][col] = max(a[row-1][col], a[row][col-1], a[row-1][col-1]+f(S[row-1],R[col-1]))
            b[row][col] = calc_gain(a,row,col)
    return b

def calc_gain(a,i,j):
    if a[i][j] == a[i-1][j]:
        return 0
    elif a[i][j] == a[i][j-1]:
        return 1
    elif a[i][j] == a[i-1][j-1]+1:
        return 2
    
def print_lcs(S,R):
    b = lcs_with_backtrack(S,R)
    T = []
    ss= print_lcs_rec(b,S,len(S),len(R),T)
    return ss
    
def print_lcs_rec(b,S,i,j,T):
    if i == 0 or j == 0: 
        return ""
    if b[i][j] == 2:
        return print_lcs_rec(b,S,i-1,j-1,T)+ S[i-1]
        
    elif b[i][j] == 0:
        return print_lcs_rec(b,S,i-1,j,T)
    else:
        return print_lcs_rec(b,S,i,j-1,T)
    
def f(s,r):
    if s == r:
        return 1  
    else:
        return 0
    


if __name__ == "__main__":
    S = "AGCTTAGCTG"
    R = "TCGGATG"
    #print(lcs(S,R))