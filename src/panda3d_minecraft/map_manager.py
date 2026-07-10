from panda3d.core import NodePath

from panda3d_minecraft.block import Block
from panda3d_minecraft.utils.file_reader import read_map


class MapManager:
    def __init__(self, loader, render: NodePath, map_path) -> None:
        self.loader = loader
        self.render = render
        self.map_path = map_path

        self.root = render.attachNewNode("World")
        self.blocks: list[Block] = []

    def build_map(self) -> None:
        map_data = read_map(self.map_path)

        rows = len(map_data)
        columns = len(map_data[0])

        offset_x = columns / 2
        offset_y = rows / 2

        for row_index, row in enumerate(map_data):
            for column_index, height in enumerate(row):
                if height == 0:
                    continue

                for z in range(height):
                    block_type = self.get_block_type(z, height)

                    position = (
                        column_index - offset_x,
                        row_index - offset_y,
                        z,
                    )

                    block = Block(
                        loader=self.loader,
                        parent=self.root,
                        block_type=block_type,
                        position=position,
                    )

                    self.blocks.append(block)

    def get_block_type(self, z: int, height: int) -> int:
        if z == height - 1:
            return 1  # Pasto en la superficie

        if z >= height - 3:
            return 2  # Tierra cerca de la superficie

        return 3  # Piedra en las capas profundas
