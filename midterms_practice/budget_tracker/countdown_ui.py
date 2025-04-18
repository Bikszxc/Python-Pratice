import tkinter as tk

def generate_cd(n):
    for i in range(n, -1, -1):
        yield i

def start_countdown(n):
    frame_main.pack_forget()
    
    frame_cd = tk.Frame(root)
    frame_cd.pack(fill="both", expand=True)

    label_cd = tk.Label(frame_cd, text="", font=("Arial", 36))
    label_cd.pack(expand=True)

    cd_gen = generate_cd(n)

    def update_count():
        try:
            num = next(cd_gen)
            label_cd.config(text=num)
            root.after(1000, update_count)
        except StopIteration:
            frame_cd.pack_forget()
            frame_main.pack(fill="both", expand=True)

    update_count()

def get_time():
    try:
        seconds = int(entry_seconds.get())
        label_error.pack_forget()
        start_countdown(seconds)
    except ValueError:
        label_error.pack(pady=50)

root = tk.Tk()
root.geometry("250x250")
root.title("Countdowner")

frame_main = tk.Frame(root)
frame_main.pack(fill="both", expand=True)

label_seconds = tk.Label(frame_main, text="Enter number of seconds:")
label_seconds.pack()

entry_seconds = tk.Entry(frame_main, font=("Arial", 18), justify="center")
entry_seconds.pack()

btn_start = tk.Button(frame_main, text="Start!", command=get_time)
btn_start.pack(pady=20)

label_error = tk.Label(frame_main, text="Please enter a valid input!", fg="red")

root.mainloop()
