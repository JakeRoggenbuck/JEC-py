# JEC-py
Jabacat's Easy Config

[JEC-py](https://github.com/JakeRoggenbuck/JEC-py) | JEC-rs | [JEC-go](https://github.com/JakeRoggenbuck/JEC-go) | JEC-c | JEC-c++ | JEC-zig | JEC-ts

## Usage
```py
conf_1 = ConfigFile("./config.yml")
conf_2 = ConfigFile.from_home("./config.yml")

dir_1 = ConfigDir("./config/")
dir_2 = ConfigDir.from_home("./config/")

if not dir_1.exists():
	dir_1.create()

dir_1.remove()
```
