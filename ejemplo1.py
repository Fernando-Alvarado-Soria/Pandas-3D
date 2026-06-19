from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):
    def __init__(self):
        super().__init__()

        self.model = loader.loadModel("models/environment")
        self.model.reparentTo(render)

        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)

        self.camera.setPos(0, -50, 10)

        self.camLens.setFov(90)


game = Game()
game.run()