import hashlib

# Variables to use

int_val = 4
str_val = 'PythonIsBest'
flt_val = 24.56

# Hash Table  

class HashItem: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 

class HashTable: 
    def __init__(self): 
        self.size = 256 
        self.slots = [None for i in range(self.size)] 
        self.count = 0 


    def __hash__(self, key): 
        mult = 1 
        hv = 0 
        for ch in key: 
            hv += mult * ord(ch) 
            mult += 1 
        return hv % self.size 

    def put(self, key, value): 
            item = HashItem(key, value) 
            h = self.__hash__(key) 
            
            while self.slots[h] is not None: 
                if self.slots[h].key is key: 
                    break 
                h = (h + 1) % self.size 

            if self.slots[h] is None: 
                self.count += 1 
                self.slots[h] = item  

    def get(self, key):
        h = self.__hash__(key)

        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+ 1 ) % self.size

        return None

# Custome functions for hashes

def myhash(to_hash): 
    mult = 1 
    hv = 0 
    for ch in to_hash: 
        hv += mult * ord(ch) 
        mult += 3 
    return hv 

def myhash_v1(to_hash):
    return hash(to_hash)

def myhash_v2(to_hash): 
    m = hashlib.sha224(to_hash.encode('utf8')).hexdigest()    
    return m


# Creating a new hash table
table = HashTable()
table.put("language", str_val) 
table.put("integer", int_val) 
table.put("float", flt_val) 


#Calling the functions to display the different hashes

print("\n------ Using manual hashes --------")

for item in ((str(int_val), str_val, str(flt_val))): 
        print("{}: {}".format(item, myhash(item))) 

print("\n------ Using the hash() --------")

for item in ((str(int_val), str_val, str(flt_val))): 
        print("{}: {}".format(item, myhash_v1(item))) 

print("\n------ Using hashlib --------")

for item in ((str(int_val), str_val, str(flt_val))): 
        print("{}: {}".format(item, myhash_v2(item))) 

print("\n------ Using Hash Table --------")

for key in ("language", "integer", "float", "favorite class"): 
    v = table.get(key) 
    print(key,":",v) 

# Using just print and hash()
print("\n------ Using Just Print and hash()--------")
print("PythonIsBest :", hash(str_val))
print("4 :", hash(int_val))
print("24.56 :", hash(flt_val))