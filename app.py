import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-secret"

BRAND = "JB Construction.co"
OWNER = "Bharat Prajapati"
PHONE = "9574718777"
EMAIL = "bkpra77@gmail.com"
WHATSAPP = "919574718777"

CATS = {  # folder: label
    "exterior": "Luxury Villas", "living": "Living Rooms", "hall": "Grand Halls",
    "kitchen": "Kitchens", "bedroom": "Bedrooms", "bathroom": "Bathrooms",
    "dining": "Dining Areas", "ceiling": "False Ceiling", "renovation": "Renovation",
}
SERVICES = [
    ("🏞️", "Land Purchase", "Verified, legally clear land in fast-growing locations."),
    ("🏠", "Home Construction", "Premium construction with the finest materials."),
    ("🔑", "Ready Homes for Sale", "Move-in ready luxury homes at honest prices."),
    ("🛠️", "Home Renovation", "Turn your old house into a modern luxury home."),
]
RENO = [
    ("Full Home Renovation", "Structure, flooring, plaster and paint, completely renewed.", "renovation"),
    ("Modular Kitchen", "Modern, smart and stylish kitchens.", "kitchen"),
    ("Bathroom Makeover", "Premium tiles, fittings and waterproofing.", "bathroom"),
    ("Interior & False Ceiling", "Luxury ceilings, cove lighting and woodwork.", "ceiling"),
    ("Exterior & Elevation", "A striking front elevation and finish.", "exterior"),
    ("Living & Dining Design", "Elegant spaces made for family and guests.", "living"),
]

def photos(cat):
    d = os.path.join(app.static_folder, "img", cat)
    if not os.path.isdir(d): return []
    fs = sorted(f for f in os.listdir(d) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))
    return [dict(cat=cat, label=CATS[cat], path=f"img/{cat}/{f}", title=f"{CATS[cat]} {i+1:02d}") for i, f in enumerate(fs)]

def first(cat):
    p = photos(cat); return p[0]["path"] if p else None

@app.context_processor
def inject():
    return dict(BRAND=BRAND, OWNER=OWNER, PHONE=PHONE, EMAIL=EMAIL, WHATSAPP=WHATSAPP)

DESC = {
    "exterior": "Modern villas and bungalows with striking elevations.", "living": "Elegant living rooms designed for comfort and style.",
    "hall": "Grand halls and foyers with statement lighting.", "kitchen": "Modular kitchens with premium finishes.",
    "bedroom": "Luxury bedrooms and master suites.", "bathroom": "Spa-style bathrooms with premium fittings.",
    "dining": "Refined dining spaces for family and guests.", "ceiling": "False ceilings with cove and designer lighting.",
    "renovation": "Complete home makeovers, before to after.",
}

def categories(skip=("renovation",)):
    out = []
    for c, l in CATS.items():
        p = photos(c)
        if c not in skip and p: out.append(dict(cat=c, label=l, desc=DESC[c], cover=p[0]["path"], count=len(p)))
    return out

@app.route("/")
def home():
    hero = [first(c) for c in ("exterior", "living", "hall")]
    return render_template("index.html", feat=categories()[:6], hero=hero, services=SERVICES)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/homes")
def homes():
    return render_template("homes.html", cats=categories())

@app.route("/gallery/<cat>")
def gallery(cat):
    if cat not in CATS: return redirect(url_for("homes"))
    return render_template("gallery.html", items=photos(cat), label=CATS[cat], desc=DESC[cat])

@app.route("/renovation")
def renovation():
    return render_template("renovation.html", items=[(t, d, first(c), c) for t, d, c in RENO])

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("NEW ENQUIRY:", dict(request.form))
        flash("Thank you! We will contact you shortly.")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    import subprocess, sys
    key = os.getenv("PEXELS_KEY") or (open("key.txt").read().strip() if os.path.exists("key.txt") else None)
    if key and not photos("exterior"):
        subprocess.run([sys.executable, "get_photos.py", key])
    app.run(debug=True)
