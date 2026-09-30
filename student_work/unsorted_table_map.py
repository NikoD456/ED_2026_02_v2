class UnsortedTableMap:
    # Diccionario implementado desde cero con una lista no ordenada de entradas [clave, valor].

    def __init__(self):
        # Crea un diccionario vacío.
        self._table = []                  # lista de entradas [clave, valor]

    # ---------- auxiliar ----------
    def _buscar(self, k):
        # Retorna el índice de la entrada con clave k, o -1 si no existe.
        for idx,i in enumerate(self._table):
            if k == i[0]:
                return idx
        return -1
        pass

    # ---------- núcleo: métodos especiales ----------
    def __len__(self):
        # len(M)
        return len(self._table)

    def __getitem__(self, k):
        idx = self._buscar(k)
        if idx == -1:
            raise KeyError
        return self._table[idx][1]


    def __setitem__(self, k, v):
        idx = self._buscar(k)
        if idx == -1:
            self._table.append([k,v])
        else:
            self._table[self._buscar(k)][1] = v

    def __delitem__(self, k):
        idx = self._buscar(k)
        if idx == -1:
            raise KeyError
        del self._table[self._buscar(k)]

    def __contains__(self, k):
        if self._buscar(k) == -1: return False
        return True

    def __iter__(self):
        for item in self._table:
            yield item[0]

    def __eq__(self, otro):
        # M == otro  (mismos pares, sin importar el orden)
        if not isinstance(otro, UnsortedTableMap):
            return False

        dic1 = set(tuple(item) for item in self._table)
        dic2 = set(tuple(item) for item in otro._table)
        return dic1 == dic2
        pass

    # ---------- dado ----------
    def __repr__(self):
        return '{' + ', '.join(f'{k!r}: {v!r}' for k, v in self._table) + '}'
