import hashlib
import os


class FileHasher():

    def __init__(self, dedup_root: str):
        self.dedup_root = dedup_root

    def __repr__(self):
        pass

    def file_hash_association(self, hashed_files: tuple) -> dict:
        results = dict()

        for file in hashed_files:
            results[file] = self.file_hasher(file)

        return(results)

    def file_walker(self, root_path: str = None) -> tuple:
        """
            Given a path, returns a tuple with all non-empty files
        """
        if root_path is None:
            root_path = self.dedup_root

        all_files = list()

        for root, dirs, files in os.walk(root_path):
            for file in files:
                if os.path.getsize(os.path.join(root, file)):
                    all_files.append(os.path.join(root, file))

        return(self.file_hash_association(tuple(all_files)))

    def file_hasher(self, file: str) -> str:
        """

        """
        buffer_size = 65536
        sha256_object = hashlib.sha256()
        with open(file, 'rb') as file:
            while True:
                data = file.read(buffer_size)
                if not data:
                    break
                sha256_object.update(data)
        return(sha256_object.hexdigest())
