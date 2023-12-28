import tkinter as tk
import requests
from tkinter import messagebox

class DiscordWebhookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Discord Webhook Sender")
        self.root.geometry("500x300")  # Увеличиваем размер окна

        self.webhook_entry_label = tk.Label(root, text="Webhook URL:")
        self.webhook_entry_label.pack(pady=5)

        self.webhook_entry = tk.Entry(root, width=40)
        self.webhook_entry.pack(pady=5)

        self.bot_name_label = tk.Label(root, text="Имя бота:")
        self.bot_name_label.pack(pady=5)

        self.bot_name_entry = tk.Entry(root, width=40)
        self.bot_name_entry.pack(pady=5)

        self.bot_avatar_label = tk.Label(root, text="URL аватарки бота:")
        self.bot_avatar_label.pack(pady=5)

        self.bot_avatar_entry = tk.Entry(root, width=40)
        self.bot_avatar_entry.pack(pady=5)

        self.message_entry_label = tk.Label(root, text="Сообщение:")
        self.message_entry_label.pack(pady=5)

        self.message_entry = tk.Entry(root, width=40)
        self.message_entry.pack(pady=10)

        send_button = tk.Button(root, text="Отправить", command=self.send_message, height=2, width=20)
        send_button.pack()

    def send_message(self):
        webhook_url = self.webhook_entry.get()

        if not webhook_url:
            messagebox.showwarning("Внимание", "Введите URL webhook перед отправкой!")
            return

        bot_name = self.bot_name_entry.get()
        bot_avatar_url = self.bot_avatar_entry.get()

        message = self.message_entry.get()

        if not message:
            messagebox.showwarning("Внимание", "Введите сообщение перед отправкой!")
            return

        payload = {
            "username": bot_name,
            "avatar_url": bot_avatar_url,
            "content": message
        }

        try:
            response = requests.post(webhook_url, json=payload)
            response.raise_for_status()
            messagebox.showinfo("Успех", "Сообщение успешно отправлено в Discord!")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Ошибка при отправке сообщения: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiscordWebhookApp(root)
    root.mainloop()
