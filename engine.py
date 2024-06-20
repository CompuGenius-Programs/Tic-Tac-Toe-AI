import new
import original


Engine = new.NewEngine
OriginalEngine = original.OriginalEngine


if __name__ == '__main__':
    engine = Engine()
    engine.playing_as = 'X'
    engine.game_turn()
