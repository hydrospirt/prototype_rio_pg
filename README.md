# prototype_rio_pg
<a href="https://www.python.org/" style="text-decoration: none;"><img src="https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=ffdd54" height="20" alt="python"></a>
<a href="https://rio.dev/" style="text-decoration: none;"><img src="https://img.shields.io/badge/Rio-outline.svg?color=%2311e8e3e&link=https%3A%2F%2Frio.dev&style=flat-square&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgd2lkdGg9IjEwMDIuMTA1IgogICBoZWlnaHQ9IjE0OTkuODA1NyIKICAgdmlld0JveD0iMCAwIDI2NS4xNDAyOSAzOTYuODIzNTkiCiAgIHZlcnNpb249IjEuMSIKICAgaWQ9InN2Zzg5NiIKICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiCiAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyI+PGRlZnMKICAgICBpZD0iZGVmczg5MCIgLz48bWV0YWRhdGEKICAgICBpZD0ibWV0YWRhdGE4OTMiPjxyZGY6UkRGPjxjYzpXb3JrCiAgICAgICAgIHJkZjphYm91dD0iIj48ZGM6Zm9ybWF0PmltYWdlL3N2Zyt4bWw8L2RjOmZvcm1hdD48ZGM6dHlwZQogICAgICAgICAgIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiIC8+PC9jYzpXb3JrPjwvcmRmOlJERj48L21ldGFkYXRhPjxnCiAgICAgaWQ9ImxheWVyMSIKICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNi40MTM4NDcsNTAuMjcxMzUpIj48cGF0aAogICAgICAgaWQ9InBhdGgxIgogICAgICAgc3R5bGU9ImZpbGw6I2ZmZmZmZjtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MC4yNjQ1ODMiCiAgICAgICBkPSJtIC04LjgwMzA4MDMsLTUwLjI3MTM1IGMgLTE1LjI3NjU1OTcsMC44NjA1MjQgLTE4LjYzMTgzNDcsMTcuNTQ0NTEyIC0xNy4zNjc0MTU3LDI5Ljk2ODk1MiAwLjUxMzcyNywxNi4yNDQxNjYxIC0xLjIxMzE5NywzMi43MTkyOTcgMS4yNjg1MTcsNDguNzY2NzkzIDguMTQxMTg1LDE0LjcxMDAxMiAyNi4wNzc2NzYxLDE4Ljg0OTk3MiAzOS44Nzc0ODIsMjYuNzcwMTM0IDMwLjM3ODk2MiwxNS4wNjY1NSA2MC43NTc5MjUsMzAuMTMzMTAxIDkxLjEzNjg4Nyw0NS4xOTk2NTEgLTM0LjgyMjM5OCwxNy42MDY2OCAtNzAuMjI2MTE3LDM0LjE0NzgzIC0xMDQuNjYwNTA2OCw1Mi40NjUyOCAtMjAuMDM3Nzc1MiwxMS40ODE0NCAtMzQuNzc4MTg3MiwzNi45NjY5OCAtMjQuMTAxMTk2Miw1OS41OTIxMSAxMS4yOTkzMSwyNS42MDQ3IDM5Ljc0MjkxMSwzMy43MTY5NSA2Mi40NzIyMDgsNDUuOTY4MDIgNTguOTU5MTAzLDI5LjA5NDExIDExNy43MTA1MzUsNTguNjQ4NDIgMTc2Ljc4OTE1NSw4Ny40NzU2IDE0LjA2MTIxLDMuOTY4MzYgMjQuMDM2NzYsLTEyLjAyMzEgMjEuODAwNzksLTI0LjUzMjIgLTAuNTQyODUsLTE3LjgzMTU3IDEuMjU4MTYsLTM1LjkwMjkyIC0xLjI2ODM2LC01My41MzY0OCAtOC4xNDA2MywtMTQuNzEwNzEgLTI2LjA3NjkyLC0xOC44NTE5OCAtMzkuODc3MTksLTI2Ljc3MTcyIC0zMC4zNzYwNiwtMTUuMDcxMTUgLTYwLjgwMDczLC0zMC4xNDExNyAtOTEuMTQ2NDIsLTQ1LjIxMzA0IDM0LjUwODc5LC0xNy4zNzM3NyA2OS40NTU5NywtMzMuOTI1NjUgMTAzLjY3Mjk4LC01MS44NDY2MyAyMC4xOTUxMywtMTEuMDA2MjggMzUuMzg2NDQsLTM2LjMwMDA1IDI1LjYwMzM4LC01OC45ODA5NCBDIDIyNC43MDYyMyw1OC44NzI1MzQgMTk2LjA1MDY3LDUwLjQ4NjY0MSAxNzMuMTY3MjYsMzguMjM4MTkxIDE1MS4xOTIyNiwyNy4zNDkyOTUgMTI2LjI0NjM5LDE0LjkzOTYzOCAxMDYuMTIxMTcsNC45OTc2Mjc4IDcwLjA0MTcxOSwtMTIuODk5Mjk5IDMzLjk2MjI2OCwtMzAuNzk2MjI1IC0yLjExNzE4MzQsLTQ4LjY5MzE1MiBsIC0zLjM3MjY3NzcsLTEuMjE4NDkyIHoiIC8+PC9nPjwvc3ZnPgo=" alt="Rio"/>

<p align="center">
  <img src="https://github.com/hydrospirt/prototype_rio_pg/blob/master/img/title.png" alt="Password Generator" width=80%>
</p>
<p>Made with Rio Framework</p>

-   [Discord](https://discord.gg/7ejXaPwhyH) (Boost your skills with Rio! **Join the Discord server** to chat with other developers and discuss how to contribute.)
-   [GitHub](https://github.com/rio-labs/rio) (**Found a bug?** Issues are the perfect place to report it.)
-   [Community Forum](https://github.com/rio-labs/rio/discussions) (**Join the community forum on Github** to ask questions and participate in discussions)
-   [Feature Requests](https://github.com/rio-labs/rio/discussions/categories/feature-requests) (The easiest way to **request a feature** on GitHub)

## Description

🚀 **prototype_rio_pg** is a password generator prototype built on the Rio Framework. Open to all MVPs.

## Key Features

- ✨ **Password Generation**: Create passwords of varying lengths (from 8 to 128) and complexities ("Empty", "Pathetic" "Weak", "Good", "Strong", "Excellent").
- 🔥 **Parameter Customization**: Ability to choose the inclusion of numbers, letters, and special characters.
- 🛡️ **Security**: Utilizes cryptographic secrets for password generation.
<p align="center">
  <img src="https://github.com/hydrospirt/prototype_rio_pg/blob/master/img/discord.png" alt="Password Generator" width=80%>
</p>

### 🔍 Small Tip
If you want to edit the template, go to `password-generator/password_generator/utils/settings.py`

- 🤝 Got a question? You can reach me on Telegram: https://t.me/arcan1um

## Installation

Step-by-step instructions for installing the project.

1. Clone the project to your computer:
```bash
git clone git@github.com:hydrospirt/prototype_rio_pg.git
```
2. Install and activate the virtual environment with Python 3.12.5
    ```bash
    cd ./prototype_rio_pg/ &&
    py -3.12 -m venv venv
    ```
   For Windows:
    ```bash
    source venv/Scripts/Activate
    ```
    For Linux
    ```bash
    source . venv/bin/activate
    ```
3. Install dependencies from the requirements.txt file
    For Windows:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
    for Linux:
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. To run, execute the commands:
    ```bash
    cd ./password-generator/ &&
    rio run
    ```
5. Go to the link in the terminal or enter manually in the browser http://127.0.0.1:8000
```bash
The app is running at http://127.0.0.1:8000
```
## License 
🎉 Yay, free license [Unlicense](https://github.com/hydrospirt/prototype_rio_pg/blob/master/LICENSE)

Star it if you like it :)