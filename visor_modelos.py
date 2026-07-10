from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight


class GaleriaBasica(ShowBase):
    def __init__(self):
        super().__init__()

        self.setBackgroundColor(0.5, 0.8, 1)

        luz = AmbientLight("luz")
        luz.setColor((1, 1, 1, 1))
        render.setLight(render.attachNewNode(luz))

        self.crear_piso()

        self.crear_modelo("models/box", -6, 10, 0, 1, (1, 0, 0, 1))
        self.crear_modelo("models/smiley", 0, 10, 0, 2, (1, 1, 1, 1))
        self.crear_modelo("models/frowney", 6, 10, 0, 2, (1, 1, 1, 1))

        self.camera.setPos(0, -20, 8)
        self.camera.lookAt(0, 10, 0)

    def crear_piso(self):
        piso = loader.loadModel("models/box")
        piso.reparentTo(render)
        piso.setScale(18, 12, 0.1)
        piso.setPos(0, 10, -1)
        piso.setColor(0.2, 0.7, 0.3, 1)

    def crear_modelo(self, ruta, x, y, z, escala, color):
        modelo = loader.loadModel(ruta)
        modelo.reparentTo(render)
        modelo.setPos(x, y, z)
        modelo.setScale(escala)
        modelo.setColor(color)


app = GaleriaBasica()
app.run()