A copy & paste backport of Python 3.3's ``shutil.which`` function.

Usage
=====

* Install this package: ``pip install shutilwhich``
* Import like this: ``import shutilwhich``. This will monkeypatch ``shutil``
  if there is no ``shutil.which`` method, otherwise leave it alone.
