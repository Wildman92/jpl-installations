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
