import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacja Student")

        try:
            self.conn = sqlite3.connect("students.db")
            self.create_table()
        except sqlite3.Error as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd przy połączeniu z bazą danych:\n{str(e)}")
            root.quit()

        self.create_widgets()

    def create_table(self):
        try:
            query = """
                        CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            score1 INTEGER,
                            score2 INTEGER,
                            score3 INTEGER,
                            score4 INTEGER,
                            score5 INTEGER,
                            score6 INTEGER,
                            score7 INTEGER,
                            score8 INTEGER,
                            score9 INTEGER,
                            score10 INTEGER,
                            score11 INTEGER,
                            score12 INTEGER,
                            score13 INTEGER,
                            score14 INTEGER,
                            score15 INTEGER,
                            status TEXT
                        )
                    """
            self.conn.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd przy tworzeniu tabeli students:\n{str(e)}")
            self.root.quit()

    def create_widgets(self):
        self.student_listbox = tk.Listbox(self.root, width=150)
        self.student_listbox.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Dodaj", command=self.add_student)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edytuj", command=self.edit_student)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Usuń", command=self.delete_student)
        self.delete_button.pack(pady=5)

        self.update_student_listbox()

    def add_student(self):
        student_data = self.show_dialog("Dodaj studenta", "Podaj dane studenta (oddzielone przecinkami):",
                                        "email,imie,nazwisko,ocena1,ocena2,...,status")

        if student_data:
            data = student_data.split(",")

            if len(data) == 19:
                query = """
                    INSERT INTO students (email, first_name, last_name, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, score11, score12, score13, score14, score15, status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                self.conn.execute(query, data)
                self.conn.commit()

                self.update_student_listbox()
            else:
                self.show_message("Błąd", "Nieprawidłowa liczba wartości. Wprowadź wszystkie dane.")

    def edit_student(self):
        if self.student_listbox.curselection():
            index = self.student_listbox.curselection()[0]
            student_id = self.get_student_id(index)

            query = "SELECT * FROM students WHERE id = ?"
            result = self.conn.execute(query, (student_id,))
            student_data = result.fetchone()

            student_data_str = [str(value) if isinstance(value, int) else value for value in student_data[1:]]

            new_data = self.show_dialog("Edytuj studenta", "Edytuj dane studenta (oddzielone przecinkami):",
                                        ",".join(student_data_str))

            if new_data:
                query = """
                    UPDATE students SET email = ?, first_name = ?, last_name = ?, score1 = ?, score2 = ?, score3 = ?, score4 = ?, score5 = ?, score6 = ?, score7 = ?, score8 = ?, score9 = ?, score10 = ?, score11 = ?, score12 = ?, score13 = ?, score14 = ?, score15 = ?, status = ?
                    WHERE id = ?
                """
                self.conn.execute(query, tuple(new_data.split(",") + [student_id]))
                self.conn.commit()

                self.update_student_listbox()
        else:
            self.show_message("Błąd", "Zaznacz studenta, którego chcesz edytować.")

    def delete_student(self):
        if self.student_listbox.curselection():
            index = self.student_listbox.curselection()[0]
            student_id = self.get_student_id(index)

            query = "DELETE FROM students WHERE id = ?"
            self.conn.execute(query, (student_id,))
            self.conn.commit()

            self.update_student_listbox()
        else:
            self.show_message("Błąd", "Zaznacz studenta, którego chcesz usunąć.")

    def update_student_listbox(self):
        self.student_listbox.delete(0, tk.END)

        query = "SELECT * FROM students"
        result = self.conn.execute(query)
        students_data = result.fetchall()

        for student_data in students_data:
            student_id, email, first_name, last_name, *scores, status = student_data
            display_text = f"ID: {student_id}, Email: {email}, Imię: {first_name}, Nazwisko: {last_name}, Oceny: {', '.join(str(score) for score in scores)}, Status: {status}"
            self.student_listbox.insert(tk.END, display_text)

    def get_student_id(self, index):
        query = "SELECT id FROM students LIMIT 1 OFFSET ?"
        result = self.conn.execute(query, (index,))
        student_id = result.fetchone()[0]
        return student_id

    def show_dialog(self, title, message, default_value=""):
        return tk.simpledialog.askstring(title, message, initialvalue=default_value, parent=self.root)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
