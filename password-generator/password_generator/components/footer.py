from datetime import datetime as dt
import rio

year = dt.now().year


class Footer(rio.Component):
    copyright: str = (f"© 2007 — {year} ООО «Роксис». "
                      + "Обслуживание компьютеров организаций "
                      + "в Зеленограде и Москве.")
    target_link: str = "https://www.roksis.ru/contacts/"
    adress: str = "Москва, Зеленоград, ул. Юности, д. 8, оф. 702-718"
    email: str = "info@roksis.ru"
    phone: str = "8 (495) 662-47-21"

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
