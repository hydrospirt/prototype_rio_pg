from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio

from .. import components as comps


class Options(rio.Component):
    is_on_lower: bool = True
    is_on_upper: bool = True
    is_on_nums: bool = True
    is_on_symbols: bool = False
    is_on_bad_symbol: bool = True

    def is_on_change_lower(self, event: rio.SwitchChangeEvent):
        self.is_on_lower = event.is_on

    def is_on_change_upper(self, event: rio.SwitchChangeEvent):
        self.is_on_upper = event.is_on

    def is_on_change_nums(self, event: rio.SwitchChangeEvent):
        self.is_on_nums = event.is_on

    def is_on_change_symbols(self, event: rio.SwitchChangeEvent):
        self.is_on_symbols = event.is_on

    def is_on_change_bad_symbol(self, event: rio.CheckboxChangeEvent):
        self.is_on_bad_symbol = event.is_on
        print(self.is_on_bad_symbol)

    def build(self) -> rio.Component:
        return rio.Grid(
            rio.Row(rio.Switch(is_on=self.is_on_lower,
                               on_change=self.is_on_change_lower),
                    rio.Text(text="a-z"),
                    rio.Switch(is_on=self.is_on_upper,
                               on_change=self.is_on_change_upper),
                    rio.Text(text="A-Z"),
                    rio.Switch(is_on=self.is_on_nums,
                               on_change=self.is_on_change_nums),
                    rio.Text(text="0-9"),
                    rio.Switch(is_on=self.is_on_symbols,
                               on_change=self.is_on_change_symbols),
                    rio.Text(text="!-)"),
                    ),
            rio.Row(rio.Checkbox(is_on=self.is_on_bad_symbol,
                                 on_change=self.is_on_change_bad_symbol),
                    rio.Text(text="Исключить символы l и I",
                    align_x=-0.001,
                    width=35)),
            column_spacing=0,
            row_spacing=2
        )
