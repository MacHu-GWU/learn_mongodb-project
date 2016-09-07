from learnMongo import test_col

test_col.remove({})
test_col.insert({"a": 1})
test_col.update({"a": 1}, {"$set": {"a": 2}})
print(test_col.find_one({"a": 2}))