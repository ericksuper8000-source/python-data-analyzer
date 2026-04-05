# Sales Data Analyzer 📊

## 📌 Project Overview

This project is a simple data analysis application built with Python. It processes sales data from a CSV file and provides basic insights such as total sales, units sold, and best-selling products.

The goal of this project is to demonstrate foundational data analysis skills using tools like **pandas** and **matplotlib**, while keeping the implementation simple and easy to understand.

---

## 🚀 Features

* Load and process sales data from a CSV file
* Explore dataset structure (rows, columns, data types)
* Filter sales by a specific date
* Calculate:

  * Total revenue per day
  * Total units sold
  * Best-selling product
* Visualize total units sold per product using a bar chart

---

## 🧠 Key Concepts Used

* Data loading with `pandas`
* Data exploration (`shape`, `dtypes`, `head`)
* Data filtering
* Aggregations with `groupby`
* Basic data visualization with `matplotlib`
* Handling user input and date parsing

---

## 📊 Visualization

The project includes a simple bar chart showing:

> **Total units sold by product**

This helps quickly identify the most popular products.

---

## 🏗️ Project Structure

```
sales-analyzer/
│
├── data/
│   └── sales.csv
│
├── src/
│   └── load_data.py
│
├── main.py
└── README.md
```

---

## ⚙️ How to Run

1. Install dependencies:

```
pip install pandas matplotlib
```

2. Run the application:

```
python main.py
```

3. Enter a date when prompted:

```
YYYY-MM-DD
```

---

## 🧾 Design Decisions

* **Simplicity over complexity**:
  The project avoids advanced patterns (like classes or complex architecture) to focus on core concepts.

* **Step-by-step data flow**:
  The application follows a clear sequence:

  ```
  Load → Explore → Filter → Analyze → Visualize
  ```

* **Use of pandas**:
  Chosen for its simplicity and wide use in real-world data analysis.

* **Basic visualization**:
  A simple bar chart was selected to keep the project readable while still adding value.

---

## ⏱️ Development Process

This project was built incrementally over multiple sessions, focusing on learning and understanding each step rather than rushing into complexity.

Approximate breakdown:

* Data loading and exploration: ~1 session
* Basic analysis (metrics and filtering): ~2 sessions
* Visualization: ~1 session
* Code cleanup and improvements: ~1 session

Total: ~5 focused sessions

---

## 🎯 Purpose of the Project

This project is part of my learning process as a junior developer. It is intended to:

* Practice working with real datasets
* Strengthen Python and pandas skills
* Build a portfolio project that reflects real-world tasks at an entry level

---

## 🔧 Future Improvements

* Add more visualizations (e.g., sales over time)
* Improve user interaction (menu system)
* Export reports
* Handle missing or inconsistent data

---

## 👨‍💻 Author

Erick Perez

---