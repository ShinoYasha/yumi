import pandas as pd
import csv
import random
import numpy as np
import datetime

class HMM(object):
    def __init__(self,N,M):
        self.A = np.zeros((N,N))        # 状态转移概率矩阵
        self.B = np.zeros((N,M))        # 观测概率矩阵
        self.Pi = np.array([1.0/N]*N)   # 初始状态概率矩阵

        self.N = N                      # 可能的状态数
        self.M = M                      # 可能的观测数

    def cal_probality(self, O):
        self.T = len(O)
        self.O = O

        self.forward()
        return sum(self.alpha[self.T-1])

    def forward(self):
        """
        前向算法
        """
        self.alpha = np.zeros((self.T,self.N))

        # 公式 10.15
        for i in range(self.N):
            self.alpha[0][i] = self.Pi[i]*self.B[i][self.O[0]]

        # 公式10.16
        for t in range(1,self.T):
            for i in range(self.N):
                sum = 0
                for j in range(self.N):
                    sum += self.alpha[t-1][j]*self.A[j][i]
                self.alpha[t][i] = sum * self.B[i][self.O[t]]

    def backward(self):
        """
        后向算法
        """
        self.beta = np.zeros((self.T,self.N))

        # 公式10.19
        for i in range(self.N):
            self.beta[self.T-1][i] = 1

        # 公式10.20
        for t in range(self.T-2,-1,-1):
            for i in range(self.N):
                for j in range(self.N):
                    self.beta[t][i] += self.A[i][j]*self.B[j][self.O[t+1]]*self.beta[t+1][j]

    def cal_gamma(self, i, t):
        """
        公式 10.24
        """
        numerator = self.alpha[t][i]*self.beta[t][i]
        denominator = 0

        for j in range(self.N):
            denominator += self.alpha[t][j]*self.beta[t][j]

        return numerator/denominator

    def cal_ksi(self, i, j, t):
        """
        公式 10.26
        """

        numerator = self.alpha[t][i]*self.A[i][j]*self.B[j][self.O[t+1]]*self.beta[t+1][j]
        denominator = 0

        for i in range(self.N):
            for j in range(self.N):
                denominator += self.alpha[t][i]*self.A[i][j]*self.B[j][self.O[t+1]]*self.beta[t+1][j]

        return numerator/denominator

    def init(self):
        """
        随机生成 A，B，Pi
        并保证每行相加等于 1
        """
        import random
        for i in range(self.N):
            randomlist = [random.randint(0,100) for t in range(self.N)]
            Sum = sum(randomlist)
            for j in range(self.N):
                self.A[i][j] = randomlist[j]/Sum

        for i in range(self.N):
            randomlist = [random.randint(0,100) for t in range(self.M)]
            Sum = sum(randomlist)
            for j in range(self.M):
                self.B[i][j] = randomlist[j]/Sum

    def train(self, O, MaxSteps = 5):
        self.T = len(O)
        self.O = O

        # 初始化
        self.init()

        step = 0
        # 递推
        while step<MaxSteps:
            step+=1
            print(step)
            tmp_A = np.zeros((self.N,self.N))
            tmp_B = np.zeros((self.N,self.M))
            tmp_pi = np.array([0.0]*self.N)

            self.forward()
            self.backward()

            # a_{ij}
            for i in range(self.N):
                for j in range(self.N):
                    numerator=0.0
                    denominator=0.0
                    for t in range(self.T-1):
                        numerator += self.cal_ksi(i,j,t)
                        denominator += self.cal_gamma(i,t)
                    tmp_A[i][j] = numerator/denominator

            # b_{jk}
            for j in range(self.N):
                for k in range(self.M):
                    numerator = 0.0
                    denominator = 0.0
                    for t in range(self.T):
                        if k == self.O[t]:
                            numerator += self.cal_gamma(j,t)
                        denominator += self.cal_gamma(j,t)
                    tmp_B[j][k] = numerator / denominator

            # pi_i
            for i in range(self.N):
                tmp_pi[i] = self.cal_gamma(i,0)

            self.A = tmp_A
            self.B = tmp_B
            self.Pi = tmp_pi
          #  print(self.A)

    def generate(self, length):
        import random
        I = []

        # start
        ran = random.randint(0,1000)/1000.0
        i = 0
        while self.Pi[i]<ran or self.Pi[i]<0.0001:
            ran -= self.Pi[i]
            i += 1
        I.append(i)

        # 生成状态序列
        for i in range(1,length):
            last = I[-1]
            ran = random.randint(0, 1000) / 1000.0
            i = 0
            while self.A[last][i] < ran or self.A[last][i]<0.0001:
                ran -= self.A[last][i]
                i += 1
            I.append(i)

        # 生成观测序列
        Y = []
        for i in range(length):
            k = 0
            ran = random.randint(0, 1000) / 1000.0
            while self.B[I[i]][k] < ran or self.B[I[i]][k]<0.0001:
                ran -= self.B[I[i]][k]
                k += 1
            Y.append(k)
        return Y



def triangle(length,b):
    '''
    三角波
    '''
    X = [i for i in range(length)]
    Y = []

    for x in X:
        Y.append(int(b[x] / 100))
    return X,Y
def triangle2(length):
    '''
    三角波
    '''
    X = [i for i in range(length)]
    Y = []

    for x in X:
        x = x % 6
        if x <= 3:
            Y.append(x)
        else:
            Y.append(6-x)
    return X,Y


def show_data(x,y):
    import matplotlib.pyplot as plt
    plt.plot(x, y, 'g')
    plt.show()

    return y


if __name__ == '__main__':
    df = pd.read_csv('./甜玉米_data.csv')
    a = df.values.tolist()
    b = []
    for i in a:
        b.append(i[6])
    hmm = HMM(10,3660)
    #print(triangle(20))
    tri_x, tri_y = triangle(30, b)
    x,y =triangle2(39)
    print(tri_y)
    print(y)
   #print(b)
    hmm.train(tri_y)
   # hmm.train(y)
    y = hmm.generate(365)
    print(y)
    # x = [i for i in range(365)]
    # show_data(x,y)
    # a = [47, 41, 27, 79, 63, 63, 64, 81, 15, 66, 27, 63, 81, 70, 91, 63, 87, 91, 91, 87, 40, 63, 64, 63, 15, 41, 52, 199, 142, 78, 81, 58, 66, 27, 79, 114, 63, 79, 114, 60, 63, 70, 91, 64, 111, 15, 83, 27, 79, 63, 64, 29, 58, 83, 27, 63, 81, 47, 83, 52, 122, 114, 78, 63, 70, 77, 40, 87, 64, 122, 142, 63, 79, 142, 63, 63, 15, 83, 52, 199, 142, 63, 122, 40, 63, 64, 122, 142, 63, 29, 15, 41, 52, 199, 114, 78, 111, 47, 83, 55, 64, 29, 15, 83, 52, 122, 40, 40, 40, 63, 40, 91, 64, 29, 58, 83, 55, 78, 199, 114, 63, 29, 15, 66, 52, 79, 142, 60, 111, 15, 66, 52, 60, 111, 70, 87, 64, 79, 142, 78, 79, 114, 78, 63, 58, 66, 52, 64, 63, 58, 83, 55, 63, 199, 142, 63, 29, 15, 83, 27, 122, 114, 60, 29, 15, 41, 27, 78, 199, 87, 64, 122, 114, 60, 29, 47, 41, 55, 78, 81, 58, 66, 55, 60, 29, 58, 41, 52, 63, 111, 15, 83, 52, 78, 122, 142, 60, 63, 47, 66, 55, 64, 63, 47, 66, 52, 199, 77, 64, 79, 142, 78, 111, 47, 41, 27, 122, 142, 63, 79, 77, 40, 87, 91, 64, 199, 87, 77, 64, 79, 114, 78, 63, 70, 87, 91, 87, 64, 63, 15, 41, 55, 60, 81, 70, 87, 63, 64, 199, 114, 60, 81, 15, 41, 27, 122, 77, 64, 111, 47, 66, 55, 60, 63, 58, 41, 52, 122, 142, 64, 111, 47, 66, 52, 60, 29, 15, 41, 55, 63, 199, 114, 78, 63, 15, 83, 27, 122, 114, 60, 81, 15, 41, 27, 79, 142, 60, 111, 15, 66, 55, 78, 79, 40, 64, 81, 70, 40, 64, 29, 47, 83, 55, 60, 81, 58, 66, 27, 199, 142, 64, 81, 58, 66, 55, 199, 40, 64, 81, 58, 41, 27, 79, 142, 63, 29, 15, 83, 52, 122, 63, 64, 111, 58, 41, 27, 78, 122, 114, 78, 199, 77, 40, 87, 77, 91, 91, 64, 199, 91, 64, 79, 114, 63, 29]
    # b = []
    # begin = datetime.date(2018, 1, 11)
    # delta = datetime.timedelta(days = 1)
    # for i in range(len(a)):
    #     current = {
    #         'time': begin.strftime("%Y-%m-%d"),
    #         'sales': a[i] * 100 + random.randint(0, 100)
    #     }
    #     b.append(current)
    #     begin += delta
    # print(b)