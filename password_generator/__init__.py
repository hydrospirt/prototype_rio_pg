from __future__ import annotations

from pathlib import Path
from typing import *  # type: ignore

import rio

from . import pages
from . import components as comps

from .utils import MainPageSettings

# Define a theme for Rio to use.
#
# You can modify the colors here to adapt the appearance of your app or website.
# The most important parameters are listed, but more are available! You can find
# them all in the docs
#
# https://rio.dev/docs/api/theme
theme = rio.Theme.from_colors(
    primary_color=rio.Color.from_hex("01dffdff"),
    secondary_color=rio.Color.from_hex("0083ffff"),
    mode="dark",
)


# Create the Rio app
app = rio.App(
    name="password_generator",
    pages=[
        rio.Page(
            name="Home",
            page_url="",
            build=pages.MainPage,
        ),
    ],
    theme=theme,
    assets_dir=Path(__file__).parent / "assets",
    description=MainPageSettings.DESCRIPTION,
    meta_tags=MainPageSettings.META_TAGS
)
