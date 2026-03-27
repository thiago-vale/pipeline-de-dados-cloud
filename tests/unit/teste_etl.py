from utils.base_etl import Base


class FakeETL(Base):
    def extract(self):
        return {}

    def transform(self, data_sources):
        return None

    def load(self, df):
        pass


def test_fake_etl_implements_base():
    """
    Verifica se uma classe concreta baseada em Base funciona
    """
    etl = FakeETL()

    assert etl is not None