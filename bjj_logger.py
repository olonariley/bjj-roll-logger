# bjj_logger.py - Track your rolls like a pro
import json
import os
from datetime import datetime

# Save to your Desktop (works on any Mac)
LOG_FILE = os.path.expanduser("~/Desktop/rolls.json")

def load_rolls():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_rolls(rolls):
    with open(LOG_FILE, "w") as f:
        json.dump(rolls, f, indent=2)

def add_roll():
    partner = input("Partner name: ")
    my_subs = input("Subs you hit: ")
    their_subs = input("Subs they hit: ")
    notes = input("Notes (optional): ")
    
    roll = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "partner": partner,
        "my_subs": my_subs.split(", "),
        "their_subs": their_subs.split(", "),
        "notes": notes
    }
    return roll

def show_stats(rolls):
    print("\n=== YOUR ROLL STATS ===")
    print(f"Total rolls: {len(rolls)}")
    subs_hit = sum(len(r["my_subs"]) for r in rolls if r["my_subs"] != [''])
    print(f"Subs hit: {subs_hit}")
    if rolls:
        from collections import Counter
        partners = [r["partner"] for r in rolls]
        top3 = Counter(partners).most_common(3)
        print("Top partners:", ", ".join([f"{p} ({c})" for p, c in top3]))
    else:
        print("No rolls yet!")

# Main loop
rolls = load_rolls()
print("BJJ Roll Logger - Type 'done' to quit")

while True:
    action = input("\nAdd roll? (y/n/stats/done): ").lower()
    if action == "y":
        rolls.append(add_roll())
        save_rolls(rolls)
        print("Roll saved!")
    elif action == "stats":
        show_stats(rolls)
    elif action in ["n", "done"]:
        break

print("See you on the mats!")