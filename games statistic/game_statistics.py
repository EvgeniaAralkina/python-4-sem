import matplotlib.pyplot as plt
f = open('games.txt', 'r', encoding='utf8')
years = {}
ten = {}
for line in f:
    arr = line.split(';')
    if years.get(arr[3][1:5]) == None:
        years[arr[3][1:5]] = 1
    else:
        years[arr[3][1:5]] += 1
    if (ten.get(arr[3][3:4])) == None:
        ten[arr[3][3:4]] = {}
        ten[arr[3][3:4]][arr[1][1:-1]] = 1
    elif ten.get(arr[3][3:4]).get(arr[1][1:-1]) == None:
        ten[arr[3][3:4]][arr[1][1:-1]] = 1
    else:
        ten[arr[3][3:4]][arr[1][1:-1]] += 1


del(years['не и'])
del(ten[' '])

sorted_ten = {'8':{},'9':{},'0':{}}
sorted_keys = {'8':{},'9':{},'0':{}}
for i in ten:
    sorted_key = sorted(ten[i], key=ten[i].get)
    sorted_keys[i] = sorted_key


sum1=[]
for i in sorted_keys:
    for w in sorted_keys[i]:
        #print(w)
        #print(ten[i][w])
        sorted_ten[i][w] = ten[i][w]
    sum1.append(sum(sorted_ten[i].values()))


fig = plt.figure()
ax_1 = fig.add_subplot(2,1,2)
ax_1.set_facecolor('black')
ax_1.set_xlim([0, len(years.keys())])
ax_1.set_ylim([0, max(years.values())])
ax_1.set_title('кол-во игр в год')
ax_1.plot(years.keys(),years.values())

ax_2 = fig.add_subplot(2,3,1)
ax_2.set_title('топ 3 игр в 80-е')
a,b,c = sorted_ten['8'].popitem(),sorted_ten['8'].popitem(),sorted_ten['8'].popitem()
ax_2.pie([a[1],b[1],c[1]])
labels =[a[0],b[0],c[0]]
colors = ['blue', 'orange', 'green']
plt.legend(labels, loc="best", fontsize = 7)

ax_3 = fig.add_subplot(2,3,2)
ax_3.set_title('топ 3 игр в 90-е')
a1, b1, c1 = sorted_ten['9'].popitem(), sorted_ten['9'].popitem(), sorted_ten['9'].popitem()
ax_3.pie([a1[1], b1[1], c1[1]])
labels =[a1[0], b1[0], c1[0]]
colors = ['blue', 'orange', 'green']
plt.legend(labels, loc="best", fontsize = 7)

ax_4 = fig.add_subplot(2,3,3)
ax_4.set_facecolor('black')
ax_4.set_title('топ 3 игр в 00-е')
a2, b2, c2 = sorted_ten['0'].popitem(), sorted_ten['0'].popitem(), sorted_ten['0'].popitem()
ax_4.pie([a2[1], b2[1], c2[1]])
labels =[a2[0], b2[0], c2[0]]
colors = ['blue', 'orange', 'green']
plt.legend(labels, loc="best", fontsize = 7)

plt.show()