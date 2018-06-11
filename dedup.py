import hashlib
import os

root_of_tests = "/home/dnunes/avocado/job-results/job-2018-06-11T14.35-4958f56"

result = dict()
all_files = list()
all_dirs = list()
for root, dirs, files in os.walk(root_of_tests):
    for name in files:
        all_files.append(os.path.join(root, name))


for file in all_files:
    result[file] = hashlib.sha256(file.encode()).hexdigest()

for key, value in result.items():
    print(key, value)