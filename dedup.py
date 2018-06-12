import hashlib
import os
import sys


def file_hasher(path):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
        return(sha256.hexdigest())


root_of_tests = sys.argv[1]

result = dict()
all_files = list()
all_dirs = list()
for root, dirs, files in os.walk(root_of_tests):
    for name in files:
        all_files.append(os.path.join(root, name))

for file in all_files:
    result[file] = file_hasher(file)

# for key, value in result.items():
#     print(key, value)
all_tests = list()
for value in result.values():
    all_tests.append(value)

for test in all_tests:
    print(all_tests.count(test))

for test in all_tests:
    if all_tests.count(test) > 1:
        for key, value in result.items():
            if value == test:
                print(key)
                print(test)
                print(value)
