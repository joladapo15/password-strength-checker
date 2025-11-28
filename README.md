# 🔐 Password Strength Checker (Python)

A simple Python tool that analyzes a password and gives **real-time feedback** every time you enter a new password.  
This project checks for:

- Uppercase letters (A–Z)
- Lowercase letters (a–z)
- Numbers (0–9)
- Special characters (!@#$%^& etc.)
- Minimum length requirement

It then assigns a **strength rating**: `Weak`, `Moderate`, or `Strong`.

---

## 🚀 Features

- ✔️ Real-time feedback in the terminal  
- ✔️ Strength scoring system  
- ✔️ Beginner-friendly Python  
- ✔️ No external libraries required  
- ✔️ Great starter project for IT / Cybersecurity portfolios  

---

## 📌 How It Works

When you run the program, you can enter a password and instantly see:

- Which character requirements are met
- Password length
- Overall strength rating

You can keep testing passwords until you type:
done


---

## 🧠 Logic Behind the Strength Score

Each of these adds **1 point** to the score:

- Contains uppercase letters  
- Contains lowercase letters  
- Contains digits  
- Contains special characters  
- Password length ≥ 8  

Total score ranges from **0 to 5**.

Strength levels:

| Score | Strength  |
|-------|-----------|
| 0–2   | Weak      |
| 3–4   | Moderate  |
| 5     | Strong    |

---

## 🖥️ Example Output

Enter a password (or type 'done' to exit): Ab3@

Feedback:
Uppercase: ✓
Lowercase: ✓
Digit: ✓
Special: ✓
Length: 4 characters
Password strength: Moderate

---

## 📚 Skills Demonstrated

- Python input handling  
- Loops and conditionals  
- Character classification (isupper, islower, isdigit)  
- Basic cybersecurity concepts  
- Score-based evaluation  
- Clean, readable code structure  

---

## 🤝 Future Improvements

Ideas you can build later:

- Masked input (hide password while typing)
- GUI version with Tkinter
- Password generator
- Entropy-based strength scoring
- Save password tests to logs

---







