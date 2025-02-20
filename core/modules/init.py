import os, json
from core.modules.logging import *

def check_dirs():
    dirs = [
        "core/assets"
    ]

    for dir in dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)

def create_config():
    token = inpt("Token: ")
    prefix = inpt("Prefix: ")
    config = {
        "token": token,
        "prefix": prefix
    }
    with open("core/assets/config.json", "w") as f:
        json.dump(config, f, indent=4)

def load_config():
    if not os.path.exists("core/assets/config.json"):
        create_config()
    with open("core/assets/config.json", "r") as f:
        return json.load(f)