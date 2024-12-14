class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # 元の update() メソッドのプライベートコピー

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # update() への新シグネチャ導入
        # しかし __init__() は壊さない
        for item in zip(keys, values):
            self.items_list.append(item)

