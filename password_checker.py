
def analyze_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False 

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    score = 0 

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if len(password) >= 8:
        score += 1

    return has_upper, has_lower, has_digit, has_special, len(password), score 

while True:
    password = input("Enter a password(or type 'done to exit): ")

    if password.lower() == "done":
        break

    has_upper, has_lower, has_digit, has_special, length, score = analyze_password(password)

    print("\nFeedback:")
    print("Uppercase:",  "✓" if has_upper else "✗")
    print("Lowercase:",  "✓" if has_lower else "✗")
    print("Digit:",      "✓" if has_digit else "✗")
    print("Special:",    "✓" if has_special else "✗")
    print(f" Length: {length} characters")



    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("Password strength: ", strength)


