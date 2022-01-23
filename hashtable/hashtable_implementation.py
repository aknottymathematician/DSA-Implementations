class HashTable:
    def __init__(self):
        self.SIZE = 10
        self.arr = [None for i in range(self.SIZE)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.SIZE

    '''
    How to use the below implementation of add, get and delete
    t = HashTable()
    t.add('str1', 10)
    t.get('str1')
    t.delete('str1')
    '''
    
    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    '''
    Though not bad, there is a better way to implement above functions using default python operators
    __setitem__{add function}
    __getitem__{get function}
    __delitem__ {delete function}
    The way to use these functions is simpler
    t['str1'] = 10{SET}
    t['str1']{GET}
    del t['str1']{DELETE}
    '''
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
print(t.arr)
t['str1'] = 10#{SET}
print(t.arr)
print(t['str1'])#{GET}
del t['str1']
print(t.arr)