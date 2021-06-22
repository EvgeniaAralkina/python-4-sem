import json
import email.utils
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

with open('table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

days = [m['date'][:3] for m in messages]

messages = [(m['subj'].upper(), email.utils.parsedate(m['date']))  for m in messages]


#task 1 Как по времени суток распределяется активность студентов?
lst = list()
for i in messages:
    lst.append(i[1][3])

#fig = plt.figure()
plt.plot([i for i in range(24)], [lst.count(i) for i in range(24)], marker='o', color='black')
plt.xlabel('Время суток')
plt.ylabel('Колличество сообщений')
plt.xticks([i for i in range(24)])
plt.title("Как по времени суток распределяется активность студентов?")
plt.show()

#task 2 Как по дням недели распределяется активность студентов?

#fig = plt.figure()

mp = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.plot(mp, [days.count(i) for i in mp], marker='o', color='black')
plt.title("Как по дням недели распределяется активность студентов?")
plt.show()

#task 3 В каких группах было отправлено больше всего сообщений?
figure(figsize=(20,7))
lst1 = list()

for i in messages:
    lst1.append(i[0][:3].replace(' ', ''))


mp1 = set(lst1)
mp1 = list(mp1)
mp1.sort()

plt.bar(mp1, [lst1.count(i) for i in mp1])
plt.xlabel("Группа")
plt.ylabel("Кол-во отправленных сообщений")
plt.title("В каких группах было отправлено больше всего сообщений?")
plt.show()

#task 4 В каких группах было получено больше всего правильных решений?
figure(figsize=(20,7))
lst2 = list()
for i in table['data']:
    if i[3] == 1:
        lst2.append(i[0])

mp2 = set(lst2)
mp2 = list(mp2)
mp2.sort()

plt.bar(mp2, [lst2.count(i) for i in mp2])


plt.xlabel("Группа")
plt.ylabel("Кол-во верных решений")
plt.title("В каких группах было получено больше всего правильных решений?")
plt.show()

#task 5 Какие задачи оказались самыми легкими, самыми сложными?

lst3 = list()
for i in table['data']:
    if i[3] == 0:
        lst3.append(i[2])

mp3 = set(lst3)
mp3 = list(mp3)
mp3.sort()
plt.plot(mp3, [lst3.count(i) for i in mp3], marker='o', color='black')
#plt.bar(mp3, [lst3.count(i) for i in mp3])
maxa = max([lst3.count(i) for i in mp3])
mina = min([lst3.count(i) for i in mp3])
x = [mina, int((mina + maxa) / 2), maxa]
plt.yticks(x, ['easy', 'medium', 'hard'])
plt.title("Какие задачи оказались самыми легкими, самыми сложными?")
plt.show()

#print(failed)