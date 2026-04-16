# Travel Booking Data Engineering Challenge

## 📋 Overview

You work for a travel company that processes booking data from multiple sources. Your task is to clean, transform, and analyze booking data that has various quality issues.

## 🎯 What We're Evaluating

- **Python & Pandas**: Data cleaning, transformation, and ETL pipeline development
- **Code Design**: Your approach to structuring code (functional, OOP, or other)
- **Code Quality**: Clean, efficient, well-documented code with type annotations
- **SQL**: Analytical queries and data aggregation
- **Git**: Version control practices and commit hygiene
- **Problem Solving**: Identifying and handling data quality issues
- **Critical Thinking**: Improving existing code where opportunities exist

## 🛠️ Setup

### Prerequisites
- Python 3.9 or higher
- Git

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd data-engineer-test
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Verify the database is accessible:
```bash
python -c "import sqlite3; conn = sqlite3.connect('bookings.db'); print('Database loaded successfully')"
```

## 📊 Database Structure

The `bookings.db` SQLite database contains two tables:

- **`raw_bookings`**: Travel booking transactions (with data quality issues to fix)
- **`destinations`**: Destination reference data for enrichment

Explore the tables to understand the data structure and identify issues.

## ✅ Tasks

### Task 1: Python ETL Pipeline (30 minutes)

**File to edit:** `etl.py`

Complete the ETL pipeline as outlined in the `TODO` comments in the main section:

1. **Clean the booking data**:
   - Handle duplicate bookings
   - Standardize date formats (booking_date, start_date, end_date)
   - Deal with missing values appropriately
2. **Enrich the data** by joining with the destinations table
3. **Transform** the data as needed (calculate derived fields, handle currency conversions)
4. **Save** the cleaned data to a new table `clean_bookings` in the database

**Your Approach:**
- Design your own code structure (functional, OOP, or other approaches)
- Review the existing code - if you find opportunities for improvement, feel free to refactor
- One function is provided as a reference for style (docstring, type annotations)

**Success Criteria:**
- All TODOs implemented with clean, well-structured code
- Code runs without errors
- `clean_bookings` table created with valid, cleaned data
- Proper error handling for data quality issues

### Task 2: SQL Analysis (10 minutes)

**File to edit:** `queries.sql`

Write a SQL query:

**Query: Revenue by Destination**
- Calculate total revenue, booking count, and average booking value per destination
- Only include destinations with more than 5 bookings
- Order by total revenue (highest first)

**Success Criteria:**
- Query executes without errors
- Results are meaningful and correctly calculated
- Appropriate use of SQL constructs (GROUP BY, HAVING, aggregations, etc.)
---

## Mockups

### Result
![Result_Example](mockups/result_example.png)

---


## 📤 Submission Instructions

1. **Branch Creation**: Create a new branch for your work using a descriptive name (e.g., something like `feature/your-name-solution`)

2. **Version Control**: Make commits as you progress through the tasks. Use meaningful commit messages that clearly describe what each commit accomplishes.

3. **Remote Submission**: Push your branch to the remote repository

4. **Merge Request**: Create a Merge Request with a comprehensive description that includes:
   - Your approach and design decisions
   - What you implemented and why you structured it that way
   - Data quality issues found and how you handled them
   - Any assumptions or decisions made
   - Any additional comments you have

5. **Notify**: After creating your Pull Request, send an email as specified in the received instructions. 

All done! We will get back to you when we have an update about your submission.

## 🤔 Need Help?

If you have questions about:
- **Technical issues**: Check Python/pandas versions, database connection
- **Assumptions**: Document them in your Merge Request description

## 💡 Tips

- **Explore the data first** - understand what you're working with
- **Handle edge cases** - real data is messy!
- **Document your decisions** - explain your reasoning
- **Test your code** - make sure it runs end-to-end
  

Good luck! 🚀
#
