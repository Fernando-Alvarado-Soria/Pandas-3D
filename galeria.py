from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight


class GaleriaInteractiva(ShowBase):
    def __init__(self):
        super().__init__()

        self.setBackgroundColor(0.5, 0.8, 1)
        self.velocidad = 10

        self.teclas = {
            "w": False,
            "s": False,
            "a": False,
            "d": False,
            "q": False,
            "e": False
        }

        luz = AmbientLight("luz")
        luz.setColor((1, 1, 1, 1))
        render.setLight(render.attachNewNode(luz))

        self.crear_piso()

        self.crear_modelo("models/box", -10, 15, 0, 1, (1, 0, 0, 1))
        self.crear_modelo("models/smiley", 0, 15, 0, 0.8, (1, 1, 1, 1))
        self.crear_modelo("models/frowney", 10, 15, 0, 0.8, (1, 1, 1, 1))

        self.camera.setPos(0, -10, 5)
        self.camera.lookAt(0, 15, 0)

        for tecla in self.teclas:
            self.accept(tecla, self.actualizar_tecla, [tecla, True])
            self.accept(tecla + "-up", self.actualizar_tecla, [tecla, False])

        self.taskMgr.add(self.actualizar_movimiento, "actualizar_movimiento")

    def crear_piso(self):
        piso = loader.loadModel("models/box")
        piso.reparentTo(render)
        piso.setScale(25, 25, 0.1)
        piso.setPos(0, 20, -1)
        piso.setColor(0.2, 0.7, 0.3, 1)

    def crear_modelo(self, ruta, x, y, z, escala, color):
        modelo = loader.loadModel(ruta)
        modelo.reparentTo(render)
        modelo.setPos(x, y, z)
        modelo.setScale(escala)
        modelo.setColor(color)

    def actualizar_tecla(self, tecla, estado):
        self.teclas[tecla] = estado

    def actualizar_movimiento(self, task):
        dt = globalClock.getDt()

        if self.teclas["w"]:
            self.camera.setY(self.camera.getY() + self.velocidad * dt)
        if self.teclas["s"]:
            self.camera.setY(self.camera.getY() - self.velocidad * dt)
        if self.teclas["a"]:
            self.camera.setX(self.camera.getX() - self.velocidad * dt)
        if self.teclas["d"]:
            self.camera.setX(self.camera.getX() + self.velocidad * dt)
        if self.teclas["q"]:
            self.camera.setZ(self.camera.getZ() + self.velocidad * dt)
        if self.teclas["e"]:
            self.camera.setZ(self.camera.getZ() - self.velocidad * dt)

        return task.cont


app = GaleriaInteractiva()
app.run()