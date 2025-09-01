class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # agrega al final

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # quita el primero
        else:
            return None

    def front(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ==== Ejemplo de uso ====
queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')

print(f"Primer elemento: {queue.front()}")   # Salida: A
print(f"Elimina : {queue.dequeue()}")       # Salida: A
print(f"Nuevo primero: {queue.front()}")       # Salida: B
print(f"Tamaño de pila: {queue.size()}")       # Salida: 2
