import json
import webbrowser
import random

def printJson(dict):
    print(json.dumps(dict, sort_keys=False, indent=2))
username = input("What is your computer username?")
windows = rf"C:\\Users\\{username}\AppData\\Local\\Google\\Chrome\\User Data\Default\Bookmarks"
mac = f"/Users/{username}/Library/Application Support/Google/Chrome/Default/Bookmarks"

raw_data = open(windows, "r")
object_data = json.loads(raw_data.read())

del object_data["sync_metadata"]
del object_data["checksum"]

bookmarks = object_data["roots"]["bookmark_bar"]["children"]

unused_folders = []
urls = []


for bookmark in bookmarks:
    if "children" in bookmark:
        unused_folders.append(bookmark["children"])
    else:
        urls.append(bookmark["url"])

for object in unused_folders:
   for bookmark in object:
        if "children" in object:
            unused_folders.append(bookmark["children"])
        else:
            urls.append(bookmark["url"])


random_url = random.choice(urls)
print(random_url)

webbrowser.open(random_url)