class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ## Set the basecase
        triangle = [[1]]

        ## Iterate and keep filling up the triangle
        for i in range(1, numRows):
            ## Intialize next_row as empty
            next_row = []
            ## We will be adding two elements at a time, hence len(prev_row) -1
            for j in range(len(triangle[i-1])-1):
                next_row.append(triangle[i-1][j] + triangle[i-1][j+1])
            ## We need to insert and append first two 1
            next_row.insert(0, 1)
            next_row.append(1)
            ## Add the next row to the triangle
            triangle.append(next_row)
                
        return triangle
