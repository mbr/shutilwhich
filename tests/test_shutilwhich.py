def test_monkeypatch():
    import shutilwhich
    import shutil

    assert callable(shutil.which)


def test_import():
    from shutilwhich import which

    assert callable(which)


def test_same_as_stock():
    from shutilwhich import which
    import shutil

    assert shutil.which == which
