from configparser import ConfigParser


def get_config_data(section, key):
    config = ConfigParser()
    config.read(r'D:\New_project\WebApplicationFrameWork\Configurations\config_file.ini')
    return config.get(section, key)
