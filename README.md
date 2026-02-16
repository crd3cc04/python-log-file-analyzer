# 🐍 Python Log File Analyzer

A lightweight Python script that scans log files and generates a summary of INFO, WARNING, and ERROR messages. This project demonstrates practical automation skills used in IT, DevOps, and cybersecurity environments.

---

## 🚀 Features

- Counts INFO, WARNING, and ERROR messages  
- Extracts and analyzes error messages  
- Identifies the most common error    
- Fully tested with pytest  

---

## 📁 Project Structure

```
python-log-file-analyzer/
│
├── src/
|   ├── init.py
│   └── log_analyzer.py
│
├── sample_logs/
│   └── system.log
|
├── tests/
|   └── test_log_analyzer.py
|
├── conftest.py
│
└── README.md
```

---

## ▶️ How to Run

From the project root:

```bash
python3 src/log_analyzer.py
```

---

## 🧪 Sample Output

```
===== Log File Summary =====
Total INFO messages: 3
Total WARNING messages: 1
Total ERROR messages: 2

Most common error: 'Backup process failed' occurred 1 times
```

---

## 🧪 Running Tests

To run the full test suite:

```bash
pytest -v
```

## 📘 Sample Log Format

```code
2024-06-01 12:00:00 INFO User logged in
2024-06-01 12:00:00 ERROR Something broke
```
Malfromed lines are automatically detected and marked as:
```code
level = 'UNKNOWN"
timestamp = None
```

---

## 📌 Why This Project Matters

This script demonstrates:

- Python automation  
- Log parsing  
- Pattern recognition  
- Error analysis  
- Real‑world IT troubleshooting skills  

Perfect for showcasing practical scripting ability on a GitHub portfolio.

---

## 🔧 Future Enhancements

- Export results to CSV  
- Add colorized terminal output  
- Support for multiple log formats  
- Regex‑based filtering
- Add CLI interface
- Add JSON output option
- Add summary export to file  
