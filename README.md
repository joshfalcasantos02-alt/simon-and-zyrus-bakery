# 🥖 Simon & Zyrus Bakery - Django Inventory & Daily Sales Management System

A production-ready **Django** web application and inventory ledger for **Simon & Zyrus Bakery**, providing real-time daily stock tracking, POS cash drawer reconciliation, recipe batch costing, supplier purchases, and sales reporting.

---

## 🚀 Quick Start

### 1. One-Click Windows Launch
Double-click **`start.bat`** in this folder:
```
C:\Users\ADMIN\.gemini\antigravity\scratch\django-bakery\start.bat
```

### 2. Or Run via Terminal
```powershell
cd C:\Users\ADMIN\.gemini\antigravity\scratch\django-bakery
python run.py
```
Or standard Django command:
```powershell
python manage.py runserver
```

Open your browser at:
- **Bakery Dashboard:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Admin Portal:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - **Username:** `admin`
  - **Password:** `admin123`
- **XAMPP phpMyAdmin:** [http://localhost/phpmyadmin/](http://localhost/phpmyadmin/)
  - **Database Name:** `bakery_db`

---

## 🗄️ XAMPP MySQL Connection Settings

The project is connected to your local **XAMPP MySQL / MariaDB** server:
- **Host:** `127.0.0.1` (localhost)
- **Port:** `3306`
- **Database:** `bakery_db`
- **User:** `root`
- **Password:** *(empty by default in XAMPP)*
- **Driver:** `pymysql` (installed as MySQLdb)

Ensure your **XAMPP Control Panel** has the **MySQL** module started (green indicator).

## 🌟 Key Features

### 1. 📊 Real-Time Daily Count Ledger
- **Beginning Stock Auto-Carryover:** Beginning count automatically rolls over from the previous day's ending count.
- **Inventory Math:** `Available = Beginning + Added - Damaged`, `Sold = Available - Ending`, `Sales = Sold × Unit Price`.
- **Quick Unsold Filler:** Single-click "Mark blank items as unsold" button.
- **Category Filter & Search:** Filter by Breads & Pastries, Snacks & Candies, Groceries, Beverages, Ice Cream.
- **Debounced Instant Auto-Save:** Edits save directly to Django via REST endpoints with CSRF protection.

### 2. 💵 Cash Drawer & End-of-Day Reconciliation
- **Expected Cash vs Counted Cash:** Automatically calculates expected net cash from item sales, sales orders, change fund, deposits, utang payments minus expenses, utang given, and remittances.
- **Denomination Counter:** Quick piece count for ₱1,000, ₱500, ₱200, ₱100, ₱50, ₱20, ₱10, ₱5, and ₱1 bills & coins.
- **Short / Over Badge:** Highlights net cash discrepancy in green (over) or red (short).
- **Expense & Utang (Credit) Log:** Records itemized daily operational expenses and customer credit slips.

### 3. 🍞 Items for Sale (Products)
- Full product catalog with categories, retail selling prices (₱), opening inventory, and minimum reorder alert levels.
- Historical price stability: Price edits only apply to new daily counts without altering recorded historical reports.

### 4. 📦 Purchases & Stock on Hand
- **Supplier Purchases:** Log raw ingredients, packaging, or store inventory with quantities, units, and supplier costs. Automatically updates the item's latest cost for recipe calculations.
- **Physical Shelf Count:** Record periodic stock audits with `On Hand = Last Count + Purchases Since Count`.
- **Restocking Alerts:** Proactive warnings for items approaching or below minimum reorder thresholds.

### 5. 🧑‍🍳 Recipe Costing & Batch Profitability
- Dynamic batch costing for signature bakery favorites (Classic Pandesal, Ube Cheese Pandesal, Spanish Bread, etc.).
- Calculates **Batch Cost**, **Cost per Piece**, **Food Cost %**, **Margin per Piece**, and **Total Batch Profit**.
- Supports unit conversions (e.g. grams vs kilograms, milliliters vs liters).

### 6. 📈 Sales Reports & CSV Downloads
- Daily sales bar chart with breakdown of counter sales vs custom sales orders.
- Item sales rank with sales volume, revenue share %, and daily average.
- Stock usage report calculated between physical stock count intervals.
- 1-click **Download CSV** buttons for accounting and Excel spreadsheets.

---

## 🛠️ Project Structure

```
django-bakery/
├── bakery/                   # Django project configuration
│   ├── settings.py           # Database, timezone (Asia/Manila), static & templates
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI entrypoint
│   └── asgi.py               # ASGI entrypoint
├── inventory/                # Bakery Inventory Django Application
│   ├── models.py             # Product, StockItem, Recipe, DayRecord, Purchase, StockCount
│   ├── views.py              # REST API endpoints & dashboard controller
│   ├── urls.py               # App routes & API endpoints
│   ├── admin.py              # Django admin registrations
│   ├── tests.py              # Automated test suite
│   └── management/
│       └── commands/
│           └── seed_bakery.py# Preloaded bakery items, ingredients & recipes
├── templates/
│   └── inventory/
│       └── index.html        # Interactive responsive SPA frontend
├── static/                   # Static assets directory
├── db.sqlite3                # SQLite database with seeded data
├── run.py                    # Server runner script
├── start.bat                 # Windows launcher
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```
