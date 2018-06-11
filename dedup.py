import hashlib
import os


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


root_of_tests = "/home/dnunes/avocado/job-results/job-2018-06-11T14.35-4958f56"

result = dict()
all_files = list()
all_dirs = list()
for root, dirs, files in os.walk(root_of_tests):
    for name in files:
        all_files.append(os.path.join(root, name))

for file in all_files:
    result[file] = file_hasher(file)

for key, value in result.items():
    print(key, value)
