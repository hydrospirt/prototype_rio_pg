from datetime import datetime as dt
import rio

year = dt.now().year


class Footer(rio.Component):
    copyright: str = (f"© {year} made with Rio framework")
    target_link: str = ""
    adress: str = "Your adress"
    email: str = "info@info.com"
    phone: str = "+00 0 000000000"

    def build(self) -> rio.Component:
        return rio.Grid(
            rio.Text(self.copyright),
            rio.Row(
                rio.Link(content=self.phone,
                         target_url=self.target_link),
                rio.Link(content=self.email,
                         target_url=self.target_link),
                rio.Link(content=self.adress, target_url=self.target_link),),
            row_spacing=0.5,
        )
