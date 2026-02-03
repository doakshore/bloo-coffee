# ☕ Bloo Coffee

**HarvardX CS50x Final Project (2023)** A full-stack web application built with **Python (Flask)**, **SQLite**, and **Jinja2**.

Bloo Coffee allows users to vote for their favorite coffee flavors, while administrators can securely manage data through a dedicated admin interface.

---

## 🎯 Product Vision & Summary

The project centered on developing a digital customer engagement ecosystem designed to bridge the gap between user feedback and business strategy. It serves as a strategic tool for gathering market insights and managing a dynamic product catalog.

* **Value Proposition:** Maximizing business impact by enabling real-time, data-driven decision-making in product development.
* **Product Strategy:** Managed the end-to-end lifecycle from concept to a production-ready Minimum Viable Product (MVP), overseeing both architecture design and implementation.

---

## 🔍 Technical & Business Deep Dive

### 🏗️ Backend Architecture & Scalability (Python & Flask)

The backend utilizes Python and Flask to ensure agile development and high solution customizability.

* **Architectural Integrity:** Follows the MVC (Model-View-Controller) pattern to decouple business logic from the UI, facilitating future growth and reducing technical debt.
* **Security & Risk Management:** Integrated `werkzeug.security` for password hashing and implemented strict input validation (including Regex-based password strength policies) to ensure data integrity and security.
* **Session Management:** Leveraged Flask sessions to maintain secure user journeys, which is critical for sustaining customer trust and protecting administrative routes.

### 📊 Data-Driven Decision Making (Database & Raw SQL)

The database layer was built using Raw SQL for maximum performance and full transparency in complex reporting.

* **Stakeholder Reporting (KPIs):** Developed advanced SQL queries (JOINs, GROUP BY) to transform raw data into business intelligence (e.g., "Top Flavors" reports), providing immediate visibility into market trends.
* **Schema Design:** Designed a normalized database structure to support scalability and efficient management of users, flavors, and voting data.

### 🎨 User Experience & Customer Insight (Frontend & UI/UX)

The platform was developed with a user-centric design focus, prioritizing responsiveness and clarity.

* **Efficiency:** Used Jinja2 template inheritance (DRY principle) to optimize development resources and accelerate time-to-market.
* **Interactive Admin Dashboard:** Integrated DataTables and Bootstrap 5 to allow administrators to manage large datasets effortlessly, enhancing operational efficiency.

---

## 🚀 Features

* **User voting:** Cast votes for coffee flavors on a clean and simple interface.
* **Admin dashboard:** Add new flavors, manage administrators, and view database entries.
* **Authentication & security:**
* Password hashing with `werkzeug.security`.
* Email validation (`validate_email`).
* Session management for secure logins.


* **Database:** SQLite backend for storing votes, users, and flavors.
* **Templates:** Modular UI built with Jinja2, including shared `base.html`.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Jinja2, Bootstrap 5
* **Database:** SQLite
* **Security:** Werkzeug, validate_email, Regex validation
* **Version Control:** GitHub

---

## 📂 Project Structure

* `app.py`: Main Flask application handling routing and business logic.
* `queries.py`: Centralized SQL query definitions and database interaction logic.
* `bloo.db`: SQLite database storing all application data.
* `templates/`: Jinja2 HTML templates for frontend rendering.
* `static/`: Contains CSS stylesheets and image assets.
* `package.json`: Defines frontend dependencies and libraries.
