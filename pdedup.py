"""
TODO DOCstring.

docstring
"""

from Library.filehasher import FileHasher
from Library.cmdargs import CmdArgs

#print(args)
#print(os.path.isdir(args.dir_path))


args = CmdArgs.cmd_parsed_args()

print(args)

# file = FileHasher(args.dir_path)

# print(file.file_walker())

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
