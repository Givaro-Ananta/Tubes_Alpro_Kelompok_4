import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class ExamApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Exam Simulation")
        self.master.geometry("500x400")
        self.master.configure(bg="#ffffff")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#ffffff')
        
        # Base button style
        self.style.configure('TButton',
                           padding=(10, 8),
                           font=('Helvetica', 10),
                           background='#ffffff',
                           borderwidth=1,
                           relief='solid')
        
        self.style.map('TButton',
                      background=[('active', '#e0e0e0')])
        
        # Custom button styles
        self.style.configure('Login.TButton',
                           padding=(10, 8),
                           font=('Helvetica', 10),
                           background='#ffffff',
                           borderwidth=1,
                           relief='solid')
        
        self.style.configure('Register.TButton',
                           padding=(10, 8),
                           font=('Helvetica', 10),
                           background='#ffffff',
                           borderwidth=1,
                           relief='solid')
        
        # Label styles
        self.style.configure('TLabel',
                           font=('Helvetica', 10),
                           background='#ffffff')
        self.style.configure('Header.TLabel',
                           font=('Helvetica', 20, 'bold'),
                           background='#ffffff')
        
        # Initialize user dictionaries for different roles
        self.admin_users = {"admin": "admin123"}  # Default admin account
        self.participant_users = {}
        self.current_user = None
        self.current_role = None
        self.questions = {}
        self.user_scores = {}  # Dictionary to store user scores
        
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        self.login_screen()
    
    def create_entry(self, parent, show=None):
        entry = ttk.Entry(parent, width=25, font=('Helvetica', 10))
        if show:
            entry.configure(show=show)
        return entry

    def login_screen(self):
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, text="Exam App", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        # Login form
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(pady=10)
        
        ttk.Label(form_frame, text="Username").pack(anchor="w", pady=(0, 5))
        self.username_entry = self.create_entry(form_frame)
        self.username_entry.pack(pady=(0, 15))
        
        ttk.Label(form_frame, text="Password").pack(anchor="w", pady=(0, 5))
        self.password_entry = self.create_entry(form_frame, show="*")
        self.password_entry.pack(pady=(0, 15))
        
        btn_frame = ttk.Frame(form_frame)
        btn_frame.pack(pady=5)
        
        login_btn = ttk.Button(btn_frame, text="Login", command=self.login,
                              style='Login.TButton', width=20)
        login_btn.pack(pady=5)
        
        # Add Register button
        register_btn = ttk.Button(btn_frame, text="Register", 
                                command=self.register_screen,
                                style='Register.TButton', width=20)
        register_btn.pack(pady=5)
        
        # Admin login link
        admin_btn = ttk.Button(form_frame, text="Login as Admin", 
                             command=self.admin_login_screen,
                             style='Register.TButton', width=20)
        admin_btn.pack(pady=5)

    def register_screen(self):
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, text="Register Account", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(pady=10)
        
        ttk.Label(form_frame, text="Username").pack(anchor="w", pady=(0, 5))
        self.reg_username_entry = self.create_entry(form_frame)
        self.reg_username_entry.pack(pady=(0, 15))
        
        ttk.Label(form_frame, text="Password").pack(anchor="w", pady=(0, 5))
        self.reg_password_entry = self.create_entry(form_frame, show="*")
        self.reg_password_entry.pack(pady=(0, 15))
        
        ttk.Label(form_frame, text="Confirm Password").pack(anchor="w", pady=(0, 5))
        self.reg_confirm_password_entry = self.create_entry(form_frame, show="*")
        self.reg_confirm_password_entry.pack(pady=(0, 15))
        
        btn_frame = ttk.Frame(form_frame)
        btn_frame.pack(pady=5)
        
        register_btn = ttk.Button(btn_frame, text="Register", 
                                command=self.register_account,
                                style='Login.TButton', width=20)
        register_btn.pack(pady=5)
        
        back_btn = ttk.Button(btn_frame, text="Back to Login", 
                            command=self.login_screen,
                            style='Register.TButton', width=20)
        back_btn.pack(pady=5)

    def register_account(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        confirm_password = self.reg_confirm_password_entry.get()
        
        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        if username in self.participant_users or username in self.admin_users:
            messagebox.showerror("Error", "Username already exists")
            return
        
        self.participant_users[username] = password
        self.user_scores[username] = []  # Initialize empty scores list for new user
        messagebox.showinfo("Success", "Account registered successfully")
        self.login_screen()

    def admin_login_screen(self):
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, text="Admin Login", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(pady=10)
        
        ttk.Label(form_frame, text="Admin Username").pack(anchor="w", pady=(0, 5))
        self.admin_username_entry = self.create_entry(form_frame)
        self.admin_username_entry.pack(pady=(0, 15))
        
        ttk.Label(form_frame, text="Admin Password").pack(anchor="w", pady=(0, 5))
        self.admin_password_entry = self.create_entry(form_frame, show="*")
        self.admin_password_entry.pack(pady=(0, 15))
        
        btn_frame = ttk.Frame(form_frame)
        btn_frame.pack(pady=5)
        
        login_btn = ttk.Button(btn_frame, text="Login as Admin", 
                             command=self.admin_login,
                             style='Login.TButton', width=20)
        login_btn.pack(pady=5)
        
        back_btn = ttk.Button(btn_frame, text="Back to Participant Login", 
                            command=self.login_screen,
                            style='Register.TButton', width=20)
        back_btn.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.participant_users and self.participant_users[username] == password:
            self.current_user = username
            self.current_role = "participant"
            self.participant_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def admin_login(self):
        username = self.admin_username_entry.get()
        password = self.admin_password_entry.get()
        
        if username in self.admin_users and self.admin_users[username] == password:
            self.current_user = username
            self.current_role = "admin"
            self.admin_screen()
        else:
            messagebox.showerror("Error", "Invalid admin credentials")

    def admin_screen(self):
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, 
                          text=f"Welcome Admin: {self.current_user}",
                          style='Header.TLabel')
        header.pack(pady=(0, 15))
        
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        
        actions = [
            ("Create Question", self.create_question),
            ("Delete Question", self.delete_question),
            ("View All Questions", self.view_questions),
            ("View All Scores", self.view_all_scores),  # New action
            ("Logout", self.login_screen)
        ]
        
        for text, command in actions:
            btn = ttk.Button(btn_frame, text=text, command=command,
                           style='Register.TButton', width=20)
            btn.pack(pady=5)

    def participant_screen(self):
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, 
                          text=f"Welcome {self.current_user}",
                          style='Header.TLabel')
        header.pack(pady=(0, 15))
        
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        
        actions = [
            ("Take Exam", self.take_exam),
            ("View My Scores", self.view_my_scores),  # New action
            ("Logout", self.login_screen)
        ]
        
        for text, command in actions:
            btn = ttk.Button(btn_frame, text=text, command=command,
                           style='Register.TButton', width=20)
            btn.pack(pady=5)

    def view_questions(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("All Questions")
        view_window.geometry("400x300")
        
        frame = ttk.Frame(view_window)
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ttk.Label(frame, text="Questions and Answers", 
                 style='Header.TLabel').pack(pady=(0, 10))
        
        text_widget = tk.Text(frame, wrap=tk.WORD, width=40, height=12)
        text_widget.pack(pady=10)
        
        for question, answer in self.questions.items():
            text_widget.insert(tk.END, f"Q: {question}\nA: {answer}\n\n")
        
        text_widget.configure(state='disabled')
        
        ttk.Button(frame, text="Close", command=view_window.destroy,
                  style='Login.TButton', width=20).pack(pady=5)

    def view_my_scores(self):
        if self.current_user not in self.user_scores or not self.user_scores[self.current_user]:
            messagebox.showinfo("No Scores", "You haven't taken any exams yet")
            return
            
        view_window = tk.Toplevel(self.master)
        view_window.title("My Scores")
        view_window.geometry("300x400")
        
        frame = ttk.Frame(view_window)
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ttk.Label(frame, text="My Exam Scores", 
                 style='Header.TLabel').pack(pady=(0, 10))
        
        text_widget = tk.Text(frame, wrap=tk.WORD, width=30, height=15)
        text_widget.pack(pady=10)
        
        for i, score in enumerate(self.user_scores[self.current_user], 1):
            text_widget.insert(tk.END, f"Attempt {i}: {score:.2f}/100\n")
        
        avg_score = sum(self.user_scores[self.current_user]) / len(self.user_scores[self.current_user])
        text_widget.insert(tk.END, f"\nAverage Score: {avg_score:.2f}/100")
        
        text_widget.configure(state='disabled')
        
        ttk.Button(frame, text="Close", command=view_window.destroy,
                  style='Login.TButton', width=20).pack(pady=5)

    def view_all_scores(self):
        if not any(self.user_scores.values()):
            messagebox.showinfo("No Scores", "No exam scores available yet")
            return
            
        view_window = tk.Toplevel(self.master)
        view_window.title("All User Scores")
        view_window.geometry("400x500")
        
        frame = ttk.Frame(view_window)
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ttk.Label(frame, text="All User Scores", 
                 style='Header.TLabel').pack(pady=(0, 10))
        
        text_widget = tk.Text(frame, wrap=tk.WORD, width=40, height=20)
        text_widget.pack(pady=10)
        
        for username, scores in self.user_scores.items():
            if scores:
                text_widget.insert(tk.END, f"\nUser: {username}\n")
                for i, score in enumerate(scores, 1):
                    text_widget.insert(tk.END, f"Attempt {i}: {score:.2f}/100\n")
                avg_score = sum(scores) / len(scores)
                text_widget.insert(tk.END, f"Average Score: {avg_score:.2f}/100\n")
                text_widget.insert(tk.END, "-" * 40 + "\n")
        
        text_widget.configure(state='disabled')
        
        ttk.Button(frame, text="Close", command=view_window.destroy,
                  style='Login.TButton', width=20).pack(pady=5)

    def take_exam(self):
        self.clear_frame(self.main_frame)
        
        self.score = 0
        self.current_question_index = 0
        self.question_keys = list(self.questions.keys())
        
        if not self.question_keys:
            messagebox.showerror("Error", "No questions available")
            self.participant_screen()
            return
        
        header = ttk.Label(self.main_frame, text="Exam in Progress", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        self.question_frame = ttk.Frame(self.main_frame)
        self.question_frame.pack(pady=10, fill="both", expand=True)
        
        self.show_question()

    def show_question(self):
        self.clear_frame(self.question_frame)
        
        if self.current_question_index >= len(self.question_keys):
            self.finish_exam()
            return
        
        current_question = self.question_keys[self.current_question_index]
        
        # Question number and text
        question_label = ttk.Label(self.question_frame, 
                                 text=f"Question {self.current_question_index + 1} of {len(self.question_keys)}",
                                 style='TLabel')
        question_label.pack(pady=(0, 10))
        
        question_text = ttk.Label(self.question_frame, text=current_question,
                                wraplength=400, style='TLabel')
        question_text.pack(pady=(0, 20))
        
        # Answer entry
        self.answer_entry = ttk.Entry(self.question_frame, width=40)
        self.answer_entry.pack(pady=(0, 20))
        
        # Navigation buttons
        btn_frame = ttk.Frame(self.question_frame)
        btn_frame.pack(pady=10)
        
        if self.current_question_index > 0:
            prev_btn = ttk.Button(btn_frame, text="Previous",
                                command=self.previous_question,
                                style='Register.TButton', width=15)
            prev_btn.pack(side="left", padx=5)
        
        next_btn = ttk.Button(btn_frame, text="Next",
                            command=self.submit_answer,
                            style='Login.TButton', width=15)
        next_btn.pack(side="left", padx=5)

    def previous_question(self):
        self.current_question_index -= 1
        self.show_question()

    def submit_answer(self):
        current_question = self.question_keys[self.current_question_index]
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[current_question].strip().lower()
        
        if user_answer == correct_answer:
            self.score += 1
        
        self.current_question_index += 1
        self.show_question()

    def finish_exam(self):
        final_score = (self.score / len(self.question_keys)) * 100
        
        # Store the score
        if self.current_user not in self.user_scores:
            self.user_scores[self.current_user] = []
        self.user_scores[self.current_user].append(final_score)
        
        # Show results
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, text="Exam Complete!", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        score_label = ttk.Label(self.main_frame, 
                              text=f"Your Score: {final_score:.2f}%\n"
                                   f"Correct Answers: {self.score} out of {len(self.question_keys)}",
                              style='TLabel')
        score_label.pack(pady=(0, 20))
        
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Return to Menu",
                  command=self.participant_screen,
                  style='Login.TButton', width=20).pack(pady=5)

    def create_question(self):
        question = simpledialog.askstring("New Question", "Enter the question:")
        if question:
            answer = simpledialog.askstring("New Answer", "Enter the answer:")
            if answer:
                self.questions[question] = answer
                messagebox.showinfo("Success", "Question added successfully")

    def delete_question(self):
        if not self.questions:
            messagebox.showerror("Error", "No questions available")
            return
            
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Question")
        delete_window.geometry("400x300")
        
        frame = ttk.Frame(delete_window)
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ttk.Label(frame, text="Select Question to Delete",
                 style='Header.TLabel').pack(pady=(0, 10))
        
        listbox = tk.Listbox(frame, width=40, height=10)
        listbox.pack(pady=10)
        
        for question in self.questions:
            listbox.insert(tk.END, question)
        
        def delete_selected():
            selection = listbox.curselection()
            if selection:
                question = listbox.get(selection[0])
                del self.questions[question]
                delete_window.destroy()
                messagebox.showinfo("Success", "Question deleted successfully")
            else:
                messagebox.showerror("Error", "Please select a question")
        
        ttk.Button(frame, text="Delete",
                  command=delete_selected,
                  style='Login.TButton', width=20).pack(pady=5)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExamApp(root)
    root.mainloop()
    
#akun admin: 
#username: admin
#password: admin123
