import requests
import tkinter as tk


def update_messages():
    response = requests.get('http://localhost:5000/messages')
    messages = response.json()
    text = "\n".join([f"[{msg['timestamp']}]: {msg['message']}" for msg in messages])

    chat.configure(state='normal')
    chat.replace("1.0", "end", text)
    chat.config(state='disabled')

def send_message():
    message = entry.get()
    entry.delete(0, 'end')
    requests.post('http://localhost:5000/messages', json={'message': message})
    update_messages()

if __name__ == "__main__":
    window = tk.Tk()
    window.title('Anonymous chat application')
    window.resizable(width=False, height=False)

    chat = tk.Text(font=("Arial", 14), height=20, width=50)

    frame = tk.Frame(window)

    entry = tk.Entry(frame,width=50)
    entry.grid(column=0, row=0, padx=10)

    send = tk.Button(frame,
            text="Send",
            width=4,
            height=1,
            command=send_message
    )
    send.grid(column=1, row=0, padx=10)

    update = tk.Button(frame,
            text="Update",
            width=5,
            height=1,
            command=update_messages
    )
    update.grid(column=2, row=0, padx=10)

    update_messages()

    chat.pack()
    frame.pack()

    window.mainloop()

