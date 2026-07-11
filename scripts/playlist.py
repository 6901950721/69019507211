import re

with open("us-original.m3u", "r", encoding="utf-8") as f:
    playlist = f.read()
    
playlist = re.sub(
    r'tvg-id="([^"]+)@[^"]+"',
    r'tvg-id="\1"',
    playlist
)

with open("us.m3u", "w", encoding="utf-8") as f:
    f.write(playlist)

print("Playlist fixed")