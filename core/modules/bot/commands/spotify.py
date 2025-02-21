import json

class spotify:
    def __init__(self, external_self):
        self.self = external_self

        self.exists, self.access_token = self.check_spotify()
        self.device_id = self.get_devices()
        self.prev_uri = ""

        self.commands = {
            "pause" : self.pause,
            "play" : self.play,
            "previous" : self.previous,
            "next" : self.next,
            "select" : self.select,
            "info" : self.info
        }

        @self.self.bot.command()
        async def spotify(ctx, command, args=""):
            if not self.exists:
                await ctx.send("No spotify account linked with this account")
            if command in self.commands:
                result = self.commands[command](args)

                await ctx.send(self.self.output("Spotify | {}".format(command), result, ctx.author.name, self.self.style, "general"))

    def check_spotify(self):
        api = "https://discord.com/api/v9/users/@me/connections"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.self.token
        }
        response = self.self.session.get(api, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for connection in data:
                if connection["type"] == "spotify":
                    return True, connection["access_token"]
        else:
            return False, ""
        
    def get_devices(self):
        api = "https://api.spotify.com/v1/me/player/devices"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        response = self.self.session.get(api, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["devices"][0]["id"]
        else:
            return ""

    def pause(self, args):
        api = "https://api.spotify.com/v1/me/player/pause"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        response = self.self.session.put(api, headers=headers)
        if response.status_code == 200:
            return [{"key" : "Success", "value" : "Spotify is now paused"}]
        else:
            return [{"key" : "Error", "value" : "Something went wrong"}]

    def play(self, args):
        api = "https://api.spotify.com/v1/me/player/play"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        response = self.self.session.put(api, headers=headers)
        if response.status_code == 200:
            return [{"key" : "Success", "value" : "Spotify is now playing"}]
        else:
            return [{"key" : "Error", "value" : "Something went wrong"}]

    def previous(self, args):
        api = "https://api.spotify.com/v1/me/player/previous"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        response = self.self.session.post(api, headers=headers)
        if response.status_code == 200:
            return [{"key" : "Success", "value" : "Spotify is now rewinding"}]
        else:
            return [{"key" : "Error", "value" : "Something went wrong"}]

    def next(self, args):
        api = "https://api.spotify.com/v1/me/player/next"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        response = self.self.session.post(api, headers=headers)
        if response.status_code == 200:
            return [{"key" : "Success", "value" : "Spotify is now fastforwarding"}]
        else:
            return [{"key" : "Error", "value" : "Something went wrong"}]

    def select(self, args):
        if "track" in args:
            uri = "spotify:track:" + args.split("track/")[1].split("?")[0]
            data = {"uris" : [uri]}
        elif "album" in args:
            uri = "spotify:album:" + args.split("album/")[1].split("?")[0]
            data = {"context_uri" : uri}
        elif "playlist" in args:
            uri = "spotify:playlist:" + args.split("playlist/")[1].split("?")[0]
            data = {"context_uri" : uri}
        api = "https://api.spotify.com/v1/me/player/play"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        response = self.self.session.put(api, headers=headers, json=data)
        if response.status_code == 204:
            return [{"key" : "Success", "value" : "Spotify is now playing"}]
        else:
            return [{"key" : "Error", "value" : "Something went wrong"}]

    def info(self, args):
        api = "https://api.spotify.com/v1/me"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        response = self.self.session.get(api, headers=headers)
        if response.status_code == 200:
            data = response.json()

            country = data["country"]
            name    = data["display_name"]
            product = data["product"]
            type    = data["type"]

            values = ["Country", "Name", "Product", "Type"]

            longest = max(len(value) for value in values)

            return [
                {
                    "key" : "Country".ljust(longest),
                    "value" : country
                },
                {
                    "key" : "Name".ljust(longest),
                    "value" : name
                },
                {
                    "key" : "Product".ljust(longest),
                    "value" : product
                },
                {
                    "key" : "Type".ljust(longest),
                    "value" : type
                }
            ]