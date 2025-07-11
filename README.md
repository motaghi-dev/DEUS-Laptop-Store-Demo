# DEUS Laptop Store

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A **Python-based command-line application** simulating an elementary laptop store with basic user authentication, product filtering, and shopping cart functionality.
I made this small side project mainly as an outlet to experiment with pandas and SQL.

---

##  Features

- **User Authentication System**
  - New user registration
  - Returning user login
  - Secure credential storage

- **Product Management**
  - Web-scraped laptop database (from `zoomit.ir`)
  - Detailed product specifications and pricing
  - Advanced filtering system with SQL-like syntax

- **Shopping Cart Functionality**
  - Add multiple products by index
  - Remove individual items
  - Empty cart completely
  - Final purchase confirmation

- **Data Handling**
  - `pandas` DataFrame integration
  - Persistent data storage in text files
  - Clean terminal interface with color formatting

---

##  File Structure

```
DEUS-Store/
├── cart.py                  # Shopping cart management
├── Dataframex.py            # DataFrame operations and filtering
├── fetch_data.py            # Web scraper for product data
├── fetch_data.txt           # Product database
├── main_menu.py             # User authentication system
├── shopping_cart.txt        # Current cart contents
├── store.py                 # Main store interface
└── username_passwords.txt   # User credentials storage
```

---

##  Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/DEUS-Online-Store.git
   cd DEUS-Online-Store
   ```

2. **Install required dependencies:**
   ```bash
   pip install pandas beautifulsoup4 requests termcolor
   ```

3. **Run the application:**
   ```bash
   python main_menu.py
   ```

---

##  Usage

###  Authentication
- Register a new account or login with existing credentials.

###  Store Interface
- View all available laptops.
- Filter products using conditions like:
  ```text
  Price > 1000 and "Apple" in Name and "16GB" in Specs
  ```
- Add products to cart by entering their indices (e.g., `12 43 26`).

###  Shopping Cart
- Review selected items.
- Remove individual products.
- Empty cart completely.
- Complete purchase.

---

##  Data Flow

- Product data is scraped from `zoomit.ir` and stored in `fetch_data.txt`.
- User credentials are stored in `username_passwords.txt`.
- Cart contents persist in `shopping_cart.txt`.

---

## ⚙ Technical Details

- Built with **Python 3.x**
- Uses:
  - `pandas` for data manipulation
  - `BeautifulSoup` for web scraping
  - `termcolor` for CLI styling
- Persistent data storage via text files.

---

##  Example Queries

- Find all **Lenovo laptops under $1000**:
  ```text
  Price < 1000 and "Lenovo" in Name
  ```

- Find **gaming laptops with RTX 4060**:
  ```text
  "RTX 4060" in Specs
  ```

- Find **premium Apple laptops**:
  ```text
  "Apple" in Name and Price > 1500
  ```

---

##  License

This project is open-source and available under the [MIT License](LICENSE).
