import random


class Ch:
    def duplicate(self, li, stat):
        dup = []
        lst = []
        for i in li:
            if i in lst:
                dup.append(i)
            else:
                lst.append(i)
        if stat == 0:
            return lst
        else:
            return dup

    def create(self):
        vazir = []
        while len(vazir) < 8:
            gene = random.randint(1, 8)
            if gene not in vazir:
                vazir.append(gene)
        return vazir

    def dup_count(self, li):
        return len(self.duplicate(li, 1))

    def mutate(self, li):
        dup = self.duplicate(li, 1)
        lst = self.duplicate(li, 0)
        index = []
        for item in dup:
            index.append(li.index(item))
        for ii in index:
            for i in range(1, 9):
                if i not in lst:
                    lst.insert(ii, i)
        return lst

    def score(self, li):
        sc = 0
        if self.dup_count(li) > 0:
            sc += self.dup_count(li)
        for i in li:
            for j in li:
                if j != i & abs(li.index(i) - li.index(j)) == abs(i - j):
                    sc += 1
        return sc - 8

    def lst_index(self, li):
        lst = []
        for i in li:
            lst.append(li.index(i))
        return lst


class Gen:
    parent = []
    child = []
    temp = []
    ch = Ch()
    g = 0

    def __init__(self):
        for i in range(20):
            self.parent.append(self.ch.create())

    def crossOver(self, l1, l2):
        swapped1 = []
        swapped2 = []
        point = random.randint(1, 8)
        h1 = l1[:point]
        s2 = l2[point:]
        h2 = l1[point:]
        s1 = l2[:point]
        for i in range(len(h1)):
            swapped1.append(h1[i])
        for i in range(len(s2)):
            swapped1.append(s2[i])
        for i in range(len(h2)):
            swapped2.append(h2[i])
        for i in range(len(s1)):
            swapped2.append(s1[i])
        return [swapped1, swapped2]

    def next_gen(self):
        lst = []
        self.g += 1
        for p in range(0, len(self.parent), +2):
            ls = self.crossOver(self.parent[p], self.parent[p + 1])
            for i in ls:
                lst.append(i)
        for c in lst:
            if self.ch.dup_count(c) > 0:
                self.child.append(self.ch.mutate(c))
            else:
                self.child.append(c)

    def select(self):
        lst = []
        te = []
        for i in self.parent:
            lst.append(i)
        for ii in self.child:
            lst.append(ii)
        for c in lst:
            te.append(self.ch.score(c))
        for s in range(20):
            m = min(te)
            if m == 0:
                print("Generation " + str(self.g) + " : " + str(lst[te.index(0)]))
            self.temp.append(lst[te.index(m)])
            te.remove(m)
        self.parent.clear()
        for item in self.temp:
            self.parent.append(item)
        self.child.clear()
        self.temp.clear()

    def print_result(self):
        for i in range(250):
            self.next_gen()
            self.select()
