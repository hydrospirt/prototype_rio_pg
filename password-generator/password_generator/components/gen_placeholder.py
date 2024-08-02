import rio

from .. import components as comps
from ..utils import create_new_password


class GenPlaceholder(rio.Component):
    label: str = "Генератор паролей"
    value: float = 0
    text: str = ""

    def on_change_slider(self, event: rio.SliderChangeEvent):
        self.value = event.value
        print(f"value slider: {self.value}")
        return self.value

    def on_change_num(self, event: rio.NumberInputChangeEvent):
        self.value = event.value
        print(f"value inputnum: {self.value}")
        return self.value

    def _on_press(self):
        self.text = create_new_password(self.value, "gdlfl;slf")
        return self.text

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Row(
                rio.TextInput(
                    label=self.label,
                    width=35,
                    text=create_new_password(self.value, "gdlfl;slf"),),
                rio.IconButton(icon="material/install_desktop",
                               on_press=self._on_press),
                rio.IconButton(icon="material/content_copy",
                               style="minor"),
                spacing=1),
            rio.Row(rio.Slider(
                    value=self.value,
                    minimum=0,
                    maximum=128,
                    step=1,
                    show_values=True,
                    width=32,
                    on_change=self.on_change_slider),
                    rio.NumberInput(value=self.value,
                                    label="Длина",
                                    decimals=0,
                                    minimum=0,
                                    maximum=128,
                                    width=1,
                                    on_change=self.on_change_num),),
            comps.Complexity(),
            comps.Options(),
            spacing=2,)
