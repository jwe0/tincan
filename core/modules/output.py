import json, datetime

def load_style(style):
    with open("core/settings/style.json", "r") as f:
        return json.load(f)[style]

def apply_custom_markdown(data, title, content, author, style):
    markdowns = [
        ("{title}", title),
        ("{time}", datetime.datetime.now().strftime("%H:%M:%S")),
        ("{split}", style["split"]),
    ]

    for markdown in markdowns:
        data = data.replace(markdown[0], markdown[1])
    
    return data

def output(title="", content="", author="", style="default"):
    style = load_style(style)
    if not style:
        return "Style not found"
    message = ""

    message += apply_custom_markdown(style["header"], title, content, author, style) + "\n"
    for line in content.split("\n"):
        message += style["start"] + apply_custom_markdown(line, title, content, author, style) + style["end"] + "\n" 

    message += apply_custom_markdown(style["footer"], title, content, author, style)
    return message