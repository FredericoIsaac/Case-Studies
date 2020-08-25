# Source: https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/a5f68248-862f-4a72-8682-24b86e2f6d61/lessons/b24e0f2b-815d-46c5-96dc-d74ef2294c12/concepts/8a30b719-1d4c-4815-b41c-8cc3ac6beb7a

class HashMap:
    
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37                  # a prime numbers 
        self.num_entries = 0
        
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)                        # The returned hash code will be the bucket_index
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)                          # length of array to be used in Mod operation
        
        current_coefficient = 1                                       # represents (self.p^0) which is 1
        
        hash_code = 0
        
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code (Mod operation)
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient as well

        return hash_code % num_buckets                                # one last compression before returning
    
    
    def size(self):
        return self.num_entries

hash_map = HashMap()

bucket_index = hash_map.get_bucket_index("abcd")
print(bucket_index)
# 4

bucket_index = hash_map.get_bucket_index("bcda")
print(bucket_index)
# 2


bucket_index = hash_map.get_bucket_index("one")
print(bucket_index)
# 0
bucket_index = hash_map.get_bucket_index("neo")
print(bucket_index)                                  # Collision might occur
# 6