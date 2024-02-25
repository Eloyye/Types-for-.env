from typing import Dict

template_first = "declare global{\n\tnamespace NodeJS {\n\t\tinterface ProcessEnv {\n"
template_second = "\t\t}\n\t}\n}\n\nexport {};"


def create_template(dictionary: Dict[str, str]) -> str:
    res = ""
    for key, val in dictionary.items():
        option = "" if val else "?"
        res += f'\t\t\t{key}{option}: string;\n'
    return template_first + res + template_second


if __name__ == '__main__':
    dic = {"OPENAI": "1234", "KEY2": "457", "NULLTYPE": ""}
    print(create_template(dic))
