class Cliente:
    def __init__(self, titular):
        self._titular = titular

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def nome(self,titular):
        self._titular = titular
