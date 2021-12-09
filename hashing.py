from __future__ import print_function



#import hashlib library
import hashlib 

# variable to store the input
print("================================================")
print("")
string = "Hashing Algorithm Implementation"

#encode the input
encoded=string.encode()

#hash the input using md5 algorithm
result = hashlib.md5(encoded)
print("String : ", end ="")
print(string)
print("================================================")


print("Hash Value : ", end ="")
print("")


print(result)
print("================================================")
print("Hexadecimal equivalent: ",result.hexdigest())
print("================================================")
