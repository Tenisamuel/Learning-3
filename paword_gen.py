#collects user preferences f
# - length 
# - special characters
# - use of the password
# - should contain upper case
# - should contain lower case

# get all all available characters
# randomly select characters from the length.
#ensure one of each character type
#ensure length is valid and a good amount to for the user to remember.
#import tkinter as tk
#import random




import tkinter as tk

# ---------------- PASSWORD LOGIC (UNCHANGED, JUST PARAMETERIZED) ----------------
#The initial program has been wiped in other to facilitate the tkinter commands.
#The function generate_password_from_ui holds all the necessary parameters that hoolds necessary information and 
#prompts of the user.
def generate_password_from_ui(length, include_uppercase, include_lowercase, include_digits, include_special):
    import random, string

    if length < 4: #If the number of characters in the password is less than 4 it makes it easier to guess and is 
        #suceptible to hackers.
        return "Password must be at least 4 characters."

    lowercase_letters = string.ascii_lowercase if include_lowercase else ""
    uppercase_letters = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_digits else ""
    special_characters = string.punctuation if include_special else ""
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    #First block of code validates and checks the specific input and crtiteria of depepending on the users choice.
    #Ascii is used to store all possible characters for: special characters, numbers, letters(upper case,lowercase)
    if not all_characters:
        return "No character types selected."
    #Another set of validation that enables the user to filter what is needed in their password.
    required_characters = []
    if include_uppercase:
        required_characters.append(random.choice(uppercase_letters))
    if include_lowercase:
        required_characters.append(random.choice(lowercase_letters))
    if include_digits:
        required_characters.append(random.choice(digits))
    if include_special:
        required_characters.append(random.choice(special_characters))
#The block of code above ensures the final password contains at least one 
#character out of all the requirements. It is crucial that 
#a strong password is created to make it harder for exploiters and data minors 
# To gain access to user information and data.
    remaining_length = length - len(required_characters)
    password = list(required_characters)

    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return "".join(password)

# ---------------- MODERN UI ----------------

def run_ui():
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("520x420")
    window.configure(bg="#1e1e1e")
    #Creates the actual application, title and its size.
    frame = tk.Frame(window, bg="#2d2d2d", bd=2, relief="ridge")
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    #Frames are used to make the UI look neater
    tk.Label(frame, text="Random Password Generator", font=("Segoe UI", 18, "bold"),
             fg="#00d4ff", bg="#2d2d2d").pack(pady=10)

    # Length input
    tk.Label(frame, text="Password Length:", font=("Segoe UI", 12), fg="white", bg="#2d2d2d").pack()
    length_entry = tk.Entry(frame, font=("Segoe UI", 12), width=10)
    length_entry.pack(pady=5)

    # Checkboxes
    uppercase_var = tk.BooleanVar()
    lowercase_var = tk.BooleanVar()
    digits_var = tk.BooleanVar()
    special_var = tk.BooleanVar()

    tk.Checkbutton(frame, text="Include Uppercase", variable=uppercase_var,
                   font=("Segoe UI", 11), fg="white", bg="#2d2d2d",
                   activebackground="#ADD8E6").pack(anchor="w", padx=20)

    tk.Checkbutton(frame, text="Include Lowercase", variable=lowercase_var,
                   font=("Segoe UI", 11), fg="white", bg="#2d2d2d",
                   activebackground="#ADD8E6").pack(anchor="w", padx=20)

    tk.Checkbutton(frame, text="Include Digits", variable=digits_var,
                   font=("Segoe UI", 11), fg="white", bg="#2d2d2d",
                   activebackground="#ADD8E6").pack(anchor="w", padx=20)

    tk.Checkbutton(frame, text="Include Special Characters", variable=special_var,
                   font=("Segoe UI", 11), fg="white", bg="#2d2d2d",
                   activebackground= "#ADD8E6").pack(anchor="w", padx=20)

    # Output label
    output_label = tk.Label(frame, text="", font=("Segoe UI", 14), fg="#00ff88",
                            bg="#2d2d2d", wraplength=450)
    output_label.pack(pady=15)

    # Generate button
    def generate_and_show():
        try:
            length = int(length_entry.get())
        except ValueError:
            output_label.config(text="Please enter a valid number.")
            return

        password = generate_password_from_ui(
            length,
            uppercase_var.get(),
            lowercase_var.get(),
            digits_var.get(),
            special_var.get()
        )
        output_label.config(text=password)

    tk.Button(frame, text="Generate Password", command=generate_and_show,
              font=("Segoe UI", 14, "bold"), bg="#00d4ff", fg="black",
              activebackground="#009ec2", width=20).pack(pady=10)

    # Copy button
    def copy_password():
        window.clipboard_clear()
        window.clipboard_append(output_label.cget("text"))

    tk.Button(frame, text="Copy to Clipboard", command=copy_password,
              font=("Segoe UI", 12), bg="#3a3a3a", fg="white",
              activebackground="#555555", width=20).pack(pady=5)

    window.mainloop()

run_ui()

