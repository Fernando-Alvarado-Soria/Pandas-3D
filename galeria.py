from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight


class Gallery3D(ShowBase):
    def __init__(self):
        super().__init__()

        # Fondo azul cielo
        self.setBackgroundColor(0.4, 0.7, 1)

        # Luz general
        light = AmbientLight("luz_general")
        light.setColor((1, 1, 1, 1))
        light_node = render.attachNewNode(light)
        render.setLight(light_node)

        # Piso
        self.floor = loader.loadModel("models/box")
        self.floor.reparentTo(render)
        self.floor.setScale(25, 20, 0.1)
        self.floor.setPos(0, 15, -2)
        self.floor.setColor(0.2, 0.8, 0.2, 1)

        # Objetos de la galería
        self.create_model("models/box", -10, 10, 0, 1, (1, 0, 0, 1))
        self.create_model("models/smiley", -5, 10, 0, 2, (1, 1, 1, 1))
        self.create_model("models/frowney", 0, 10, 0, 2, (1, 1, 1, 1))
        self.create_model("models/smiley", 5, 10, 0, 2, (1, 1, 1, 1))
        self.create_model("models/box", 10, 10, 0, 1, (0, 0, 1, 1))

        # Segunda fila
        self.create_model("models/box", -10, 20, 0, 1, (1, 1, 0, 1))
        self.create_model("models/smiley", -5, 20, 0, 2, (1, 1, 1, 1))
        self.create_model("models/frowney", 0, 20, 0, 2, (1, 1, 1, 1))
        self.create_model("models/smiley", 5, 20, 0, 2, (1, 1, 1, 1))
        self.create_model("models/box", 10, 20, 0, 1, (0.8, 0.2, 0.8, 1))

        # Cámara
        self.camera.setPos(0, -25, 10)
        self.camera.lookAt(0, 15, 0)

        # Campo de visión
        base.camLens.setFov(80)

    def create_model(self, model_name, x, y, z, scale, color):
        model = loader.loadModel(model_name)
        model.reparentTo(render)
        model.setPos(x, y, z)
        model.setScale(scale)
        model.setColor(color)


app = Gallery3D()
app.run()