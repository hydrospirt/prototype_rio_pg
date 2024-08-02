import rio


class Title(rio.Component):
    title: str = "Роксис"
    subtitle: str = "Информационные системы"

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Text(
                self.title,
                justify="center",
                style=rio.TextStyle(
                    font_size=5,
                    italic=True,
                    font_weight="bold",
                    fill=rio.LinearGradientFill(
                        (self.session.theme.secondary_color, 0),
                        (self.session.theme.primary_color, 1),
                    ),
                ),),
            rio.Text(
                self.subtitle,
                justify="center",
                style=rio.TextStyle(
                     font_size=1,
                     italic=True,
                     fill=rio.LinearGradientFill(
                        (self.session.theme.secondary_color, 0),
                        (self.session.theme.primary_color, 1),),),
            ),
        )
