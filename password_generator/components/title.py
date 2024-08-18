import rio
from ..utils import HeaderSettings


class Title(rio.Component):
    title: str = HeaderSettings.TITLE
    subtitle: str = HeaderSettings.SUB_TITLE

    def build(self) -> rio.Component:
        return rio.Card(
            rio.Column(
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
                    margin_bottom=1,
                    style=rio.TextStyle(
                        font_size=1,
                        italic=True,
                        fill=rio.LinearGradientFill(
                            (self.session.theme.secondary_color, 0),
                            (self.session.theme.primary_color, 1),),),
                ),
            ),
            color=rio.Color.from_hex("#0A1819"),
            corner_radius=(10, 0, 0, 0)
        )
