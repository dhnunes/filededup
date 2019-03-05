"""
TODO docstring.

Docstring
"""

import hashlib
import os
import time
from tqdm import tqdm
from reprint import output
import multiprocessing
import pdb


class FileHasher():
    """
    TODO docstring.

    Docstring
    """

    def __init__(self, dedup_root: str):
        """
        TODO docstring.

        Docstring
        """
        self.dedup_root = dedup_root

    def __repr__(self):
        """
        TODO docstring.

        Docstring
        """
        pass

    def file_hash_association(self, files_path: tuple) -> dict:
        """
            Calls file hasher, associate a hash with file, and returns a dict
            with files as keys and hashs as values
        """
        results = dict()
        pool = multiprocessing.Pool(processes=20)

        with output(output_type="list", initial_len=5, interval=0) as output_list:
            for file in files_path:

                # pdb.set_trace()
                print(f"Main Process ID {os.getpid()}")

                results[file] = pool.apply(self.file_hasher, args=(file,))
                # pool.map(self.file_hasher, files_path)

            pool.close()
        # for file in files_path:
        # # Here comes the progress bar update
        #     time.sleep(0.2)
        #     #print(file)
        #     results[file] = self.file_hasher(file)

        return(results)

    def file_walker(self, root_path: str = None) -> tuple:
        """
        Walks through a directory tree.

        Given a path ( usually as parameter in command line or directly if
        using as a library ), this function will walk starting at that point
        in directory tree and will return a list of non-empty, non-link
        files ( if called as a Library ) or a tuple if called as a
        standalone application.

        Parameters:
        root_path (str): The relative or absolute path to methd works.

        Returns:
        list: If called as Library
        tuple: If called as cmd application
        """
        if root_path is None:
            root_path = self.dedup_root

        all_files = list()

        for root, dirs, files in os.walk(root_path):
            for file in files:
                if os.path.islink(os.path.join(root, file)):
                    continue
                else:
                    if os.path.getsize(os.path.join(root, file)):
                        all_files.append(os.path.join(root, file))

        return(self.file_hash_association(tuple(all_files)))

    def file_hasher(self, file: str) -> str:
        """
            Opens and hashs a file using SHA 256.
        """
        print(multiprocessing.current_process())
        print(f"Process ID {os.getpid()}")
        buffer_size = 65536
        sha256_object = hashlib.sha256()
        with open(file, 'rb') as file:
            while True:
                data = file.read(buffer_size)
                if not data:
                    break
                sha256_object.update(data)
        return(sha256_object.hexdigest())

    def file_find_duplicates(self, hashed_dict: dict):
            final = { k:v for (k,v) in result.items() if list(result.values()).count(v) > 1}
