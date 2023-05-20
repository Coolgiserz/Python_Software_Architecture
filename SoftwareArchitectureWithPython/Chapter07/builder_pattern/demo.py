"""
建造者模式:将对象的构造和组装过程分离
"""
class Life(object):
    def __init__(self, lucky, n_hobby, n_friend, n_fortune):
        self.n_hobby = n_hobby
        self.n_friend = n_friend
        self.n_fortune = n_fortune
        self.lucky = lucky
        self.hobbies = []
        self.friends = []
        self.fortures = []

    def __str__(self):
        return f"Life: {len(self.hobbies),len(self.friends),len(self.fortures)}"

class Hobby(object):
    def __init__(self, consume=10):
        self.consume = consume
    def __str__(self):
        return f"Hobby-<happiness: {self.consume}, consume:{self.consume}>"
class Friend(object):
    def __init__(self, consume=None, happiness=None):
        self.consume = consume
        self.happiness = happiness

    def __str__(self):
        return f"Friend-<happiness: {self.happiness}, consume:{self.consume}>"

class Fortune(object):
    def __init__(self, lucky=10):
        self.lucky = lucky
    def __str__(self):
        return f"Fortune-< consume:{self.lucky}>"
class LifeBuilder(object):
    def __init__(self, *args, **kwargs):
        self.life = Life(*args, **kwargs)

    def build(self):
        self.build_hobby()
        self.build_friend()
        self.build_fortune()

        return self.life

    def build_friend(self):
        for n in range(self.life.n_friend):
            self.life.friends.append(Friend())

    def build_hobby(self):
        for n in range(self.life.n_hobby):
            self.life.hobbies.append(Hobby())

    def build_fortune(self):
        for n in range(self.life.n_fortune):
            self.life.fortures.append(Fortune(lucky=self.life.lucky))

if __name__ == "__main__":
    lb = LifeBuilder(lucky=2,n_hobby=2, n_fortune=3,n_friend=4)
    life = lb.build()
    print(life)