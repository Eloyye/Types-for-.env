class TestEnvType:
    def test_single(self):
        path = "tests/data/single.env"
        env_type = EnvType(path)
        env_type.produce_