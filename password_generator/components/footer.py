import rio
from ..utils import FooterSettings


class Footer(rio.Component):
    copyright: str = FooterSettings.COPYRIGHT
    target_link: str = FooterSettings.TR_LINK
    adress: str = FooterSettings.ADRESS
    email: str = FooterSettings.EMAIL
    phone: str = FooterSettings.PHONE

    def build(self) -> rio.Component:
        return rio.Card(
            rio.Grid(
                rio.Text(self.copyright),
                rio.Row(
                    rio.Link(content=self.phone,
                             target_url=self.target_link),
                    rio.Link(content=self.email,
                             target_url=self.target_link),
                    rio.Link(content=self.adress,
                             target_url=self.target_link),),
                row_spacing=0.5,
                margin=1,
            ),
            color=rio.Color.from_hex("#0A1819"),
            corner_radius=(0, 0, 10, 0)
        )
