from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):

    def __init__(self):
        super().__init__()

        self.camera.setPos(-10, -20, 10)

        self.create_block(0, 10, 0)
        self.create_block(2, 10, 0)
        self.create_block(4, 10, 0)

        self.camera.lookAt(2, 10, 0)

    def create_block(self, x, y, z):

        block = loader.loadModel("models/box")

        block.reparentTo(render)

        block.setPos(x, y, z)

        block.setColor(0.2, 0.8, 0.2, 1)


game = Game()
game.run()