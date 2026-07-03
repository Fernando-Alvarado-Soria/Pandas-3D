from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight
from gltf._loader import GltfLoader
from panda3d.core import LoaderFileTypeRegistry


class VisorModelos(ShowBase):
    def __init__(self):
        super().__init__()

        self.setBackgroundColor(0.4, 0.7, 1)

        luz_ambiente = AmbientLight("luz_ambiente")
        luz_ambiente.setColor((0.7, 0.7, 0.7, 1))
        nodo_luz = render.attachNewNode(luz_ambiente)
        render.setLight(nodo_luz)

        luz_direccional = DirectionalLight("luz_direccional")
        luz_direccional.setColor((1, 1, 1, 1))
        nodo_direccional = render.attachNewNode(luz_direccional)
        nodo_direccional.setHpr(45, -45, 0)
        render.setLight(nodo_direccional)

        self.crear_piso()

        # Registrar el cargador de archivos glTF/GLB
        LoaderFileTypeRegistry.get_global_ptr().register_type(GltfLoader())

        self.modelo = loader.loadModel("assets/personajes/01_robot.glb")
        self.modelo.reparentTo(render)
        self.modelo.setPos(0, 10, 0)
        self.modelo.setScale(1)

        self.camera.setPos(0, -15, 6)
        self.camera.lookAt(self.modelo)

    def crear_piso(self):
        piso = loader.loadModel("models/box")
        piso.reparentTo(render)
        piso.setScale(20, 20, 0.1)
        piso.setPos(0, 10, -1)
        piso.setColor(0.2, 0.8, 0.2, 1)


app = VisorModelos()
app.run()