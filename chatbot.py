import nltk
import random
import string
import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# تحسين أزواج الأسئلة والإجابات
pairs = [
    [r"hello|hi|hey", ["Hello! 😊", "Hi there! How can I assist?", "Hey! Need any help?"]],
    [r"how are you", ["I'm great! How about you?", "Feeling good today! What about you?"]],
    [r"what is your name", ["I'm ChatBot 2.0!", "You can call me SmartBot."]],
    [r"bye|goodbye", ["Goodbye! Have a nice day! 👋", "See you later!", "Bye! Take care."]],
    [r"(.*) your name", ["I'm an AI chatbot, and you?", "I go by many names, but you can call me ChatGPT!"]],
    [r"(.*) help", ["I'm here to assist! What do you need help with?", "Sure! Tell me what you need."]],
    [r"(.*) your age", ["I exist in the digital world, so I don't age!", "I'm timeless!"]],
    [r"who created you", ["I was created by a team of developers using Python!", "I am a product of artificial intelligence."]],
    [r"(.*) weather", ["I can't check the weather right now, but you can try a weather app!", "I don't have live updates, but I hope it's sunny!"]],
    [r"(.*)", ["I'm not sure I understand, could you rephrase?", "Hmm, can you ask in another way?"]],
]

# إنشاء نموذج الشات بوت
chatbot = Chat(pairs, reflections)

# تحسين واجهة المستخدم باستخدام Tkinter
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot 🤖")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")

      
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='disabled', font=("Arial", 12), bg="white")
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

 
        self.user_input = tk.Entry(root, width=40, font=("Arial", 12))
        self.user_input.grid(row=1, column=0, padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message)  # إرسال بالضغط على Enter

    
        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.send_button.grid(row=1, column=1, padx=5, pady=10)

        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_chat, font=("Arial", 12), bg="#FF5733", fg="white")
        self.clear_button.grid(row=2, column=0, columnspan=2, pady=5)

      
        self.update_chat("🤖 Chatbot: Hello! Type 'bye' to exit.")

    # 
    def send_message(self, event=None):
        user_text = self.user_input.get().strip().lower()
        if user_text:
            self.update_chat("You: " + user_text)
            response = chatbot.respond(user_text)
            if response:
                self.update_chat("🤖 Chatbot: " + response)
            else:
                self.update_chat("🤖 Chatbot: Sorry, I didn't understand that.")
            self.user_input.delete(0, tk.END)

    
    def update_chat(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

    
    def clear_chat(self):
        self.chat_display.config(state='normal')
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.config(state='disabled')
        self.update_chat("🤖 Chatbot: Hello! Type 'bye' to exit.")

#تشغيل التطبيق
if __name__ == "__main__":
    root = tk.Tk()
    chat_gui = ChatbotGUI(root)
    root.mainloop()
