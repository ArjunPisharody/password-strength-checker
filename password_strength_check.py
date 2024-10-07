import re

def check_password_strength(password):
    score=0
    feedback=[]

    conditions=[
        (r".{8,}","Password is too short. Minimum 8 characters required."),
        (r"[A-Z]","Password should contain at least one uppercase letter."),
        (r"[a-z]","Password should contain at least one lowercase letter."),
        (r"\d","Password should contain at least one digit."),
        (r"[!@#$%^&*(),.?\":{}|<>]", "Password should contain at least one special character.")
    ]

    for pattern,message in conditions:
        if re.search(pattern,password):
            score+=1
        else:
            feedback.append(message)
    if score==5:
        return "Strong password!",feedback
    elif 3<=score<5:
        return "moderate password. think about imporving it",feedback
    else:
        return "weak password. better impove it",feedback

def main():
    password=input("Enter the password: ")

    strength,feedback=check_password_strength(password)

    print(f"Password Strength: {strength}")

    if feedback:
        print("Feedback for improvement: ")
        for tip in feedback:
            print(f"- {tip}")

if __name__=="__main__":
    main()
