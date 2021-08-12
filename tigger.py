class _Tigger:
    _instance = None

    def _str_(self):
        return "I'm the only one!"
        
    def roar(self):
        return 'Grrr!'


def Tigger():
    if _Tigger._instance is None:
        _Tigger._instance = _Tigger()
    return _Tigger._instance