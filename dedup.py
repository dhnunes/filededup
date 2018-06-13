import hashlib
import os
import sys
import pdb


def file_walker(path: str) -> tuple:
    all_files = list()

    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.getsize(os.path.join(root, file)):
                all_files.append(os.path.join(root, file))

    return(file_hash_association(tuple(all_files)))


def file_hasher(file: str) -> str:
    buffer_size = 65536
    sha256_object = hashlib.sha256()
    with open(file, 'rb') as file:
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            sha256_object.update(data)
    return(sha256_object.hexdigest())


def file_hash_association(hashed_files: tuple) -> dict:
    results = dict()

    for file in hashed_files:
        results[file] = file_hasher(file)

    return(results)


print(file_walker(sys.argv[1]))

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
