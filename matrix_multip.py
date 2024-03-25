A = [[5, 4, 3],  
     [2, 4, 6],  
     [4, 7, 9]]    
B = [[3, 2],  
     [4, 3],  
     [2, 7]]   

C = [[0, 0],
     [0, 0],    
     [0, 0]]  

for i in range(len(A)):    
   for j in range(len(B[0])):    
          for k in range(len(B)):    
               C[i][j] += A[i][k] * B[k][j]

for rows in C:    
   print(rows) 