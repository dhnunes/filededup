import sys
from Library import filehasher
import pdb

file = filehasher.FileHasher(sys.argv[1])

print(file.file_walker())

# all_tests = list()
# for value in result.values():
#     all_tests.append(value)

# for test in all_tests:
#     print(all_tests.count(test))
# if all_tests.count(test) > 1:
# for key, value in result.items():
#     if value == test:
#         print(key)
#         print(test)
#         print(value)
