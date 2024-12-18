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

