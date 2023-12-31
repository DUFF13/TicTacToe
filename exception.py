

class InvalidMoveError(Exception):
    """Jouer sur une case déjà jouée est impossible"""
    def __init__(self, message = "Choix de case impossible") -> None:
        self.message = message
        super().__init__(self.message)
