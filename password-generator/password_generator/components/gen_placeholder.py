import rio
from typing import Literal
from .. import components as comps
from ..utils import create_new_password, get_password_entropy


class GenPlaceholder(rio.Component):
    label: str = "Генератор паролей"
    value: float = 8
    text: str = ""
    hex_color: Literal["#ff0000", "#ffd966", "#93c47d", "#00ff00"] = "#ff0000"
    bits: str = "0"
    banner_text: Literal["Пусто", "Жалкий", "Слабый",
                         "Хороший", "Сильный", "Превосходный"] = "Пусто"
    banner_style: Literal["success", "danger", "info", "warning"] = "warning"

    def change_banner_text(self):
        bits = float(self.bits)
        if bits == 0:
            self.banner_text = "Пусто"
        elif bits == 1 and bits <= 30:
            self.banner_text = "Жалкий"
            self.banner_style = "danger"
        elif bits > 30 and bits <= 50:
            self.banner_text = "Слабый"
            self.banner_style = "danger"
            self.hex_color = "#ff0000"
        elif bits > 50 and bits <= 70:
            self.banner_text = "Хороший"
            self.banner_style = "warning"
            self.hex_color = "#ffd966"
        elif bits > 70 and bits <= 120:
            self.banner_text = "Сильный"
            self.banner_style = "success"
            self.hex_color = "#93c47d"
        elif bits > 120:
            self.banner_text = "Превосходный"
            self.banner_style = "success"
            self.hex_color = "#00ff00"

    def on_change_slider(self, event: rio.SliderChangeEvent):
        self.value = event.value
        self.text = create_new_password(self.value,
                                        comps.GlobalOptions.symbols)
        print(f"value slider: {self.value}")
        return self.value

    def on_change_num(self, event: rio.NumberInputChangeEvent):
        self.value = event.value
        self.text = create_new_password(self.value,
                                        comps.GlobalOptions.symbols)
        print(f"value inputnum: {self.value}")
        return self.value

    async def _on_press(self):
        print(comps.GlobalOptions.symbols)
        self.text = create_new_password(self.value, comps.GlobalOptions.symbols)
        self.bits = str(get_password_entropy(len(self.text), len(comps.GlobalOptions.symbols)))
        self.change_banner_text()
        return self.text

    async def get_to_clip(self):
        print(self.text)
        await self.session.set_clipboard(self.text)

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Row(
                rio.TextInput(
                    label=self.label,
                    width=35,
                    text=self.bind().text,),
                rio.IconButton(icon="material/install_desktop",
                               on_press=self._on_press),
                rio.IconButton(icon="material/content_copy",
                               style="minor",
                               on_press=self.get_to_clip),
                spacing=1),
            rio.Row(rio.Slider(
                    value=self.value,
                    minimum=8,
                    maximum=128,
                    step=1,
                    show_values=True,
                    width=32,
                    on_change=self.on_change_slider),
                    rio.NumberInput(value=self.value,
                                    label="Длина",
                                    decimals=0,
                                    minimum=8,
                                    maximum=128,
                                    width=1,
                                    on_change=self.on_change_num),),
            rio.Row(rio.Text(text="Сложность:",
                             selectable=False,
                             style=rio.TextStyle(
                                font_weight="bold"
                             )),
                    rio.Banner(text=self.bind().banner_text,
                               style=self.bind().banner_style,
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
                    rio.Text(text=self.bind().bits,
                             selectable=False,
                             align_x=-1.6,
                             style=rio.TextStyle(
                                font_weight="bold",
                                underlined=True,
                                fill=rio.Color.from_hex(self.hex_color)),)),
            comps.Options(),
            spacing=2,)
