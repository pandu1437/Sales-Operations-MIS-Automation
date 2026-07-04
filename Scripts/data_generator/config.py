from pathlib import Path
import random

# ==========================================================
# PROJECT CONFIGURATION
# ==========================================================

# Project Root
BASE_DIR = Path(__file__).resolve().parents[2]

# Data Directories
DATA_DIR = BASE_DIR / "Data"
RAW_DATA_DIR = DATA_DIR / "Raw_Data"
CLEAN_DATA_DIR = DATA_DIR / "Cleaned_Data"
SQL_DATA_DIR = DATA_DIR / "SQL_Data"

# Create folders if they don't exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
CLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
SQL_DATA_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# RANDOM SEED
# ==========================================================

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# ==========================================================
# COMPANY DETAILS
# ==========================================================

COMPANY_NAME = "ABC Retail Pvt. Ltd."

# ==========================================================
# DATASET SIZE
# ==========================================================

NUM_BRANCHES = 15
NUM_EMPLOYEES = 100
NUM_CUSTOMERS = 2000
NUM_PRODUCTS = 100
NUM_SALES = 100000

# ==========================================================
# OUTPUT FILES
# ==========================================================

BRANCH_FILE = RAW_DATA_DIR / "branches.csv"
EMPLOYEE_FILE = RAW_DATA_DIR / "employees.csv"
CUSTOMER_FILE = RAW_DATA_DIR / "customers.csv"
PRODUCT_FILE = RAW_DATA_DIR / "products.csv"
SALES_FILE = RAW_DATA_DIR / "sales.csv"