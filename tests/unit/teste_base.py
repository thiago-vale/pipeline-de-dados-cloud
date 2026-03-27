from utils.base_etl import Base


def test_base_is_abstract():
    """
    Verifica se Base é abstrata e não pode ser instanciada
    """
    try:
        Base()
        assert False, "Base não deveria ser instanciável"
    except TypeError:
        assert True


def test_base_has_required_methods():
    """
    Verifica se os métodos obrigatórios existem
    """
    methods = ["extract", "transform", "load"]

    for method in methods:
        assert hasattr(Base, method)