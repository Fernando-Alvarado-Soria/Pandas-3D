from panda3d.core import NodePath


BLOCK_COLORS = {
    1: (0.20, 0.75, 0.20, 1),  # Pasto
    2: (0.45, 0.25, 0.10, 1),  # Tierra
    3: (0.50, 0.50, 0.50, 1),  # Piedra
    4: (0.10, 0.40, 0.90, 1),  # Agua
    5: (0.55, 0.35, 0.15, 1),  # Madera
    6: (0.90, 0.80, 0.50, 1),  # Arena
    7: (0.70, 0.15, 0.10, 1),  # Ladrillo
    8: (1.00, 0.80, 0.05, 1),  # Oro
    9: (0.20, 0.90, 0.90, 1),  # Diamante
}


class Block:
    def __init__(
        self,
        loader,
        parent: NodePath,
        block_type: int,
        position: tuple[int, int, int],
    ) -> None:
        self.node = loader.loadModel("models/box")
        self.node.reparentTo(parent)
        self.node.setPos(*position)
        self.node.setScale(1)

        color = BLOCK_COLORS.get(block_type, (1, 1, 1, 1))
        self.node.setColor(color)
