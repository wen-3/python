import scipy as sp
B = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# 奇異値分解的函式linalg.svd
U, s, Vs = sp.linalg.svd(B)
m, n = B.shape
S = sp.linalg.diagsvd(s,m,n)
print('U:\n',U,'\n')
print('s:\n',s,'\n')
print('Vs:\n',Vs,'\n')
print('m:',m,'\n')
print('n:',n,'\n')
print('S:\n',S,'\n')
print('U.S.V* = \n',U@S@Vs)
