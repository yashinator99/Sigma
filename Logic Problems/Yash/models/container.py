class Scamp:

    def __init__(self, contents, name):
        self.contents = contents
        self.name = name

    def __repr__(self):
        return f"Scamp {self.name}: contents - {self.contents}"