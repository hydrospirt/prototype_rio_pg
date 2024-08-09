from __future__ import annotations

from dataclasses import dataclass

import rio

from ..utils import Symbols, delete_bad_symbols, delete_symbols, OPTIONS_TEXT


@dataclass
class GlobalOptions:
    is_on_lower: bool = True
    is_on_upper: bool = True
    is_on_nums: bool = True
    is_on_symbols: bool = False
    is_on_bad_symbol: bool = True
    symbols: str = ""


class Options(rio.Component):
    text: str = OPTIONS_TEXT

    def __post_init__(self):
        if GlobalOptions.is_on_lower:
            if (Symbols.LOWERCASE not in GlobalOptions.symbols
                    and Symbols.CLEAR_LOWERCASE not in GlobalOptions.symbols):
                GlobalOptions.symbols += Symbols.LOWERCASE
        if GlobalOptions.is_on_upper:
            if (Symbols.UPPERCASE not in GlobalOptions.symbols
                    and Symbols.CLEAR_UPPERCASE not in GlobalOptions.symbols):
                GlobalOptions.symbols += Symbols.UPPERCASE
        if GlobalOptions.is_on_nums:
            if Symbols.DIGITS not in GlobalOptions.symbols:
                GlobalOptions.symbols += Symbols.DIGITS
        if GlobalOptions.is_on_symbols:
            if Symbols.PUNCTUATION not in GlobalOptions.symbols:
                GlobalOptions.symbols += Symbols.PUNCTUATION
        if GlobalOptions.is_on_bad_symbol:
            GlobalOptions.symbols = delete_bad_symbols(GlobalOptions.symbols)

    def is_on_change_lower(self, event: rio.SwitchChangeEvent):
        GlobalOptions.is_on_lower = event.is_on
        if GlobalOptions.is_on_lower:
            GlobalOptions.symbols += Symbols.LOWERCASE
            return GlobalOptions.symbols
        else:
            GlobalOptions.symbols = delete_symbols(GlobalOptions.symbols,
                                                   Symbols.LOWERCASE)
            return GlobalOptions.symbols

    def is_on_change_upper(self, event: rio.SwitchChangeEvent):
        GlobalOptions.is_on_upper = event.is_on
        if GlobalOptions.is_on_upper:
            GlobalOptions.symbols += Symbols.UPPERCASE
            return GlobalOptions.symbols
        else:
            GlobalOptions.symbols = delete_symbols(GlobalOptions.symbols,
                                                   Symbols.UPPERCASE)
            return GlobalOptions.symbols

    def is_on_change_nums(self, event: rio.SwitchChangeEvent):
        GlobalOptions.is_on_nums = event.is_on
        if GlobalOptions.is_on_nums:
            GlobalOptions.symbols += Symbols.DIGITS
            return GlobalOptions.symbols
        else:
            GlobalOptions.symbols = delete_symbols(GlobalOptions.symbols,
                                                   Symbols.DIGITS)
            return GlobalOptions.symbols

    def is_on_change_symbols(self, event: rio.SwitchChangeEvent):
        GlobalOptions.is_on_symbols = event.is_on
        if GlobalOptions.is_on_symbols:
            GlobalOptions.symbols += Symbols.PUNCTUATION
            return GlobalOptions.symbols
        else:
            GlobalOptions.symbols = delete_symbols(GlobalOptions.symbols,
                                                   Symbols.PUNCTUATION)
            return GlobalOptions.symbols

    def is_on_change_bad_symbol(self, event: rio.CheckboxChangeEvent):
        GlobalOptions.is_on_bad_symbol = event.is_on
        if GlobalOptions.is_on_bad_symbol or len(GlobalOptions.symbols) == 10:
            GlobalOptions.symbols = delete_bad_symbols(GlobalOptions.symbols)
            return GlobalOptions.symbols
        else:
            GlobalOptions.symbols += Symbols.BAD_SYMBOLS

    def build(self) -> rio.Component:
        return rio.Grid(
            rio.Row(rio.Switch(is_on=GlobalOptions.is_on_lower,
                               on_change=self.is_on_change_lower),
                    rio.Text(text="a-z"),
                    rio.Switch(is_on=GlobalOptions.is_on_upper,
                               on_change=self.is_on_change_upper),
                    rio.Text(text="A-Z"),
                    rio.Switch(is_on=GlobalOptions.is_on_nums,
                               on_change=self.is_on_change_nums),
                    rio.Text(text="0-9"),
                    rio.Switch(is_on=GlobalOptions.is_on_symbols,
                               on_change=self.is_on_change_symbols),
                    rio.Text(text="!-)"),
                    ),
            rio.Row(rio.Checkbox(is_on=GlobalOptions.is_on_bad_symbol,
                                 on_change=self.is_on_change_bad_symbol),
                    rio.Text(text=self.text,
                    align_x=-0.001,
                    width=35)),
            column_spacing=0,
            row_spacing=2
        )
