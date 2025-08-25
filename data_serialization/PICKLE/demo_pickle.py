import pickle 

# save 
data = {"name":"Alice","age":30,"scores":[90,85,88]}
with open('data.pkl','wb') as f:
    pickle.dump(data,f)

# load
with open('data.pkl','rb') as f:
    loaded_data = pickle.load(f)
print(loaded_data)

# strings
data_string = pickle.dumps(data)
loaded_data_string = pickle.loads(data_string)
print(data_string)  # --> convert to bytes
print(loaded_data_string) # convert from bytes

# problem- key-value store 
# kv_store.py
import pickle, os
class KeyValueStore:
    def __init__(self, file='store.pkl'):
        self.file = file
        self._load()
    def _load(self):
        if os.path.exists(self.file):
            self.store = pickle.load(open(self.file,'rb'))
        else:
            self.store = {}
    def set(self, key, value):
        self.store[key] = value
        self._save()
    def get(self, key, default=None):
        return self.store.get(key, default)
    def delete(self, key):
        self.store.pop(key, None)
        self._save()
    def _save(self):
        pickle.dump(self.store, open(self.file,'wb'))

if __name__=='__main__':
    kv = KeyValueStore()
    kv.set('name','Bob')
    kv.set('age', 28)
    print(kv.get('name'))   # Bob
    kv.delete('age')
    print(kv.get('age'))    # None

