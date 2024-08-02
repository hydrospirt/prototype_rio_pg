import rio


class Complexity(rio.Component):

    def build(self) -> rio.Component:
        return rio.Grid(
            rio.Row(rio.Text(text='Сложность:',
                             selectable=False,
                             style=rio.TextStyle(
                                font_weight="bold"
                             )),
                    rio.Banner(text='Пусто',
                               style='info'),
                    rio.Text(text='Энтропия:',
                             selectable=False),
                    rio.Icon(icon='material/encrypted:fill',
                             fill=rio.LinearGradientFill(
                                 (self.session.theme.secondary_color, 0),
                                 (self.session.theme.primary_color, 1),),),))
