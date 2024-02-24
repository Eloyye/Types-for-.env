import os

from env_parsing import EnvParsing, insert_entry


class TestEnvParsing:

    def test_two_words(self):
        file_path = "data/two_words.env"
        file_path = os.path.join("tests", file_path)
        env_parsing = EnvParsing(file_path).parse()
        expect = {"TWO_WORDS": "hello world"}
        assert_not_empty(env_parsing)
        for key, value in env_parsing.items():
            if key not in expect:
                assert False
            assert expect[key] == value

    def test_equal_in_value(self):
        file_path = "data/equal_in_value.env"
        file_path = os.path.join("tests", file_path)
        env_parsing = EnvParsing(file_path).parse()
        expect = {"MULT": "equal sign ="}
        assert_not_empty(env_parsing)
        if len(env_parsing) != 1:
            assert False
        for key, value in env_parsing.items():
            if key not in expect:
                assert False
            assert expect[key] == value

    def test_empty(self):
        file_path = "data/empty.env"
        file_path = os.path.join("tests", file_path)

        env_parsing = EnvParsing(file_path).parse()
        expect = {"EMPTY": ""}
        assert_not_empty(env_parsing)
        for key, value in env_parsing.items():
            if key not in expect:
                assert False
            assert expect[key] == value

    def test_single(self):
        file_path = "data/single.env"
        file_path = os.path.join("tests", file_path)

        env_parsing = EnvParsing(file_path).parse()
        expect = {"START": "hello"}
        assert_not_empty(env_parsing)
        for key, value in env_parsing.items():
            if key not in expect:
                assert False
            assert expect[key] == value

    def test_three_lines(self):
        file_path = "data/three_lines.env"
        file_path = os.path.join("tests", file_path)

        env_parsing = EnvParsing(file_path).parse()
        expect = {"START": "hello", "EMPTY": "", "TWO_WORDS": "hello world"}
        assert_not_empty(env_parsing)
        for key, value in env_parsing.items():
            if key not in expect:
                assert False
            assert expect[key] == value


class TestInsertEntry:
    def test_single_line(self):
        line = "GREETING=hello"
        key, value = insert_entry(line)
        assert key == "GREETING"
        assert value == "hello"


def assert_not_empty(env_parsing):
    if not env_parsing:
        assert False, f"expected to not be empty but got {env_parsing}"
