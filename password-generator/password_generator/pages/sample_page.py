import rio

from .. import components as comps


class SamplePage(rio.Component):
    """
    The main page of the password generator
    """

    def build(self) -> rio.Component:
        return rio.Column(
            comps.Title(),
            comps.GenPlaceholder(),
            rio.Spacer(height=5),
            comps.Footer(),
            spacing=2,
            margin=2,
            align_x=0.5,
            align_y=0,
        )
