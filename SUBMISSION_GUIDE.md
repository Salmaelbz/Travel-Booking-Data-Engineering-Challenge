# Submission Instructions — Step by Step

Follow these steps to submit the Data Engineer Take-Home Test to:
**https://github.com/vtt-de-test/data-engineer-test-vtt-Salmaelbz.git**

---

## Prerequisites

- **Git** must be installed. If not: https://git-scm.com/download/win
- Ensure Git is in your PATH (restart terminal/IDE after installing).

---

## Step 1: Open Terminal in Project Folder

```powershell
cd "c:\Users\salma\Downloads\data-engineer-test-vtt-Salmaelbz-main"
```

---

## Step 2: Initialize Git (if not already a repo)

```powershell
git init
```

---

## Step 3: Add the Remote

```powershell
git remote add origin https://github.com/vtt-de-test/data-engineer-test-vtt-Salmaelbz.git
```

If `origin` already exists and points elsewhere, use:
```powershell
git remote set-url origin https://github.com/vtt-de-test/data-engineer-test-vtt-Salmaelbz.git
```

---

## Step 4: Create Branch

```powershell
git checkout -b feature/salma-solution
```

*(Replace `salma` with your preferred identifier if needed.)*

---

## Step 5: Stage and Commit Files

**Files to submit:** `etl.py`, `queries.sql`, `config.py`, `bookings.db`, `requirements.txt`, `README.md`, `.gitignore`

### Option A: One commit (simple)

```powershell
git add etl.py queries.sql config.py bookings.db requirements.txt README.md .gitignore
git commit -m "Complete ETL pipeline and SQL analysis for travel booking data"
```

### Option B: Multiple commits (recommended — shows progression)

```powershell
git add etl.py config.py
git commit -m "Add data loading and database connection"

git add etl.py
git commit -m "Implement booking data cleaning (duplicates, dates, missing values)"

git add etl.py
git commit -m "Add enrichment and transformations"

git add etl.py
git commit -m "Save clean_bookings table to database"

git add queries.sql
git commit -m "Add revenue by destination SQL query"

git add README.md .gitignore bookings.db requirements.txt
git commit -m "Add project configuration and dependencies"
```

---

## Step 6: Push to Remote

```powershell
git push -u origin feature/salma-solution
```

You may be prompted for GitHub username and password/token. Use a **Personal Access Token** if 2FA is enabled: https://github.com/settings/tokens

---

## Step 7: Create Merge Request (on GitHub)

1. Go to: https://github.com/vtt-de-test/data-engineer-test-vtt-Salmaelbz
2. You should see a prompt to create a Pull Request for `feature/salma-solution`. Click **Compare & pull request**.
3. Fill in the description using the content from **MERGE_REQUEST.md**:
   - Approach
   - Data quality issues found
   - Decisions & assumptions
   - Improvements if given more time

---

## Step 8: Notify

Send the email as specified in the original test instructions (to the address they provided).

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `git` not recognized | Install Git and add it to PATH, then restart terminal |
| `Permission denied` or `Authentication failed` | Use a Personal Access Token instead of password |
| `remote origin already exists` | Use `git remote set-url origin ...` |
| `branch already exists` | Use `git checkout feature/salma-solution` first |
