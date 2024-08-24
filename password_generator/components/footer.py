import rio
from pathlib import Path
from ..utils import FooterSettings


class Footer(rio.Component):
    copyright: str = FooterSettings.COPYRIGHT
    target_link: str = FooterSettings.TR_LINK
    adress: str = FooterSettings.ADRESS
    email: str = FooterSettings.EMAIL
    phone: str = FooterSettings.PHONE

    def build(self) -> rio.Component:
        GRAD = rio.LinearGradientFill((self.session.theme.secondary_color, 0),
                                      (self.session.theme.primary_color, 1),)
        return rio.Card(
                rio.Grid(
                    rio.Rectangle(content=rio.Grid(
                        rio.Row(rio.Spacer(),
                                rio.Card(rio.Row(
                                    rio.Icon(
                                        'material/phone_forwarded',
                                        width=0.2,
                                        height=0.2,
                                        fill=GRAD
                                    ),
                                    rio.Column(
                                        rio.Text("Call Me",
                                                 style=rio.TextStyle(
                                                     font_size=1,
                                                     font_weight="bold",
                                                 )),
                                        rio.Link(content=self.phone,
                                                 target_url=self.target_link,),),
                                proportions=[1, 5],),
                                corner_radius=(1, 1, 1, 1),
                                height=2,
                                colorize_on_hover=True,
                                color=rio.Color.from_hex("#11292B"),),
                                proportions=[1, 1],
                                margin_right=7,),
                        rio.Row(rio.Spacer(),
                                rio.Card(rio.Row(
                                    rio.Icon("material/mail",
                                        width=0.2,
                                        height=0.2,
                                        fill=GRAD),
                                    rio.Column(
                                        rio.Text("Write Me",
                                                 style=rio.TextStyle(
                                                     font_size=1,
                                                     font_weight="bold",
                                                 )),
                                        rio.Link(content=self.email,
                                                 target_url=self.target_link),),
                                proportions=[1, 5]
                                ),
                                corner_radius=(1, 1, 1, 1),
                                height=2,
                                colorize_on_hover=True,
                                color=rio.Color.from_hex("#11292B"),),
                                proportions=[1, 1],
                                margin_right=7,),
                        rio.Row(rio.Spacer(),
                                rio.Card(rio.Row(
                                    rio.Icon(
                                        'material/location_city',
                                        width=0.2,
                                        height=0.2,
                                        fill=GRAD
                                    ),
                                    rio.Column(
                                        rio.Text("Find Me",
                                                 style=rio.TextStyle(
                                                     font_size=1,
                                                     font_weight="bold",
                                                 )),
                                        rio.Link(content=self.adress,
                                                 target_url=self.target_link),),
                                    proportions=[1, 4.5]
                                    ),
                                corner_radius=(1, 1, 1, 1),
                                height=2,
                                colorize_on_hover=True,
                                color=rio.Color.from_hex("#11292B"),),
                                proportions=[1, 1],
                                margin_right=7,),
                        row_spacing=1,
                        margin_bottom=1,
                        margin_top=1,
                        ),
                        fill=rio.ImageFill(Path(
                            self.session.assets / "fun-footer.jpeg"),
                            fill_mode="zoom",),
                        corner_radius=(0, 0, 10, 0),),
                    rio.Separator(margin_right=5),
                    rio.Text(self.copyright,
                            margin_left=1,
                            style=rio.TextStyle(
                                italic=True,
                                fill=rio.LinearGradientFill(
                                    (self.session.theme.secondary_color, 0),
                                    (self.session.theme.primary_color, 1),),),),
                    row_spacing=0.5,
                    margin=1,
                ),
                color=rio.Color.from_hex("#0A1819"),
                corner_radius=(0, 0, 10, 0)
            )
