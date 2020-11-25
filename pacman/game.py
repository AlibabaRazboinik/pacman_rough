"""
    Игра (таймеры, появление итемов (еда)),
"""


class Game:
    def __init__(self, is_active=False, level=0, timer=360):
        self.is_active = is_active
        self.level = level
        self.timer = timer
