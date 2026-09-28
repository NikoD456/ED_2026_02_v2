class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def _bubble_up(self, index):
        while index > 1 and self.arreglo[index] < self.arreglo[index // 2]:
            self.arreglo[index], self.arreglo[index // 2] = (
                self.arreglo[index // 2],
                self.arreglo[index],
            )
            index //= 2

    def _bubble_down(self, index):
        n = len(self.arreglo) - 1
        while 2 * index <= n:
            hijo = 2 * index
            if hijo < n and self.arreglo[hijo + 1] < self.arreglo[hijo]:
                hijo += 1

            if self.arreglo[index] <= self.arreglo[hijo]:
                break

            self.arreglo[index], self.arreglo[hijo] = self.arreglo[hijo], self.arreglo[index]
            index = hijo

    def insert(self, valor):
        self.arreglo.append(valor)
        self._bubble_up(len(self.arreglo) - 1)

    def remove_smallest(self):
        if len(self.arreglo) == 1:
            return None

        menor = self.arreglo[1]
        ultimo = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            self._bubble_down(1)

        return menor

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)
        for i in range(len(self.arreglo) // 2, 0, -1):
            self._bubble_down(i)
