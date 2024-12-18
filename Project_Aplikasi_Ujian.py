import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# ExamApp class: Kelas utama yang mengelola aplikasi ujian
# Menyediakan fitur untuk admin dan peserta ujian
class ExamApp:
    import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class ExamApp:
    def __init__(self, master):
        # Fungsi inisialisasi yang mengatur window utama dan styling
        # - Mengatur judul, ukuran, dan konfigurasi dasar window
        # - Menginisialisasi style untuk tombol, label, dan frame
        # - Menyiapkan dictionary untuk user admin dan peserta
        # - Menyiapkan dictionary untuk menyimpan soal dan nilai
        self.master = master
        self.master.title("Exam Simulation")
        self.master.geometry("500x400")
        self.master.configure(bg="#ffffff")
        
        # Konfigurasi style untuk tampilan UI
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
        
        # Border frame style
        self.style.configure('Border.TFrame', 
                           borderwidth=1, 
                           relief='solid', 
                           background='#ffffff')
        
        # Menginisialisasi dictionary user untuk role yang berbeda
        self.admin_users = {"admin": "admin123"}  # Akun default admin
        self.participant_users = {}  # Dictionary untuk menyimpan akun peserta
        self.current_user = None  # Menyimpan user yang sedang login
        self.current_role = None  # Menyimpan role user (admin/participant)
        
        # Daftar Soal
        self.questions = {
            "Siapa presiden pertama Republik Indonesia?": "Ir. Soekarno",
            "Berapa jumlah planet dalam system tata surya?": "Delapan",
            "Apa nama gunung tertinggi di dunia?": "Gunung Everest", 
            "Apa nama planet yang memiliki cincin?": "Saturnus",
            "Siapa tokoh yang dijuluki sebagai Bapak Pendidikan Indonesia?": "Ki Hajar Dewantara", 
            "Kapan Indonesia merdeka? (tanggal-bulan-tahun)": "17-08-1945",
            "Apa nama mata uang Indonesia?": "Rupiah",
            "Berapa lama masa jabatan presiden Indonesia?": "5 tahun",
            "Pulau manakah yang dijuluki Pulau Dewata?": "Bali",
            "Apa nama selat yang memisahkan Pulau Jawa dan Sumatra?": "Selat Sunda",
        }
        
        self.user_scores = {}  # Dictionary untuk menyimpan skor pengguna
        
        # Membuat frame utama
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        self.login_screen() # Menampilkan layar login saat aplikasi dimulai
    
    def create_entry(self, parent, show=None):
        # Fungsi helper untuk membuat entry field dengan style yang konsisten
        # Parameter show digunakan untuk input password (menampilkan *)
        entry = ttk.Entry(parent, width=25, font=('Helvetica', 10))
        if show:
            entry.configure(show=show)
        return entry

    def login_screen(self):
        # Fungsi untuk menampilkan layar login
        # - Menampilkan form login untuk peserta
        # - Menyediakan opsi untuk register dan login admin
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, text="Exam App", style='Header.TLabel')
        header.pack(pady=(0, 20))
        
        # Setup form login
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
                              style='Login.TButton', width=25)
        login_btn.pack(pady=5)
        
        # Membuat Register button
        register_btn = ttk.Button(btn_frame, text="Register", 
                                command=self.register_screen,
                                style='Register.TButton', width=25)
        register_btn.pack(pady=5)
        
        # Halaman Login (admin)
        admin_btn = ttk.Button(form_frame, text="Login as Admin", 
                             command=self.admin_login_screen,
                             style='Register.TButton', width=25)
        admin_btn.pack(pady=5)

    def register_screen(self):
        # Fungsi untuk menampilkan layar registrasi
        # - Menyediakan form untuk membuat akun baru
        # - Memvalidasi input dan menyimpan akun baru
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
        # Fungsi untuk memproses registrasi akun baru
        # - Validasi input (username unik, password match)
        # - Menyimpan akun baru ke dictionary participant_users
        # - Inisialisasi array kosong untuk menyimpan nilai
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
        # Fungsi untuk menampilkan layar login admin
        # - Form khusus untuk login admin
        # - Validasi kredensial admin
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
                             style='Login.TButton', width=25)
        login_btn.pack(pady=5)
        
        back_btn = ttk.Button(btn_frame, text="Back to Participant Login", 
                            command=self.login_screen,
                            style='Register.TButton', width=25)
        back_btn.pack(pady=5)

    def login(self):
        # Fungsi untuk memproses login peserta
        # - Validasi kredensial peserta
        # - Mengatur current_user dan current_role
        # - Mengarahkan ke layar peserta jika berhasil
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.participant_users and self.participant_users[username] == password:
            self.current_user = username
            self.current_role = "participant"
            self.participant_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def admin_login(self):
        # Fungsi untuk memproses login admin
        # - Validasi kredensial admin
        # - Mengatur current_user dan current_role
        # - Mengarahkan ke layar admin jika berhasil
        username = self.admin_username_entry.get()
        password = self.admin_password_entry.get()
        
        if username in self.admin_users and self.admin_users[username] == password:
            self.current_user = username
            self.current_role = "admin"
            self.admin_screen()
        else:
            messagebox.showerror("Error", "Invalid admin credentials")

    def admin_screen(self):
        # Fungsi untuk menampilkan dashboard admin
        # - Menampilkan menu untuk manajemen soal
        # - Opsi untuk melihat nilai semua peserta
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
            ("View All Scores", self.view_all_scores),  
            ("Logout", self.login_screen)
        ]
        
        for text, command in actions:
            btn = ttk.Button(btn_frame, text=text, command=command,
                           style='Register.TButton', width=20)
            btn.pack(pady=5)

    def participant_screen(self):
        # Fungsi untuk menampilkan dashboard peserta
        # - Menu untuk mengerjakan ujian
        # - Opsi untuk melihat nilai sendiri
        self.clear_frame(self.main_frame)
        
        header = ttk.Label(self.main_frame, 
                          text=f"Welcome {self.current_user}",
                          style='Header.TLabel')
        header.pack(pady=(0, 15))
        
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        
        actions = [
            ("Take Exam", self.take_exam),
            ("View My Scores", self.view_my_scores),  
            ("Logout", self.login_screen)
        ]
        
        for text, command in actions:
            btn = ttk.Button(btn_frame, text=text, command=command,
                           style='Register.TButton', width=20)
            btn.pack(pady=5)

    def view_questions(self):
        # Fungsi untuk menampilkan semua soal (admin only)
        # - Menampilkan soal dan jawaban dalam window terpisah
        view_window = tk.Toplevel(self.master)
        view_window.title("All Questions")
        view_window.geometry("400x300")
        
        frame = ttk.Frame(view_window, style='Border.TFrame')
        frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ttk.Label(frame, text="Questions and Answers", 
                 style='Header.TLabel').pack(pady=(0, 10))
        
        text_widget = tk.Text(frame, wrap=tk.WORD, width=40, height=12, 
                             borderwidth=1, relief='solid')
        text_widget.pack(pady=10)
        
        for question, answer in self.questions.items():
            text_widget.insert(tk.END, f"Q: {question}\nA: {answer}\n\n")
        
        text_widget.configure(state='disabled')
        
        ttk.Button(frame, text="Close", command=view_window.destroy,
                  style='Login.TButton', width=20).pack(pady=5)

