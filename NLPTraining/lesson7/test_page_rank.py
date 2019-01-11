

S=[[0,0,0,0],[0.3333,0,0,1],[0.3333,0.5,0,0],[0.3333,0.5,1,0]] #原始矩阵

U=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]  #全部都为1的矩阵

f=[1,1,1,1]  #物征向量

alpha=0.85  # a 值 0-1之间的小数

n=len(S) #网页数

def multiGeneMatrix(gene,Matrix):
    mullist = [[0]*len(Matrix) for row in range(len(Matrix))] #定义新的矩阵大小，初始化为0
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix)):
            mullist[i][j] += Matrix[i][j]*gene

    return  mullist

def addMatrix(matrix1,matrix2):
    if len(matrix1) != len(matrix2):
        print('please input the same length matrix')
        return None
    addlist = [[0]*len(matrix1) for row in range(len(matrix1))]
    for i in range(0,len(matrix1)):
        for j in range(0,len(matrix2)):
            addlist[i][j] = matrix1[i][j] +matrix2[i][j]
    return addlist

def multiMatrixVector(m,v):
    rv = [0 for _ in range(len(v))]
    for row in range(0,len(m)):
        temp = 0
        for col in range(0,len(m[1])):
            temp += m[row][col]*v[col]
            rv[row] = temp
    return rv

f1 = multiGeneMatrix(alpha,S)
f2 = multiGeneMatrix((1-alpha)/len(S[0]),U)
G = addMatrix(f1,f2)
# print(G)

count = 0
while(True):
    count = count + 1
    pr_next = multiMatrixVector(G,f)
    print('第{}轮迭代'.format(count))
    print(str(round(pr_next[0], 5)) + "\t" + str(round(pr_next[1], 5)) + "\t" + str(round(pr_next[2], 5)) + "\t" + str(
        round(pr_next[3], 5)))
    if round(f[0],5) == round(pr_next[0],5) and  round(f[1],5)==round(pr_next[1],5) and round(f[2], 5) == round(pr_next[2], 5) and round(f[3], 5) == round(pr_next[3], 5):
        break
    f = pr_next
    print('page rank 值以计算完成')





















