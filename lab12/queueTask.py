import queue
from collections import deque

print("Работа с очередью через модуль queue")

q = queue.Queue()

q.put(10)
q.put(20)
q.put(30)

print("Содержимое очереди:")
for item in q.queue:
    print(" -", item)

print("Текущий размер очереди:", q.qsize())

print("Есть ли число 20 в очереди?", 20 in q.queue)

first_item = q.get()
print("Извлечен первый элемент:", first_item)
print("Размер после извлечения:", q.qsize())

q.queue.clear()
print("Очередь очищена.")

print("Очередь пуста?", q.empty())


print("Работа с очередью через collections.deque")

dq = deque()

dq.append(10)
dq.append(20)
dq.append(30)
print("Очередь после добавления:", list(dq))

print("Первый элемент (без удаления):", dq[0])

extracted = dq.popleft()
print("Извлеченный элемент:", extracted)

print("Размер очереди:", len(dq))
print("Очередь пуста?", len(dq) == 0)
