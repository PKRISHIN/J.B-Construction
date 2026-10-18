"""Downloads real premium photos (free, Pexels) into static/img/<category>/.
Usage:  python get_photos.py YOUR_PEXELS_API_KEY"""
import sys, os, json, urllib.request, urllib.parse
KEY = sys.argv[1] if len(sys.argv) > 1 else os.getenv("PEXELS_KEY")
if not KEY: sys.exit("Usage: python get_photos.py YOUR_PEXELS_API_KEY")
CATS = {
 "exterior": "luxury villa exterior modern house",
 "living":   "luxury living room interior",
 "hall":     "luxury hall foyer interior chandelier",
 "kitchen":  "luxury modern kitchen interior",
 "bedroom":  "luxury master bedroom interior",
 "bathroom": "luxury bathroom interior",
 "dining":   "luxury dining room interior",
 "ceiling":  "false ceiling design living room lighting",
 "renovation": "home renovation interior makeover",
}
PER = 15
H = {"Authorization": KEY, "User-Agent": "Mozilla/5.0"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=30).read()
try: get("https://api.pexels.com/v1/search?query=house&per_page=1")
except Exception as e: sys.exit(f"Could not reach Pexels ({e}). Check your internet connection and API key.")
for cat, q in CATS.items():
    os.makedirs(f"static/img/{cat}", exist_ok=True)
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode({"query": q, "per_page": PER, "orientation": "landscape"})
    for i, p in enumerate(json.loads(get(url))["photos"], 1):
        path = f"static/img/{cat}/{cat}_{i:02d}.jpg"
        if os.path.exists(path): continue
        open(path, "wb").write(get(p["src"]["large"]))
        print("saved", path)
print("Done! Now run: python app.py")
