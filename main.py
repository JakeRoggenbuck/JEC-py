from pathlib import Path
import os


class ConfigBase:
    def __init__(self, path: str):
        self.path = path
        self.path_obj = Path(path)

    def exists(self):
        return self.path_obj.exists()

    @staticmethod
    def from_home(path: str):
        return str(Path.home() / Path(path))


class ConfigFile(ConfigBase):
    def create(self):
        with open(self.path) as _:
            pass

    def remove(self):
        os.remove(self.path)


class ConfigDir(ConfigBase):
    def create(self):
        os.mkdir(self.path)

    def remove(self):
        os.rmdir(self.path)
