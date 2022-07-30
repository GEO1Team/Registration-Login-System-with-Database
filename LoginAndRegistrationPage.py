from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
from tkinter import messagebox


class LoginClient(Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.geometry('1350x718')
        # window.state('zoomed')
        self.resizable(0, 0)
        self.title('Login and Registration Page')

        # Window Icon Photo
        self.icon = PhotoImage(file='images\\pic-icon.png')
        self.iconphoto(True, self.icon)

        self.LoginPage = Frame(self)
        self.RegistrationPage = Frame(self)

        for frame in (self.LoginPage, self.RegistrationPage):
            frame.grid(row=0, column=0, sticky='nsew')


        self.show_frame(self.LoginPage)


        # # ========== DATABASE VARIABLES ============
        # Email = StringVar()
        # FullName = StringVar()
        # Password = StringVar()
        # ConfirmPassword = StringVar()

        # =====================================================================================================================
        # =====================================================================================================================
        # ==================== LOGIN PAGE =====================================================================================
        # =====================================================================================================================
        # =====================================================================================================================

        self.design_frame1 = Listbox(self.LoginPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
        self.design_frame1.place(x=0, y=0)

        self.design_frame2 = Listbox(self.LoginPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
        self.design_frame2.place(x=676, y=0)

        self.design_frame3 = Listbox(self.LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
        self.design_frame3.place(x=75, y=106)

        self.design_frame4 = Listbox(self.LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
        self.design_frame4.place(x=676, y=106)

        # ====== Email ====================
        self.email_entry = Entry(self.design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
        self.email_entry.place(x=134, y=170, width=256, height=34)
        self.email_entry.config(highlightbackground="black", highlightcolor="black")
        self.email_label = Label(self.design_frame4, text='• Email account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        self.email_label.place(x=130, y=140)

        # ==== Password ==================
        self.password_entry1 = Entry(self.design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
        self.password_entry1.place(x=134, y=250, width=256, height=34)
        self.password_entry1.config(highlightbackground="black", highlightcolor="black")
        self.password_label = Label(self.design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        self.password_label.place(x=130, y=220)





        # ====== checkbutton ==============
        self.checkButton = Checkbutton(self.design_frame4, bg='#f8f8f8', command=self.password_command, text='show password')
        self.checkButton.place(x=140, y=288)

        # ========= Buttons ===============
        self.SignUp_button = Button(self.LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                            command=lambda: self.show_frame(self.RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
        self.SignUp_button.place(x=1100, y=175)

        # ===== Welcome Label ==============
        # welcome_label = Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
        # welcome_label.place(x=130, y=15)

        # ======= top Login Button =========
        self.login_button = Button(self.LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                            borderwidth=0, activebackground='#1b87d2', cursor='hand2')
        self.login_button.place(x=845, y=175)

        self.login_line = Canvas(self.LoginPage, width=60, height=5, bg='#1b87d2')
        self.login_line.place(x=840, y=203)

        # ==== LOGIN  down button ============
        self.loginBtn1 = Button(self.design_frame4, fg='#f8f8f8', text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                        cursor='hand2', activebackground='#1b87d2', command=lambda: self.login())
        self.loginBtn1.place(x=133, y=340, width=256, height=50)


        # ======= ICONS =================

        # ===== Email icon =========
        self.email_icon = Image.open('images\\email-icon.png')
        self.photo = ImageTk.PhotoImage(self.email_icon)
        self.emailIcon_label = Label(self.design_frame4, image=self.photo, bg='#f8f8f8')
        self.emailIcon_label.image = self.photo
        self.emailIcon_label.place(x=105, y=174)

        # ===== password icon =========
        self.password_icon = Image.open('images\\pass-icon.png')
        self.photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.design_frame4, image=self.photo, bg='#f8f8f8')
        self.password_icon_label.image = self.photo
        self.password_icon_label.place(x=105, y=254)

        # ===== picture icon =========
        self.picture_icon = Image.open('images\\pic-icon.png')
        self.photo = ImageTk.PhotoImage(self.picture_icon)
        self.picture_icon_label = Label(self.design_frame4, image=self.photo, bg='#f8f8f8')
        self.picture_icon_label.image = self.photo
        self.picture_icon_label.place(x=280, y=5)

        # ===== Left Side Picture ============
        side_image = Image.open('images\\GEO1 An NV5 Company.png')
        self.photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(self.design_frame3, image=self.photo, bg='#1e85d0')
        side_image_label.image = self.photo
        side_image_label.place(x=50, y=140)





        # ===================================================================================================================
        # ===================================================================================================================
        # === FORGOT PASSWORD  PAGE =========================================================================================
        # ===================================================================================================================
        # ===================================================================================================================

        self.forgotPassword = Button(self.design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                                borderwidth=0, activebackground='#f8f8f8', command=lambda: self.forgot_password(), cursor="hand2")
        self.forgotPassword.place(x=290, y=290)

        # =====================================================================================================================
        # =====================================================================================================================
        # ==================== REGISTRATION PAGE ==============================================================================
        # =====================================================================================================================
        # =====================================================================================================================

        self.design_frame5 = Listbox(self.RegistrationPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
        self.design_frame5.place(x=0, y=0)

        self.design_frame6 = Listbox(self.RegistrationPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
        self.design_frame6.place(x=676, y=0)

        self.design_frame7 = Listbox(self.RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
        self.design_frame7.place(x=75, y=106)

        self.design_frame8 = Listbox(self.RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
        self.design_frame8.place(x=676, y=106)

        # ==== Full Name =======
        self.name_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
        self.name_entry.place(x=284, y=150, width=286, height=34)
        self.name_entry.config(highlightbackground="black", highlightcolor="black")
        self.name_label = Label(self.design_frame8, text='First & Last Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        self.name_label.place(x=280, y=120)

        # ======= Email ===========
        self.email_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
        self.email_entry.place(x=284, y=220, width=286, height=34)
        self.email_entry.config(highlightbackground="black", highlightcolor="black")
        self.email_label = Label(self.design_frame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        self.email_label.place(x=280, y=190)

        # ====== Password =========
        self.password_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
        self.password_entry.place(x=284, y=295, width=286, height=34)
        self.password_entry.config(highlightbackground="black", highlightcolor="black")
        self.password_label = Label(self.design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                            font=("yu gothic ui", 11, 'bold'))
        self.password_label.place(x=280, y=265)





        self.checkButton = Checkbutton(self.design_frame8, bg='#f8f8f8', command=self.password_command, text='show password')
        self.checkButton.place(x=290, y=330)


        # ====== Confirm Password =============
        self.confirmPassword_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2, show='•')
        self.confirmPassword_entry.place(x=284, y=385, width=286, height=34)
        self.confirmPassword_entry.config(highlightbackground="black", highlightcolor="black")
        self.confirmPassword_label = Label(self.design_frame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                    font=("yu gothic ui", 11, 'bold'))
        self.confirmPassword_label.place(x=280, y=355)

        # ========= Buttons ====================
        self.SignUp_button = Button(self.RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                            command=lambda: self.show_frame(self.LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
        self.SignUp_button.place(x=1100, y=175)

        self.SignUp_line = Canvas(self.RegistrationPage, width=60, height=5, bg='#1b87d2')
        self.SignUp_line.place(x=1100, y=203)

        # # ===== Welcome Label ==================
        # welcome_label = Label(design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
        # welcome_label.place(x=130, y=15)

        # ========= Login Button =========
        self.login_button = Button(self.RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                            borderwidth=0, activebackground='#1b87d2', command=lambda: self.show_frame(self.LoginPage), cursor='hand2')
        self.login_button.place(x=845, y=175)

        # ==== SIGN UP down button ============
        self.signUp2 = Button(self.design_frame8, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                        cursor='hand2', activebackground='#1b87d2', command=lambda: self.submit())
        self.signUp2.place(x=285, y=435, width=286, height=50)

        # ===== password icon =========
        self.password_icon = Image.open('images\\pass-icon.png')
        self.photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.design_frame8, image=self.photo, bg='#f8f8f8')
        self.password_icon_label.image = self.photo
        self.password_icon_label.place(x=255, y=300)

        # ===== confirm password icon =========
        self.confirmPassword_icon = Image.open('images\\pass-icon.png')
        self.photo = ImageTk.PhotoImage(self.confirmPassword_icon)
        self.confirmPassword_icon_label = Label(self.design_frame8, image=self.photo, bg='#f8f8f8')
        self.confirmPassword_icon_label.image = self.photo
        self.confirmPassword_icon_label.place(x=255, y=390)

        # ===== Email icon =========
        self.mail_icon = Image.open('images\\email-icon.png')
        self.photo = ImageTk.PhotoImage(self.email_icon)
        self.emailIcon_label = Label(self.design_frame8, image=self.photo, bg='#f8f8f8')
        self.emailIcon_label.image = self.photo
        self.emailIcon_label.place(x=255, y=225)

        # ===== Full Name icon =========
        self.name_icon = Image.open('images\\name-icon.png')
        self.photo = ImageTk.PhotoImage(self.name_icon)
        self.nameIcon_label = Label(self.design_frame8, image=self.photo, bg='#f8f8f8')
        self.nameIcon_label.image = self.photo
        self.nameIcon_label.place(x=252, y=153)

        # ===== picture icon =========
        self.picture_icon = Image.open('images\\pic-icon.png')
        self.photo = ImageTk.PhotoImage(self.picture_icon)
        self.picture_icon_label = Label(self.design_frame8, image=self.photo, bg='#f8f8f8')
        self.picture_icon_label.image = self.photo
        self.picture_icon_label.place(x=280, y=5)

        # ===== Left Side Picture ============
        self.side_image = Image.open('images\\GEO1 An NV5 Company.png')
        self.photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.design_frame7, image=self.photo, bg='#1e85d0')
        self.side_image_label.image = self.photo
        self.side_image_label.place(x=50, y=140)


    def show_frame(self, frame):
        frame.tkraise()

        # function for show and hide password
    def password_command(self):
        if self.password_entry1.cget('show') == '•':
            self.password_entry1.config(show='')
            self.password_entry.config(show='')
            self.confirmPassword_entry.config(show='')
        else:
            self.password_entry1.config(show='•')
            self.password_entry.config(show='•')
            self.confirmPassword_entry.config(show='•')

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry1.get()
        result = email == "chandlertayek@gmail.com" and password =="123"
        # Check if their account is confirmed or not and ask for them to confirm
        # Let them confirm again
        print("Message if they need to confirm account")
        if result:
            messagebox.showinfo("Success", 'Logged in Successfully.')
            print("Move to the tool program with JWT or other creds")
            self.destroy()
        else:
            messagebox.showerror("Failed", "Wrong Login details, please try again.")

    def forgot_password(self):
        # self.withdraw()
        win = Toplevel()
        window_width = 350
        window_height = 350
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        win.title('Forgot Password')
        win.iconbitmap('images\\aa.ico')
        win.configure(background='#f8f8f8')
        win.resizable(0, 0)

        # Variables
        email = StringVar()
        password = StringVar()
        confirmPassword = StringVar()

        # ====== Email ====================
        email_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
        email_entry2.place(x=40, y=30, width=256, height=34)
        email_entry2.config(highlightbackground="black", highlightcolor="black")
        email_label2 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                            font=("yu gothic ui", 11, 'bold'))
        email_label2.place(x=40, y=0)

        # ====  New Password ==================
        new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
        new_password_entry.place(x=40, y=110, width=256, height=34)
        new_password_entry.config(highlightbackground="black", highlightcolor="black")
        new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        new_password_label.place(x=40, y=80)

        # ====== checkbutton ==============
        checkButton_reset_pass = Checkbutton(win, name='reset_pass', bg='#f8f8f8', command=lambda: password_command2(), text='show password')
        checkButton_reset_pass.place(x=40, y=150)

        # ====  Confirm Password ==================
        confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2
                                    , textvariable=confirmPassword)
        confirm_password_entry.place(x=40, y=220, width=256, height=34)
        confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
        confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                    font=("yu gothic ui", 11, 'bold'))
        confirm_password_label.place(x=40, y=180)

        # ======= Update password Button ============
        update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                            cursor='hand2', activebackground='#1b87d2', command=lambda: change_password())
        update_pass.place(x=40, y=260, width=256, height=50)

        # ========= DATABASE CONNECTION FOR FORGOT PASSWORD=====================
        def change_password():
            if new_password_entry.get() == confirm_password_entry.get():
                messagebox.showinfo('Congrats', 'Password changed successfully', parent=win)
                # self.deiconify()
                win.destroy()
            else:
                messagebox.showerror('Error!', "Passwords didn't match", parent=win)

        def password_command2():
            if new_password_entry.cget('show') == '•':
                new_password_entry.config(show='')
                confirm_password_entry.config(show='')
            else:
                new_password_entry.config(show='•')
                confirm_password_entry.config(show='•')

    def submit(self):
        check_counter = 0
        warn = ""
        if self.name_entry.get() == "":
            warn = "Full Name can't be empty"
        else:
            check_counter += 1

        if self.email_entry.get() == "":
            warn = "Email Field can't be empty"
        else:
            check_counter += 1

        if self.password_entry.get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1

        if self.confirmPassword_entry.get() == "":
            warn = "Sorry, can't sign up make sure all fields are complete"
        else:
            check_counter += 1

        if self.password_entry.get() != self.confirmPassword_entry.get():
            warn = "Passwords didn't match!"
        else:
            check_counter += 1

        if check_counter == 5:
            messagebox.showinfo("Success", "New account created successfully")
        else:
            messagebox.showerror('Error', warn)

def main():
    login_client = LoginClient()
    login_client.mainloop()

if __name__ == "__main__":
    main()