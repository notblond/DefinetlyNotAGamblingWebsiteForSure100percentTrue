def test_imports():
    import importlib
    importlib.import_module('src.games.slots')
    importlib.import_module('src.games.roulette')
    assert True
