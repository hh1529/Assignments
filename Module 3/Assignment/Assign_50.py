#  How will you create a dictionary using tuples in python? 
test_tup1 = (1,2,3)
test_tup2 = ("harsh","kite","apple")
if len(test_tup1) == len(test_tup2):
    res = dict(zip(test_tup1, test_tup2))
print("Dictionary : " + str(res))
