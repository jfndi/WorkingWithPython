#
# This example shows how to use name mangling for letting subclasses override
# methods without breaking intra-class method calls.
#
class Mapping:
    def __init__(self, iterable):
        print('Inside base class __init__() method')
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # Provide new signature for update()
        # but does not break __init()__().
        for item in zip(keys, values):
            self.items_list.append(item)


if __name__ == "__main__":
    x = MappingSubclass([])
    print('MappingSubclass instantiated.')
    x.update(['name', 'gender', 'age'], ['Jef', 'male', 57])
