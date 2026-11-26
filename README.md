# 🔐 Password Strength Analyzer with Entropy Calculation

A Python-based desktop application that evaluates password security using multiple security parameters, calculates password entropy, detects weak patterns, and provides recommendations to create stronger passwords.

## 📌 Project Overview

The Password Strength Analyzer is a cybersecurity application developed using Python and Tkinter. It helps users understand how secure their passwords are by analyzing their length, character diversity, predictable patterns, and presence in a local leaked-password database.

The application generates a security score, classifies password strength, calculates entropy, and provides suggestions for improvement through a simple graphical user interface.

## 🎯 Objectives

- Evaluate password strength using multiple security parameters.
- Calculate password entropy to estimate password complexity.
- Identify commonly used and weak password patterns.
- Detect passwords present in a local leaked-password database.
- Provide personalized password improvement suggestions.
- Generate strong random passwords.
- Promote cybersecurity awareness and secure password practices.

## ✨ Features

- **Password Strength Analysis:** Evaluates passwords based on different security criteria.
- **Security Score:** Assigns a score out of 100.
- **Entropy Calculation:** Estimates password randomness and complexity.
- **Leaked Password Detection:** Checks passwords against a locally stored password database.
- **Weak Pattern Detection:** Identifies predictable patterns and commonly used words.
- **Strength Classification:** Categorizes passwords as Very Weak, Weak, Moderate, Strong, or Very Strong.
- **Password Suggestions:** Provides recommendations to improve password security.
- **Strong Password Generator:** Generates random passwords using different character types.
- **Show/Hide Password:** Allows users to view or conceal their passwords.
- **Copy Password:** Copies generated passwords to the clipboard.
- **Graphical User Interface:** Provides a simple and interactive desktop interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Tkinter | Graphical user interface |
| Regular Expressions (re) | Password pattern validation |
| Math | Entropy calculation |
| Random | Password generation |
| String | Character selection |

## ⚙️ System Requirements

**Software Requirements**
- Python 3.x
- Windows / Linux / macOS
- VS Code, PyCharm, or IDLE

**Hardware Requirements**
- Minimum 4 GB RAM
- Intel Core i3 or equivalent processor
- At least 100 MB free storage

## 🚀 Installation and Execution

**Step 1: Clone the repository**

```bash
git clone <your-repository-link>
```

**Step 2: Navigate to the project folder**

```bash
cd Password-Strength-Analyzer
```

**Step 3: Run the application**

```bash
python your_file_name.py
```

Replace `your_file_name.py` with the actual name of your Python application file.

**Note:** Tkinter is included with many standard Python installations. If it is unavailable, install the appropriate Tkinter package for your operating system.

## 💻 How to Use

1. Launch the application.
2. Enter a password in the input field.
3. Click the **Analyze Password** button.
4. View the password strength, security score, and entropy value.
5. Read the suggestions provided to improve password security.
6. Use the **Generate Strong Password** option to create a secure password.
7. Use the **Copy Password** button to copy the generated password.

## 📊 Password Strength Categories

| Category | Description |
|---|---|
| Very Weak | Highly predictable password |
| Weak | Password with several security weaknesses |
| Moderate | Password with basic security characteristics |
| Strong | Password with good complexity |
| Very Strong | Password with high complexity and fewer predictable characteristics |

## 📁 Project Files

- Python application file – Contains the main application and analysis logic.
- `leaked_passwords.txt` – Local database used for leaked-password detection.
- `README.md` – Project documentation.

## ⚠️ Limitations

- Uses predefined rule-based password analysis.
- Leaked-password detection depends on the local database.
- Does not perform real-time online breach verification.
- Does not currently use machine learning algorithms.
- Designed primarily as a desktop application.

## 🔮 Future Enhancements

- Integration with online leaked-password databases.
- Machine learning-based password analysis.
- Web and mobile application development.
- Integration with password management systems.
- Enhanced security recommendations and reporting.

## 🔒 Privacy and Security

The application is designed for local password analysis. Passwords should not be shared or uploaded to public repositories. The local leaked-password database is used for comparison.

**Important:** This application is an educational cybersecurity project and should not be considered a replacement for professional password security tools.

## 👩‍💻 Author

**Name:** [Your Name]  
**Department:** Computer Science and Engineering  
**Project:** Password Strength Analyzer with Entropy Calculation

---

⭐ If you find this project useful, consider giving the repository a star!
