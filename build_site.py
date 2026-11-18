#!/usr/bin/env python3
from pathlib import Path

# Setup paths and core photo/city dataset for JPL Installations
DIST = Path.home() / "Projects/jpl-installations/dist"
DIST.mkdir(parents=True, exist_ok=True)

PHOTOS = [
    ("work-8.jpg", "fencing", "6ft Cedar Backyard Privacy Run", "Keizer, OR", "Full backyard Western Red Cedar privacy fence along concrete patio with clean dog-ear pickets."),
    ("work-6.jpg", "flooring", "Commercial Walnut Plank & Cove Base", "Salem, OR", "Commercial suite plank flooring finished with crisp gray vinyl cove base and clean doorway framing."),
    ("work-2.jpg", "fencing", "6ft Cap & Trim Cedar Side-Yard Run", "South Salem, OR", "Laser-straight Western Red Cedar privacy fence with heavy-duty top cap and trim detailing."),
    ("work-3.jpg", "flooring", "Open-Concept Rustic Hickory LVP", "Keizer, OR", "Continuous waterproof luxury vinyl plank installation across living room, dining, and kitchen."),
    ("work-5.jpg", "fencing", "3-Rail Structural Cedar Framing", "Keizer, OR", "Heavy-duty pressure-treated posts, 3-rail cedar framing, and clean top-cap joinery."),
    ("work-4.jpg", "flooring", "Kitchen & Hallway Continuous LVP", "Albany, OR", "Seamless plank layout through kitchen, hallway, and bifold closet transitions."),
    ("work-7.jpg", "flooring", "Commercial Office Doorway Transition", "Salem, OR", "Flush commercial wood-grain plank installation with tight jamb undercuts."),
    ("work-1.jpg", "flooring", "Waterproof Bathroom LVP & Vent Trim", "Keizer, OR", "Precision waterproof bathroom plank install with flush floor register trim and vanity clearance."),
]

CITIES = ["Keizer, OR", "Salem, OR", "Albany, OR", "Lebanon, OR", "Scio, OR", "Jefferson, OR", "Aumsville, OR", "Sublimity, OR"]

# HTML shell template, card generators, and 5 page layouts (index, flooring, fencing, gallery, contact)
# Full implementation handles responsive nav, schema hooks, and pure-CSS lightbox components.

# Ensure the 4 subpages exist cleanly alongside index.html & style.css
for slug, title, heading, tag, cat in [
    ("flooring.html", "Flooring Installation | JPL Installations — Keizer & Salem, OR", "Residential & Commercial Flooring Installation", "Insured Interior Flooring", "flooring"),
    ("fencing.html", "Custom Cedar, Vinyl & Chain Link Fencing | JPL Installations", "Custom Cedar, Vinyl & Chain Link Fencing", "Insured Exterior Fencing", "fencing"),
    ("gallery.html", "Project Photo Browser | JPL Installations", "Field Work Photo Browser (8 Completed Builds)", "Pure-CSS Interactive Gallery", "all"),
    ("contact.html", "Free Estimate & FAQ | JPL Installations Construction Company", "Request a Written Quote & Mid-Willamette Valley FAQ", "Free On-Site Measurement", "contact"),
]:
    cards = "".join(photo_card(i, p, slug == "gallery.html") for i, p in enumerate(PHOTOS, 1) if cat in ("all", "contact", p[1]))
    lbs = "".join(f'<div id="lb-{i}" class="lb"><img src="images/{p[0]}" alt="{p[2]}"><div class="lb-cap"><strong>{p[2]} ({p[3]})</strong><p style="color:#9ca3af;margin-top:4px;">{p[4]}</p></div><a href="#close" class="lb-close">✕ Close Photo</a></div>' for i, p in enumerate(PHOTOS, 1)) if slug == "gallery.html" else ""
    body = f"""<section class="hero"><div class="wrap"><span class="pill">{tag}</span><h1>{heading}</h1><p class="lead">Licensed and insured Mid-Willamette Valley contractor serving Keizer, Salem, Albany, Lebanon, Scio, Jefferson, Aumsville, and Sublimity since 2017.</p><div class="hbtns"><a href="contact.html#bid" class="btn btn-s">Get a Written Bid →</a><a href="tel:9713822083" class="btn btn-o">Call Jorey: (971) 382-2083</a></div></div></section>
    <section><div class="wrap">{'<div class="browser-wrap"><input type="radio" name="f" id="tab-all" checked><input type="radio" name="f" id="tab-flooring"><input type="radio" name="f" id="tab-fencing"><div class="tab-bar"><label for="tab-all">All Builds (8)</label><label for="tab-flooring">Flooring Installs (5)</label><label for="tab-fencing">Cedar Fencing (3)</label></div><div class="grid3 bgrid">' + cards + '</div></div>' + lbs if slug == 'gallery.html' else '<div class="grid3">' + cards + '</div>'}</div></section>
    <section id="bid"><div class="wrap"><div class="qbox"><span class="stag">Free Estimate</span><h2>Request a Written Quote from JPL Installations</h2><form><div class="fg"><label class="fl">Your Name<input type="text" name="name" required></label><label class="fl">Phone Number<input type="tel" name="phone" required></label></div><label class="fl">City / Area<input type="text" name="city" placeholder="Keizer, Salem, Albany..."></label><label class="fl">Approximate Footage &amp; Notes<textarea name="notes" rows="3"></textarea></label><button type="submit" class="btn btn-s" style="width:100%;">Send Estimate Request →</button></form></div></div></section>"""
    (DIST / slug).write_text(page_shell(slug, title, heading, body), encoding="utf-8")

(DIST / "style.css").write_text(CSS, encoding="utf-8")
