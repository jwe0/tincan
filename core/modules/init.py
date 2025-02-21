import os, json
from core.modules.logging import *

def check_dirs():
    dirs = [
        "core/assets",
        "core/settings"
    ]

    for dir in dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)

def check_files():
    files_json = [
        ["core/settings/style.json", {
            "default" : {
                "start" : "> -# `",
                "end" : "`",
                "split" : "»",
                "footer" : "```{time} | Tin Can Bot```",
                "header" : "```{title}```"
            }
        }]
    ]

    for file in files_json:
        if not os.path.exists(file[0]):
            with open(file[0], "w") as f:
                json.dump(file[1], f, indent=4, ensure_ascii=False) 

def create_config():
    token = inpt("Token: ")
    prefix = inpt("Prefix: ")
    config = {
        "token": token,
        "prefix": prefix,
        "active_style" : "default"
    }
    with open("core/assets/config.json", "w") as f:
        json.dump(config, f, indent=4)

def load_config():
    if not os.path.exists("core/assets/config.json"):
        create_config()
    with open("core/assets/config.json", "r") as f:
        return json.load(f)