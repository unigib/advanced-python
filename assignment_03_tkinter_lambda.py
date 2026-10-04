"""Assignment 3: use lambda to pass an argument to a Tkinter button callback."""

import tkinter as tk


def main() -> None:
    window = tk.Tk()
    window.title("Assignment 3: Button Callbacks")
    window.resizable(False, False)

    message = tk.StringVar(value="Click a button to choose a greeting.")
    tk.Label(window, textvariable=message, padx=20, pady=20).pack()

    def show_greeting(greeting: str) -> None:
        message.set(greeting)

    def reset_message() -> None:
        message.set("Click a button to choose a greeting.")

    # Tkinter calls each command later, when the button is clicked.
    tk.Button(
        window,
        text="Say hello",
        command=lambda: show_greeting("Hello!"),
    ).pack(fill="x", padx=20, pady=4)
    tk.Button(
        window,
        text="Say good morning",
        command=lambda: show_greeting("Good morning!"),
    ).pack(fill="x", padx=20, pady=4)
    tk.Button(
        window,
        text="Say goodbye",
        command=lambda: show_greeting("Goodbye!"),
    ).pack(fill="x", padx=20, pady=4)

    # A function that takes no arguments can be passed directly.
    tk.Button(window, text="Reset", command=reset_message).pack(
        fill="x", padx=20, pady=(4, 20)
    )

    window.mainloop()


if __name__ == "__main__":
    main()
