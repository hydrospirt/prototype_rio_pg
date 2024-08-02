import rio


class Complexity(rio.Component):
    hex_color: str = "#ff0000"

    def build(self) -> rio.Component:
        return rio.Grid(
            rio.Row(rio.Text(text="Сложность:",
                             selectable=False,
                             style=rio.TextStyle(
                                font_weight="bold"
                             )),
                    rio.Banner(text="Пусто",
                               style="warning",
                               align_x=-0.3,
                               width=0.5),
                    rio.Icon(icon="material/encrypted:fill",
                             align_x=-0.5,
                             width=2,
                             height=2,
                             fill=rio.LinearGradientFill(
                                 (self.session.theme.secondary_color, 0),
                                 (self.session.theme.primary_color, 1),),),
                    rio.Text(text="Энтропия:",
                             selectable=False,
                             align_x=-0.8,
                             style=rio.TextStyle(
                                font_weight="bold")),
                    rio.Text(text="0 bits",
                             selectable=False,
                             align_x=-1.6,
                             style=rio.TextStyle(
                                font_weight="bold",
                                underlined=True,
                                fill=rio.Color.from_hex(self.hex_color)),)))
