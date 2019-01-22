from pdedup.core.filehasher import FileHasher
from pdedup.core.cmdargs import CmdArgs

def main():
    args = CmdArgs.cmd_parsed_args()
    file = FileHasher(args["dir_path"])
    result = file.file_walker()
    print(result)