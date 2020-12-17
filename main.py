from HashMap import HashMap

def print_hash_table(ht):
    for i in range(ht.num_buckets):
        print (i, ":", sep = "", end = "")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print(key, end = " ")
        print()

# A basic demo of the methods in our hashmap class
hash_map = HashMap()
print("-----------------*----------------")
print("Welcome to a brief showdown of our HashMap!") 
print("-----------------*----------------")
print("Our HashMap is empty right now, and it looks like this:\n")
print_hash_table(hash_map)
print()
print('-------------------')
print()
print("Let's insert a few entries to our HashMap : (AAPL, 100), (GOOG, 200), (SP500, 175.75).\n")
hash_map["AAPL"] = 100
hash_map["GOOG"] = 200
hash_map["SP500"] = 175.75
print("After inserting our position, our hashMap looks like this:")
print_hash_table(hash_map)
print('-------------------')
print()
print("Let's now double the value of one of our entries : (GOOG, 400)")
hash_map["GOOG"] = 400
print("After doubling our number of shares in Google, our hashMap looks like this: \n") 
print_hash_table(hash_map)
print('-------------------')
print()
print("Oh no! Apple's stock doesn't look to be in a great position. Let's sell it!")
del(hash_map["AAPL"])
print("After selling all of our shares in Apple: ")
print_hash_table(hash_map)
print('-------------------')
print()
print("Let's use that money to buy some new stocks!!\n")
hash_map["BRK-A"] = 50
hash_map["AMZN"] = 100
hash_map["FB"] = 150
hash_map["JNJ"] = 200
hash_map["XOM"] = 25
hash_map["GE"] = 250
print("After buying spree we now hold: ")
print_hash_table(hash_map)
print('-------------------')
print()
print("Thanks for tuning in! Have a great day!")
print("-----------------*----------------")
