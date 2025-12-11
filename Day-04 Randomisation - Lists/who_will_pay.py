import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

"""
Bu yöntem doğru çalışıyor.

random_index_for_friends = random.randint(0,4)

print("Todays unlucky person is: " + friends[random_index_for_friends] + "!!! you will pay the bill :D")
"""

# bu da doğru çalışıyor.
print("Todays unlucky person is: " + random.choice(friends) + "!!! you will pay the bill :D")