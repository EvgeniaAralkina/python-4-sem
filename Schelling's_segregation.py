import matplotlib.pyplot as plt
import random

class Model:
    size = 100
    population = 80
    min = 50
    max = 50
    tolerance = 20
    r = 5
    step = 20
    arr = [[], []]
    b1, b2, c1, c2, B1, B2, C1, C1 = [], [], [], [], [], [], [], []

    def __init__(self, size, population, min, tolerance, r, step):
        self.size = size
        self.population = population
        self.step = step
        self.r = r
        self.min = min
        self.tolerance = tolerance
        self.max = 100 - min
        #b1, b2, c1, c2, B1, B2, C1, C1 = [], [], [], [], [], [], [], []

    def build_first(self):
    # заполнение точками
        for i in range(self.population):
            self.arr[0].append(random.randint(0,self.size))
            self.arr[1].append(random.randint(0,self.size))
        for j in range (i):
            while (self.arr[0][i]==self.arr[0][j] and self.arr[1][i]==self.arr[1][j]):
                self.arr[0][i], self.arr[1][i] = random.randint(0,self.size), random.randint(0,self.size)

        k = (int(len(self.arr[0]) / 100 * self.min))
        #print (k, self.population-k)
        self.B1 = (self.arr[0][:k])
        self.B2 = (self.arr[1][:k])
        self.C1 = (self.arr[0][k:])
        self.C2 = (self.arr[1][k:])

        for i in range(int(len(self.arr[0]) / 100 * self.min)-1):
            self.b1.append(self.B1[i])
            self.b2.append(self.B2[i])
        for i in range(int(len(self.arr[0]) / 100 * self.max)-1):
            self.c1.append(self.C1[i])
            self.c2.append(self.C2[i])

    def distance(self, a1, b1, a2, b2):
        return abs(a1-a2)+abs(b1-b2)

    def is_happy_2(self, a, b, A1, A2, i, key):
        t = (int(self.population / 100 * self.max)) if key == 'max' else (int(self.population / 100 * self.min))
        k = 0
        for i in range(t):
            if (self.distance(a, b, A1[i], A2[1]) > 0 and self.distance(a, b, A1[i], A2[1]) < self.r):
                k += 1
            if k >= self.tolerance: return True
        if k<self.tolerance:
            return False



    def is_happy(self, a, b, A1, A2, i, key):
        step=0
        while (self.is_happy_2(a, b, A1, A2, i, key)==False and step<150):
            A1[i], A2[i] = random.randint(0,self.size),random.randint(0,self.size)
            step+=1
            for j in range(i):
                while (A1[i] == A1[j] and A2[i] == A2[j]):
                    A1[i], A2[i] = random.randint(0,self.size),random.randint(0,self.size)

        return A1,A2

    def mutations(self):
        k1=0
        k2=0
        count_happy=[[],[]]
        coord1, coord2 = [[],[]],[[],[]]
        for i in range(self.step):
            for j in range(int(self.population /100 * self.min)):
                self.is_happy(self.B1[j], self.B2[j], self.B1, self.B2, j, 'min')
                if (self.is_happy_2(self.B1[j], self.B2[j], self.B1, self.B2, j, 'min')==True):
                    k1+=1
            for j in range(int(self.population /100 * self.max)):
                self.is_happy(self.C1[j], self.C2[j], self.C1, self.C2, j, 'max')
                if (self.is_happy_2(self.C1[j], self.C2[j], self.C1, self.C2, j, 'max')==True):
                    k2+=1
            count_happy[0].append(k1)
            count_happy[1].append(k2)
            arr = [[],[],[],[]]
            arr[0].extend(self.B1)
            arr[1].extend(self.B2)
            arr[2].extend(self.C1)
            arr[3].extend(self.C2)
            coord1[0].append(arr[0])
            coord1[1].append(arr[1])
            coord2[0].append(arr[2])
            coord2[1].append(arr[3])
            k1,k2=0,0
        return count_happy, coord1, coord2

    def build_window(self):
        arr, c1, c2 = self.mutations()

        fig1, ax = plt.subplots()

        for i in range(self.step):
            ax.cla()
            ax.set_xlim([0, self.size])
            ax.set_ylim([0, self.size])
            ax.scatter(c1[0][i], c1[1][i], color='blue', marker="s")
            ax.scatter(c2[0][i], c2[1][i], color='green', marker="s")
            ax.set_title("итерация {}".format(i))
            plt.pause(0.1)

        fig = plt.figure()
        ax_1 = fig.add_subplot(2, 2, 1)
        ax_2 = fig.add_subplot(2, 2, 2)
        ax_3 = fig.add_subplot(2, 2, 3)
        ax_4 = fig.add_subplot(2, 2, 4)


        ax_1.set_facecolor('black')
        ax_1.set_xlim([0, self.size])
        ax_1.set_ylim([0, self.size])
        ax_1.set_title('0 итераций')

        ax_2.set_facecolor('black')
        ax_2.set_xlim([0, self.size])
        ax_2.set_ylim([0, self.size])
        ax_2.set_title(str(self.step)+' итераций')

        ax_3.set_facecolor('black')
        ax_3.set_xlim([0, self.step])
        ax_3.set_ylim([0, int(self.population /100 * self.min)])
        ax_3.set_title('изменение настроения')

        ax_4.set_facecolor('black')
        ax_4.set_xlim([0, self.step])
        ax_4.set_ylim([0, int(self.population /100 * self.max)])
        ax_4.set_title('изменение настроения')

        ax_1.scatter(self.b1, self.b2, color='blue', marker="s")
        ax_1.scatter(self.c1, self.c2, color='green', marker="s")
        ax_2.scatter(self.B1, self.B2, color='blue', marker="s")
        ax_2.scatter(self.C1, self.C2, color='green', marker="s")

        steps = [i for i in range(self.step)]
        #print(len(steps), len(arr[0]), len(arr[1]))
        ax_3.plot(steps,arr[0])
        ax_4.plot(steps, arr[1])
        #print(arr[0],arr[1])
        plt.show()


m = Model(100,80,35,1,4,50)
m.build_first()
m.build_window()