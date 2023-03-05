import os
import sys
if __name__ == '__main__':
    args = sys.argv
    config_file_name = 'dev.toml'
    if len(args) >= 2 and args[1] is not None:
        config_file_name = str(args[1]) + ".toml"

    os.environ["INCLUDES_FOR_DYNACONF"] = "['{}']".format(config_file_name)
