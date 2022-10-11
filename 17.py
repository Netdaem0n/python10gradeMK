# В файле содержится последовательность из 10000
# целых положительных чисел. Каждое число не превышает
# 10000. Определите и запишите в ответе
# сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 120,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два
# различных элемента последовательности.
# Порядок элементов в паре не важен.
#0.1 - считать файл и создать список
#0.2 - создать второй список из сумм пар
#1 - (a+b) % 120 == 0
#2 - list() - > max()

data = []
with open("files_tasks/17.txt", "r") as f:
    data = f.readlines()

data = [int(x.strip("\n")) for x in data]
print(data)
print(len(data))
data2 = [data[x]+data[x+1] for x in range(0, int(len(data)), 2)]
print(data2)
print(len(data2))