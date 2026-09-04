# Hotel Management System

A command-line hotel management system covering customer check-in, room billing, restaurant orders, and laundry billing, built in Python with SQLite.

## Overview

This project was originally a CBSE Class 12 Computer Science project built with Python + MySQL. I debugged the original code, fixed several logic bugs, and converted the backend from MySQL to SQLite (including auto-seeding the reference data for rooms, restaurant menu, and laundry rates).

## Features

- **Register Customer** — record guest name, address, check-in and check-out dates
- **View Room Types** — see the 4 available room categories and their nightly rates
- **Calculate Room Bill** — pick a room type and number of nights, get the total
- **Restaurant Menu** — view available food/drink items and prices
- **Order Items** — order from the restaurant menu and get the bill for that order
- **Laundry Billing** — view laundry rates and calculate a bill based on number of items
- **Complete Bill** — view the combined restaurant + laundry bill for a customer

## Tech Stack

- Python 3
- SQLite (via the built-in `sqlite3` module — no separate database server needed)

## How to Run

```bash
python3 hotel_management.py
```

The database file (`hotel.db`) is created automatically, and the room types, restaurant menu, and laundry rates are seeded in automatically the first time you run it.

## Bugs Fixed From the Original

- **The "Complete Bill" option never actually showed the bill** — it printed the function objects themselves instead of calling them, so no numbers ever appeared. Fixed to actually call and display the bill.
- The room rent calculation used a local variable instead of a global one, so the final bill couldn't see the value calculated earlier in the session. Fixed with proper `global` declarations.
- Fixed a database column name mismatch that would have caused every new customer registration to fail
- The main menu silently asked for the same input twice, discarding the first answer — removed the duplicate prompt
- Fixed a platform-detection bug (`"windows"` vs. the correct `"Windows"`) that meant the "clear screen" logic never worked correctly on Windows
- Converted all raw MySQL syntax to SQLite, and added automatic seeding of the lookup tables so the reference data (room types, menu, laundry rates) is available without a manual SQL import
