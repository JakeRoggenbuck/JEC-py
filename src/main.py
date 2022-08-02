from pathlib import Path
import os


class ConfigBase:
    def __init__(self, path: str):
        self.path = path
        self.path_obj = Path(path)

    def exists(self):
        return self.path_obj.exists()


class ConfigFile(ConfigBase):
    def create(self):
        with open(self.path, "w") as _:
            pass

    def remove(self):
        os.remove(self.path)

    @staticmethod
    def from_home(path: str):
        return ConfigFile(str(Path.home() / Path(path)))


class ConfigDir(ConfigBase):
    def create(self):
        os.mkdir(self.path)

    def remove(self):
        os.rmdir(self.path)

    @staticmethod
    def from_home(path: str):
        return ConfigDir(str(Path.home() / Path(path)))
