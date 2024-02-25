import os.path

from env_parsing import EnvParsing
from env_type.template import create_template


class EnvType:
    _FILE_NAME = "environment.d.ts"

    def __init__(self, path: str):
        self.path = path

    def create_env_ts(self, output_directory: str = "./"):
        envs = EnvParsing(self.path).parse()
        template = create_template(envs)
        path_to_output = os.path.join(output_directory, self._FILE_NAME)
        option = 'x' if not os.path.exists(path_to_output) else 'w'
        with open(path_to_output, option) as file:
            file.write(template)


class EmptyPathException(Exception):
    pass
