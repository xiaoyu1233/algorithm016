class Solution:
    def rotatePassword(self, s1, s2):
        matrix_0 = s1
        matrix_1 = self.rotate(matrix_0)
        matrix_2 = self.rotate(matrix_1)
        matrix_3 = self.rotate(matrix_2)
        # print(matrix_0)
        # print(matrix_1)

        n = len(s1)

        res = ""
        for ss in [matrix_0,matrix_1,matrix_2,matrix_3]:
            #print(ss)
            s1 = ss
            for i in range(n):
                for j in range(n):
                    #print(i,j,s1[i][j])
                    if s1[i][j] == "0":
                        #print(i,j,s1[i][j])
                        res += s2[i][j]
        return res


    def rotate(self,matrix):
        n = len(matrix)
        matrix_rotate = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_rotate[j][n-i-1] = matrix[i][j]
        return matrix_rotate

# write code here

s1 = ["1101","1010","1111","1110"]
s2 = ["ABCD","EFGH","IJKL","MNPQ"]
a = Solution()
a.rotatePassword(s1,s2)