
import configparser, os

class INIHandler:
    @staticmethod
    def load_info(_file, option, debug=False):
        configFilename = os.environ.get('TMPDIR', os.getenv('TEMP', '')) + "/" + _file
        config = configparser.ConfigParser()
        config.read(configFilename)
        info = ""
        try:
            info = config.get("ROOT", option)
        except:
            pass
        if debug:
            print(configFilename)
        return info

    @staticmethod
    def save_info(_file, option, info, debug=False):
        configFilename = os.environ.get('TMPDIR', os.getenv('TEMP', '')) + "/" + _file
        config = configparser.ConfigParser()
        config.read(configFilename)
        if not config.has_section("ROOT"):
            config.add_section('ROOT')
        config.set('ROOT', option, str(info))
        with open(configFilename, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
        if debug:
            print(configFilename)
