class HashTable:
    # Initialize hash table with default 2x size of the package file and empty lists for each bucket
    def __init__(self, capacity = 80):
        self.capacity = capacity
        self.buckets = [[] for i in range(self.capacity)]
        self.size = 0
    
    def hash(self, key):
        # Simple hash function as each package ID is already a unique integer
        return abs(key)

    # Insertion function for A.
    def insert(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]

        # Updates value if key is already there
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Insert new pair if key not present
        bucket.append((key, value))
        self.size += 1
    
    # Lookup function for B.
    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        # Return value when matching key found in bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v

    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return
        
        raise KeyError(f"Key '{key}' not found in HashTable.")
    
    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def len(self):
        return self.size
    
    def __str__(self) -> str:
    # Returns a readable string representation of the non-empty buckets
        active_buckets = {i: b for i, b in enumerate(self.buckets) if b}
        return f"HashTable({active_buckets})"




