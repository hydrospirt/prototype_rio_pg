from datetime import datetime as dt

year = dt.now().year


class FooterSettings:
    COPYRIGHT = f"© {year} made with Rio framework in Russia/Zelenograd"
    TR_LINK = "https://rio.dev/docs"
    ADRESS = "Your adress"
    EMAIL = "youremail@info.com"
    PHONE = "+00 0 000000000"


class HeaderSettings:
    TITLE = "Password Generator"
    SUB_TITLE = "Protect your access"


class GenPalaceholderSettings:
    LABEL = "Password Generator"
    ENTROPY = "Entropy:"
    COMPLEXITY = "Complexity:"
    MOB_GENBTN = "Let's gen"
    MOB_COPYBTN = "Copy"


OPTIONS_TEXT = "Exclude the characters l and I"


class MainPageSettings:
    """
    The settings for the main page that you would like to change

    `DESCRIPTION`: A short, human-readable description of the app. This can
    show up in search engines, social media sites and similar.

    `META_TAGS`: Arbitrary key-value pairs that will be included in the HTML
        header of the app. These are used by search engines and social media
        sites to display information about your page, such as the title and a
        short description.
    """

    DESCRIPTION = ("A Rio web-app written in 100% Python. "
                   + "Generate strong passwords using this application")
    META_TAGS = {"title": "Password Generator",
                 "description": "Best site on Rio web-app"}
