import new
import original


Engine = new.NewEngine
# Engine = original.OriginalEngine


if __name__ == '__main__':
    engine = Engine()
    engine.game_turn()
