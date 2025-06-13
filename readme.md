# BGU Mart Management System (Python & SQLite)

**Assignment 4 – SPL 251: Supermarket Chain Database Management**

A lightweight Python toolset for creating, updating, and querying a supermarket chain database (`bgumart.db`) using SQLite3.

---

## 🚀 Quick Start

1. **Clone the repo**

   ```bash
   git clone https://github.com/<username>/bgumart-management-python.git
   cd bgumart-management-python
   ```

2. **Install dependencies** (requires Python 3.7+; SQLite3 comes bundled with Python)

   ```bash
   pip install -r requirements.txt   # if using any external libs
   ```

3. **Initialize the database**

   ```bash
   python initiate.py config.txt
   ```

   - Creates `bgumart.db` with tables: `employee`, `supplier`, `product`, `branch`, `activity`.

4. **Process actions**

   ```bash
   python action.py actions.txt
   ```

   - Applies insert/update/delete operations defined in `actions.txt` against `bgumart.db`.

5. **Print reports**

   ```bash
   python printdb.py employee    # prints employee report
   python printdb.py supplier    # prints supplier list
   ```

---

## 📂 Project Layout

```
├── docs/
│   └── ass4_instructions.txt    # Assignment description
├── bgumart.db                   # Preloaded SQLite database (optional)
├── config.txt                   # Database initialization parameters
├── actions.txt                  # List of actions to execute
├── initiate.py                  # Creates and seeds the database
├── action.py                    # Executes CRUD operations
├── printdb.py                   # Query and print formatted reports
├── dbtools.py                   # Helper functions for DB operations
├── persistence.py               # Data persistence layer
└── README.md                    # This file
```

---

## 🛠️ Prerequisites

- **Python:** 3.7+
- **SQLite3:** bundled with Python
- (Optional) any third-party packages listed in `requirements.txt`

---

## 💾 Database Schema

| Table      | Columns                                                     |
| ---------- | ----------------------------------------------------------- |
| `employee` | `id`, `first_name`, `last_name`, `salary`, `city`, `active` |
| `supplier` | `id`, `name`, `phone`                                       |
| `branch`   | `id`, `name`, `location`, `manager_id`                      |
| `product`  | `id`, `name`, `price`, `supplier_id`                        |
| `activity` | `id`, `employee_id`, `product_id`, `quantity`, `date`       |

---

## 📖 Usage Examples

- **Initialize & seed**

  ```bash
  python initiate.py config.txt
  ```

- **Apply actions**

  ```bash
  python action.py actions.txt
  ```

- **Generate reports**

  ```bash
  python printdb.py employee
  python printdb.py activity
  ```

---

## 🔍 Testing & Debugging

- Use `python -m pdb initiate.py` to step through initialization
- Inspect `bgumart.db` directly with SQLite CLI:
  ```bash
  sqlite3 bgumart.db
  sqlite> .tables
  ```

---

## 📝 License

MIT License — see [LICENSE](LICENSE)

