from time import sleep
import game
import view

FPS = 30
while game.is_active:
    events = view.get_events()
    game.level.player.do_actions(events)
    game.timer.do_actions()
    game.level.ghosts.do_actions()
    view.render(game.level)
    sleep(1 / FPS)
