from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, strlist=[[]]):
        templist = []
        for line in strlist:
            temp = []
            for i in line:
                temp.append(i)
            templist.append(temp)
        self.strlist = templist
        self.lines = len(strlist)
        self.columns = len(strlist[0])

    def size(self):
        return self.lines, self.columns

    def __str__(self):
        k = 0
        temp = ''
        for line in self.strlist:
            k += 1
            j = 0
            for i in line:
                temp += str(i)
                j += 1
                if j < self.columns:
                    temp += '\t'
            if k < self.lines:
                temp += '\n'
        return temp

    def __add__(self, other):
        if isinstance(other, Matrix) and \
                (self.columns, self.lines) == (other.columns, other.lines):
            return Matrix([[self.strlist[i][j] + other.strlist[i][j]
                            for j in range(self.columns)]
                           for i in range(self.lines)])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[other*self.strlist[j][i]
                            for j in range(self.columns)]
                           for i in range(self.lines)])
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def transpose(self):
        self.strlist = [[self.strlist[i][j]
                         for i in range(self.lines)]
                        for j in range(self.columns)]
        self.lines, self.columns = self.columns, self.lines
        return self

    def transposed(m):
        M = Matrix(m.strlist)
        M.strlist = [[M.strlist[i][j]
                      for i in range(M.lines)]
                     for j in range(M.columns)]
        M.lines, M.columns = M.columns, M.lines
        return M


exec(stdin.read())
