from random import choice
import yaml

# Separated into a file so that it is easier to expand
FILE_NAME = "utilities\color_codes.yml"

with open(FILE_NAME, "r") as color_file:
    color_codes = yaml.load(color_file)


def get_color_name() -> str:
    return choice([color_name for color_name in color_codes])


def get_color_code() -> str:
    return choice([color_code for color_code in color_codes.values()])


def invert_color_code(color_code: str) -> str:
    # 16777215 -> int("ffffff", 16)
    return "#" + hex(16777215 - int(color_code[1:], 16))[2:].rjust(6, "0")


if __name__ == "__main__":
    import tkinter as tk

    def button_colour():
        color_name = get_color_name()
        color_code = color_codes[color_name]
        # might want to use only black and white
        inverted_code = invert_color_code(color_code)
        color_display_name.set(color_name)
        changer_button.config(
            bg=color_code, fg=inverted_code, activebackground=inverted_code, activeforeground=color_code
        )
        root.config(bg=color_code)

    root = tk.Tk()
    root.title(string="Popular Colors")

    color_display_name = tk.StringVar()
    color_display_name.set("Color")

    changer_button = tk.Button(
        root,
        font="Helvetica 15",
        relief=tk.FLAT,
        height=2,
        width=18,
        textvariable=color_display_name,
        command=button_colour,
    )
    changer_button.pack()

    root.mainloop()
