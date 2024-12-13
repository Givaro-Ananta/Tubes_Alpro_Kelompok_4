import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class ExamApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Exam Simulation")
        self.master.geometry("500x400")
        self.master.configure(bg="#f0f2f5")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f2f5')
        self.style.configure('TButton',
                           padding=10,
                           font=('Helvetica', 10),
                           background='#1a73e8')
        
        # Custom button styles with different colors
        self.style.configure('Login.TButton',
                           background='#4CAF50',
                           padding=10,
                           font=('Helvetica', 10))
        
        self.style.configure('Register.TButton',
                           background='#2196F3',
                           padding=10,
                           font=('Helvetica', 10))
        
        self.style.configure('TLabel',
                           font=('Helvetica', 10),
                           background='#f0f2f5')
        self.style.configure('Header.TLabel',
                           font=('Helvetica', 20, 'bold'),
                           background='#f0f2f5')
        
        self.users = {}
        self.current_user = None
        self.questions = {}
        
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        self.login_screen()
    
    def create_entry(self, parent, show=None):
        entry = ttk.Entry(parent, width=30, font=('Helvetica', 10))
        if show:
            entry.configure(show=show)
        return entry

    def login_screen(self):
        self.clear_frame(self.main_frame)
        
        # Header
        header = ttk.Label(self.main_frame, text="Exam App", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        # Login form container
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(fill="x", padx=20)
        
        ttk.Label(form_frame, text="Username").pack(anchor="w", pady=(0, 5))
        self.username_entry = self.create_entry(form_frame)
        self.username_entry.pack(fill="x", pady=(0, 15))
        
        ttk.Label(form_frame, text="Password").pack(anchor="w", pady=(0, 5))
        self.password_entry = self.create_entry(form_frame, show="*")
        self.password_entry.pack(fill="x", pady=(0, 20))
        
        # Buttons container
        btn_frame = ttk.Frame(form_frame)
        btn_frame.pack(fill="x", pady=10)
        
        login_btn = ttk.Button(btn_frame, text="Login", command=self.login,
                              style='Login.TButton', width=20)
        login_btn.pack(pady=5)
        
        register_btn = ttk.Button(btn_frame, text="Create Account", 
                                command=self.register_screen,
                                style='Register.TButton', width=20)
        register_btn.pack(pady=5)

    def register_screen(self):
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, text="Create Account", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(fill="x", padx=20)
        
        ttk.Label(form_frame, text="Username").pack(anchor="w", pady=(0, 5))
        self.reg_username_entry = self.create_entry(form_frame)
        self.reg_username_entry.pack(fill="x", pady=(0, 15))
        
        ttk.Label(form_frame, text="Password").pack(anchor="w", pady=(0, 5))
        self.reg_password_entry = self.create_entry(form_frame, show="*")
        self.reg_password_entry.pack(fill="x", pady=(0, 20))
        
        btn_frame = ttk.Frame(form_frame)
        btn_frame.pack(fill="x", pady=10)
        
        register_btn = ttk.Button(btn_frame, text="Register", 
                                command=self.register,
                                style='Register.TButton', width=20)
        register_btn.pack(pady=5)
        
        back_btn = ttk.Button(btn_frame, text="Back to Login", 
                            command=self.login_screen,
                            style='Login.TButton', width=20)
        back_btn.pack(pady=5)

    def exam_screen(self):
        self.clear_frame(self.main_frame)
        
        # Welcome message with username only appears after successful login
        header = ttk.Label(self.main_frame, 
                          text=f"Welcome {self.current_user}",
                          style='Header.TLabel')
        header.pack(pady=(0, 30))
        
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(expand=True)
        
        actions = [
            ("Create Question", self.create_question),
            ("Take Exam", self.take_exam),
            ("Delete Question", self.delete_question),
            ("Logout", self.login_screen)
        ]
        
        for text, command in actions:
            btn = ttk.Button(btn_frame, text=text, command=command,
                           style='Register.TButton', width=20)
            btn.pack(pady=10)

    def take_exam(self):
        self.clear_frame(self.main_frame)
        
        self.score = 0
        self.current_question_index = 0
        self.question_keys = list(self.questions.keys())
        
        if not self.question_keys:
            messagebox.showinfo("No Questions", "No questions available to take exam")
            self.exam_screen()
            return
        
        self.next_question()
    
    def next_question(self):
        if self.current_question_index < len(self.question_keys):
            question = self.question_keys[self.current_question_index]
            self.current_question_index += 1
            
            # Question number
            question_num = ttk.Label(self.main_frame,
                                   text=f"Question {self.current_question_index}/{len(self.question_keys)}",
                                   style='Header.TLabel')
            question_num.pack(pady=(0, 20))
            
            # Question text
            question_text = ttk.Label(self.main_frame, text=question,
                                    wraplength=400)
            question_text.pack(pady=(0, 20))
            
            # Answer entry
            self.answer_entry = self.create_entry(self.main_frame)
            self.answer_entry.pack(pady=(0, 20))
            
            # Submit button
            submit_btn = ttk.Button(self.main_frame, text="Submit Answer",
                                  command=lambda: self.check_answer(question),
                                  style='Login.TButton', width=20)
            submit_btn.pack()
        else:
            total_questions = len(self.questions)
            score_per_question = 100 / total_questions
            final_score = self.score * score_per_question
            messagebox.showinfo("Result", f"Your score is: {final_score:.2f}/100")
            self.exam_screen()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.users and self.users[username] == password:
            self.current_user = username
            self.exam_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        
        if username in self.users:
            messagebox.showerror("Error", "Username already exists")
        else:
            self.users[username] = password
            messagebox.showinfo("Success", "Registration successful")
            self.login_screen()
    
    def create_question(self):
        question = simpledialog.askstring("New Question", "Enter the question:")
        if question:
            answer = simpledialog.askstring("New Question", "Enter the answer:")
            if answer:
                self.questions[question] = answer
                messagebox.showinfo("Success", "Question added successfully")
    
    def delete_question(self):
        if not self.questions:
            messagebox.showinfo("No Questions", "There are no questions to delete")
            return
        
        # Create a new window for deleting questions
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Question")
        
        # Listbox to display questions
        listbox = tk.Listbox(delete_window, selectmode=tk.SINGLE, font=('Helvetica', 10), width=50, height=10)
        listbox.pack(pady=10)
        
        # Insert questions into listbox
        for question in self.questions.keys():
            listbox.insert(tk.END, question)
        
        # Button to confirm deletion
        delete_btn = ttk.Button(delete_window, text="Delete", command=lambda: self.confirm_delete(listbox, delete_window))
        delete_btn.pack(pady=5)
    
    def confirm_delete(self, listbox, delete_window):
        selected_question = listbox.get(tk.ACTIVE)
        if selected_question:
            del self.questions[selected_question]
            messagebox.showinfo("Success", "Question deleted successfully")
            delete_window.destroy()
        else:
            messagebox.showerror("Error", "No question selected")
    
    def check_answer(self, question):
        answer = self.answer_entry.get()
        if self.questions[question].lower() == answer.lower():
            self.score += 1
        self.clear_frame(self.main_frame)
        self.next_question()
    
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExamApp(root)
    root.mainloop()
