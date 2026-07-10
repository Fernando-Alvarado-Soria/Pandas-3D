from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight, WindowProperties

from panda3d_minecraft.camera_controller import CameraController
from panda3d_minecraft.map_manager import MapManager
from panda3d_minecraft.settings import (
    BACKGROUND_COLOR,
    CAMERA_FOV,
    DEFAULT_MAP,
    WINDOW_TITLE,
)


class Game(ShowBase):
    def __init__(self) -> None:
        super().__init__()

        self.configure_window()
        self.configure_lighting()
        self.configure_camera()

        self.map_manager = MapManager(
            loader=self.loader,
            render=self.render,
            map_path=DEFAULT_MAP,
        )

        self.map_manager.build_map()

        self.camera_controller = CameraController(
            camera=self.camera,
            task_manager=self.taskMgr,
        )

    def configure_window(self) -> None:
        self.setBackgroundColor(*BACKGROUND_COLOR)

        window_properties = WindowProperties()
        window_properties.setTitle(WINDOW_TITLE)
        self.win.requestProperties(window_properties)

    def configure_lighting(self) -> None:
        ambient_light = AmbientLight("ambient_light")
        ambient_light.setColor((0.65, 0.65, 0.65, 1))

        ambient_node = self.render.attachNewNode(ambient_light)
        self.render.setLight(ambient_node)

        directional_light = DirectionalLight("directional_light")
        directional_light.setColor((0.85, 0.85, 0.85, 1))

        directional_node = self.render.attachNewNode(directional_light)
        directional_node.setHpr(-30, -60, 0)

        self.render.setLight(directional_node)

    def configure_camera(self) -> None:
        self.camLens.setFov(CAMERA_FOV)

        self.camera.setPos(0, -22, 18)
        self.camera.lookAt(0, 0, 0)
