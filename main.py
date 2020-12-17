from HashMap import HashMap

def print_hash_table(ht):
    for i in range(ht.num_buckets):
        print (i, ":", sep = "", end = "")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print(key, sep = "", end = " ")
        print()

# A basic demo of the methods in our hashmap class
hash_map = HashMap()
print("Welcome to a brief tutorial of our hashmap!\n") 

hash_map["AAPL"] = 100
hash_map["GOOG"] = 200
hash_map["SP500"] = 175.75
print("After inserting our positions:")
print()
print_hash_table(hash_map)

hash_map["GOOG"] = 400
print("After doubling our number of shares in Google: ") 
print_hash_table(hash_map)

del(hash_map["AAPL"])

print("After selling all of our shares in Apple: ")
print_hash_table(hash_map)

hash_map["BRK-A"] = 50
hash_map["AMZN"] = 100
hash_map["FB"] = 150
hash_map["JNJ"] = 200
hash_map["XOM"] = 25
hash_map["GE"] = 250

print("After buying spree we now hold: ")
print_hash_table(hash_map)
