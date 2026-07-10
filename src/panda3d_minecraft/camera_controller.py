from direct.showbase.DirectObject import DirectObject
from direct.task import Task


class CameraController(DirectObject):
    def __init__(self, camera, task_manager, speed: float = 8.0) -> None:
        super().__init__()

        self.camera = camera
        self.task_manager = task_manager
        self.speed = speed

        self.keys = {
            "w": False,
            "s": False,
            "a": False,
            "d": False,
            "q": False,
            "e": False,
        }

        for key in self.keys:
            self.accept(key, self.set_key, [key, True])
            self.accept(f"{key}-up", self.set_key, [key, False])

        self.task_manager.add(self.update, "camera_movement")

    def set_key(self, key: str, value: bool) -> None:
        self.keys[key] = value

    def update(self, task: Task):
        dt = globalClock.getDt()
        movement = self.speed * dt

        if self.keys["w"]:
            self.camera.setY(self.camera, movement)

        if self.keys["s"]:
            self.camera.setY(self.camera, -movement)

        if self.keys["a"]:
            self.camera.setX(self.camera, -movement)

        if self.keys["d"]:
            self.camera.setX(self.camera, movement)

        if self.keys["q"]:
            self.camera.setZ(self.camera.getZ() + movement)

        if self.keys["e"]:
            self.camera.setZ(self.camera.getZ() - movement)

        return task.cont
