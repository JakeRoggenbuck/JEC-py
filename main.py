from pathlib import Path


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
        pass

    def remove(self):
        pass


class ConfigDir(ConfigBase):
    def create(self):
        pass

    def remove(self):
        pass
