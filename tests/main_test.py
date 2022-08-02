from src.main import ConfigFile, ConfigDir


def test_config_file():
    conf_1 = ConfigFile("./config.yml")
    conf_2 = ConfigFile.from_home("./config.yml")

    assert conf_1.path != conf_2.path
    assert "home" not in conf_1.path
    assert "home" in conf_2.path

    assert not conf_1.exists()
    conf_1.create()

    assert conf_1.exists()

    conf_1.remove()


def test_config_dir():
    conf_1 = ConfigDir("./config/")
    conf_2 = ConfigDir.from_home("./config/")

    assert conf_1.path != conf_2.path
    assert "home" not in conf_1.path
    assert "home" in conf_2.path

    assert not conf_1.exists()
    conf_1.create()

    assert conf_1.exists()

    conf_1.remove()
