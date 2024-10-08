import rio
from pathlib import Path
from .. import components as comps


class MainPage(rio.Component):
    """
    The main page of the password generator
    """

    def build(self) -> rio.Component:
        return rio.Rectangle(
            content=rio.Column(
                comps.Title(),
                comps.GenPlaceholder(),
                comps.Footer(),
                margin=2,
                align_x=0.5,
                align_y=0,
            ),
            fill=rio.ImageFill(
                Path(self.session.assets / "fun-footer.jpeg"),
                fill_mode="fit"
            ),
        )
