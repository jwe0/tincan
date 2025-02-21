import json, datetime

def load_style(style):
    with open("core/settings/style.json", "r") as f:
        return json.load(f)[style]

def apply_custom_markdown(value, title, author, style, type, location):
    message = ""
    markdowns = [
        ("{split}", style["split"]),
        ("{title}", title),
        ("{time}", datetime.datetime.now().strftime("%H:%M:%S")),
        ("{start}", style["start"]),
        ("{end}", style["end"]),
        ("{line_end}", style["line_end"]),
        ("{author}", author),
    ]
    if location == "content":
        for markdown in markdowns:
            type = type.replace(markdown[0], markdown[1])
        message = type
        for k, v in value.items():
            message = message.replace(f"{{{k}}}", v)
    else:
        for markdown in markdowns:
            value = value.replace(markdown[0], markdown[1])
        message = value

    for markdown in markdowns:
        message = message.replace(markdown[0], markdown[1])
    return message

def output(title="", content="", author="", style="default", type="general"):
    style = load_style(style)
    if not style:
        return "Style not found"
    message = ""

    type = style["formats"][type]

    message += apply_custom_markdown(style["header"], title, author, style, type, "header")
    for line in content:
        if not line:
            continue
        message += apply_custom_markdown(line, title, author, style, type, "content")
    message += apply_custom_markdown(style["footer"], title, author, style, type, "footer")
    return message