import os
from typing import Dict


def strip_end_line(value):
    if value[-1] == '\n':
        return value[:len(value) - 1]
    return value


def filter_text(value: str):
    value = strip_end_line(value)
    value = strip_quotes(value)
    return value


def insert_entry(line: str):
    key, value = line.split('=', 1)
    value = filter_text(value) if value else ""
    return key, value


def strip_quotes(value):
    if len(value) > 1 and (value[0] == "\"" and value[-1] == "\"" or value[0] == "\'" and value[-1] == "\'"):
        value = value[1:len(value) - 1]
    return value


class EnvParsing:
    def __init__(self, path=".env"):
        self.path = path
        self.env = {}

    def parse(self) -> Dict[str, str]:
        env = {}
        print(f"current working directory: {os.getcwd()}")
        with open(self.path) as file:
            for line in file:
                if not line or (len(line) == 1 and line[0] == '\n'):
                    continue
                key, value = insert_entry(line)
                env[key] = value
        self.env = env
        return self.env
