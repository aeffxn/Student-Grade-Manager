"""
app.py

Student Grade Manager — GUI application. Made by Aeffxn.

Architecture:
    models.py   -> Student data class 
    storage.py  -> JSON load/save 
    app.py      -> this file 
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional

from models import Student
from storage import load_students, save_students


# ---------------------------------------------------------------------------
# Color palette 
# ---------------------------------------------------------------------------
BG_BLACK = "#0d0d0d"          # main app background
PANEL_BLACK = "#161616"       # slightly lighter panels/cards
BORDER_GREY = "#2a2a2a"       # subtle separators
YELLOW = "#FFC800"            # primary accent (buttons, highlights)
YELLOW_HOVER = "#FFD93D"      # lighter yellow for hover state
YELLOW_PRESSED = "#E0AD00"    # darker yellow for pressed state
TEXT_WHITE = "#F2F2F2"        # primary text on black
TEXT_GREY = "#9A9A9A"         # secondary / muted text
DANGER_RED = "#E5484D"        # delete action only

FONT_FAMILY = "Segoe UI"      # falls back gracefully on non-Windows systems
FONT_TITLE = (FONT_FAMILY, 20, "bold")
FONT_SUBTITLE = (FONT_FAMILY, 10)
FONT_LABEL = (FONT_FAMILY, 10, "bold")
FONT_BODY = (FONT_FAMILY, 10)
FONT_STAT_VALUE = (FONT_FAMILY, 22, "bold")
FONT_STAT_LABEL = (FONT_FAMILY, 9)


class YellowButton(tk.Button):
    """
    A flat, custom-styled button used for primary actions.

    """

    def __init__(self, master, text, command, danger=False, **kwargs):
        self._base_bg = DANGER_RED if danger else YELLOW
        self._hover_bg = "#F2666B" if danger else YELLOW_HOVER
        self._press_bg = "#C73E42" if danger else YELLOW_PRESSED

        super().__init__(
            master,
            text=text,
            command=command,
            bg=self._base_bg,
            fg=BG_BLACK,
            activebackground=self._press_bg,
            activeforeground=BG_BLACK,
            font=FONT_LABEL,
            relief="flat",
            bd=0,
            padx=14,
            pady=8,
            cursor="hand2",
            **kwargs,
        )
        self.bind("<Enter>", lambda e: self.config(bg=self._hover_bg))
        self.bind("<Leave>", lambda e: self.config(bg=self._base_bg))


class GradeManagerApp:
    """Top-level controller that wires together the UI and the data layer."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.students = load_students()
        self.selected_index: Optional[int] = None

        self._configure_root()
        self._configure_styles()
        self._build_layout()
        self._refresh_table()
        self._refresh_stats()

    # -- setup ---------------------------------------------------------

    def _configure_root(self):
        self.root.title("Student Grade Manager")
        self.root.geometry("980x600")
        self.root.minsize(860, 540)
        self.root.configure(bg=BG_BLACK)

        # Save to disk automatically when the window is closed.
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _configure_styles(self):
    
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=PANEL_BLACK,
            fieldbackground=PANEL_BLACK,
            foreground=TEXT_WHITE,
            rowheight=30,
            borderwidth=0,
            font=FONT_BODY,
        )
        style.map(
            "Treeview",
            background=[("selected", YELLOW)],
            foreground=[("selected", BG_BLACK)],
        )
        style.configure(
            "Treeview.Heading",
            background=BG_BLACK,
            foreground=YELLOW,
            font=FONT_LABEL,
            borderwidth=0,
            relief="flat",
        )
        style.map("Treeview.Heading", background=[("active", BG_BLACK)])

        style.configure(
            "Vertical.TScrollbar",
            background=PANEL_BLACK,
            troughcolor=BG_BLACK,
            bordercolor=BG_BLACK,
            arrowcolor=YELLOW,
            relief="flat",
        )

    # -- layout ----------------------------------------------------------

    def _build_layout(self):
        # Header --------------------------------------------------------
        header = tk.Frame(self.root, bg=BG_BLACK)
        header.pack(side="top", fill="x", padx=24, pady=(20, 10))

        tk.Label(
            header, text="Student Grade Manager",
            bg=BG_BLACK, fg=YELLOW, font=FONT_TITLE,
        ).pack(anchor="w")
        tk.Label(
            header, text="Add students, record marks, and track performance. Made by Aeffxn.",
            bg=BG_BLACK, fg=TEXT_GREY, font=FONT_SUBTITLE,
        ).pack(anchor="w", pady=(2, 0))

        # Body: left form panel + right table/stats panel ---------------
        body = tk.Frame(self.root, bg=BG_BLACK)
        body.pack(side="top", fill="both", expand=True, padx=24, pady=(10, 20))
        body.columnconfigure(0, weight=0)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        self._build_form_panel(body)

        right = tk.Frame(body, bg=BG_BLACK)
        right.grid(row=0, column=1, sticky="nsew", padx=(16, 0))
        right.rowconfigure(0, weight=1)
        right.columnconfigure(0, weight=1)

        self._build_table_panel(right)
        self._build_stats_panel(right)

    def _build_form_panel(self, parent):
        panel = tk.Frame(parent, bg=PANEL_BLACK, width=260)
        panel.grid(row=0, column=0, sticky="ns")
        panel.grid_propagate(False)

        pad = {"padx": 18, "pady": (14, 4)}

        tk.Label(
            panel, text="ADD / UPDATE STUDENT", bg=PANEL_BLACK, fg=YELLOW,
            font=FONT_LABEL,
        ).pack(anchor="w", padx=18, pady=(18, 10))

        # Name field
        tk.Label(panel, text="Student name", bg=PANEL_BLACK, fg=TEXT_GREY,
                  font=FONT_BODY).pack(anchor="w", **pad)
        self.name_entry = self._styled_entry(panel)
        self.name_entry.pack(fill="x", padx=18)

        # Mark field
        tk.Label(panel, text="Mark to add (0-100)", bg=PANEL_BLACK, fg=TEXT_GREY,
                  font=FONT_BODY).pack(anchor="w", **pad)
        self.mark_entry = self._styled_entry(panel)
        self.mark_entry.pack(fill="x", padx=18)
        self.mark_entry.bind("<Return>", lambda e: self._add_mark())

        # Buttons
        btn_frame = tk.Frame(panel, bg=PANEL_BLACK)
        btn_frame.pack(fill="x", padx=18, pady=(18, 8))

        YellowButton(btn_frame, "Add Student", self._add_student).pack(fill="x", pady=4)
        YellowButton(btn_frame, "Add Mark to Selected", self._add_mark).pack(fill="x", pady=4)
        YellowButton(btn_frame, "Delete Selected", self._delete_student, danger=True).pack(fill="x", pady=4)

        tk.Frame(panel, bg=BORDER_GREY, height=1).pack(fill="x", padx=18, pady=14)

        tk.Label(
            panel,
            text="Select a row in the table to add marks\nor delete that student.",
            bg=PANEL_BLACK, fg=TEXT_GREY, font=FONT_SUBTITLE, justify="left",
        ).pack(anchor="w", padx=18)

    def _styled_entry(self, parent) -> tk.Entry:
        return tk.Entry(
            parent,
            bg=BG_BLACK,
            fg=TEXT_WHITE,
            insertbackground=YELLOW,   # cursor color
            relief="flat",
            font=FONT_BODY,
            highlightthickness=1,
            highlightbackground=BORDER_GREY,
            highlightcolor=YELLOW,
        )

    def _build_table_panel(self, parent):
        panel = tk.Frame(parent, bg=PANEL_BLACK)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.rowconfigure(1, weight=1)
        panel.columnconfigure(0, weight=1)

        tk.Label(
            panel, text="STUDENTS", bg=PANEL_BLACK, fg=YELLOW, font=FONT_LABEL,
        ).grid(row=0, column=0, sticky="w", padx=18, pady=(14, 8))

        table_frame = tk.Frame(panel, bg=PANEL_BLACK)
        table_frame.grid(row=1, column=0, sticky="nsew", padx=18, pady=(0, 14))
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        columns = ("name", "marks", "average", "highest", "lowest")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="browse",
        )
        headings = {
            "name": "Name", "marks": "Marks", "average": "Average",
            "highest": "Highest", "lowest": "Lowest",
        }
        widths = {"name": 160, "marks": 220, "average": 90, "highest": 90, "lowest": 90}
        for col in columns:
            self.tree.heading(col, text=headings[col])
            anchor = "w" if col in ("name", "marks") else "center"
            self.tree.column(col, width=widths[col], anchor=anchor)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.tree.bind("<<TreeviewSelect>>", self._on_select_row)

    def _build_stats_panel(self, parent):
        panel = tk.Frame(parent, bg=BG_BLACK)
        panel.grid(row=1, column=0, sticky="ew", pady=(16, 0))
        for i in range(3):
            panel.columnconfigure(i, weight=1)

        self.stat_top_var = tk.StringVar(value="—")
        self.stat_low_var = tk.StringVar(value="—")
        self.stat_class_avg_var = tk.StringVar(value="—")

        self._stat_card(panel, 0, "🏆 Highest Scorer", self.stat_top_var)
        self._stat_card(panel, 1, "📉 Lowest Scorer", self.stat_low_var)
        self._stat_card(panel, 2, "📊 Class Average", self.stat_class_avg_var)

    def _stat_card(self, parent, col, label, var):
        card = tk.Frame(parent, bg=PANEL_BLACK, padx=16, pady=14)
        card.grid(row=0, column=col, sticky="ew", padx=(0 if col == 0 else 8, 0))
        tk.Label(card, textvariable=var, bg=PANEL_BLACK, fg=YELLOW,
                  font=FONT_STAT_VALUE).pack(anchor="w")
        tk.Label(card, text=label, bg=PANEL_BLACK, fg=TEXT_GREY,
                  font=FONT_STAT_LABEL).pack(anchor="w", pady=(2, 0))

    # -- data operations ---------------------------------------------------

    def _add_student(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Missing name", "Please enter a student name.")
            return
        if any(s.name.lower() == name.lower() for s in self.students):
            messagebox.showwarning("Duplicate student", f"'{name}' already exists.")
            return

        self.students.append(Student(name=name))
        self.name_entry.delete(0, "end")
        self._refresh_table()
        self._refresh_stats()
        self._save()

    def _add_mark(self):
        if self.selected_index is None:
            messagebox.showinfo("No student selected", "Select a student in the table first.")
            return

        raw_mark = self.mark_entry.get().strip()
        try:
            mark = float(raw_mark)
        except ValueError:
            messagebox.showwarning("Invalid mark", "Please enter a numeric mark.")
            return

        if not (0 <= mark <= 100):
            messagebox.showwarning("Out of range", "Mark must be between 0 and 100.")
            return

        self.students[self.selected_index].add_mark(mark)
        self.mark_entry.delete(0, "end")
        self._refresh_table()
        self._refresh_stats()
        self._save()

    def _delete_student(self):
        if self.selected_index is None:
            messagebox.showinfo("No student selected", "Select a student in the table first.")
            return

        student = self.students[self.selected_index]
        confirmed = messagebox.askyesno(
            "Confirm delete", f"Delete '{student.name}' and all their marks?"
        )
        if not confirmed:
            return

        del self.students[self.selected_index]
        self.selected_index = None
        self._refresh_table()
        self._refresh_stats()
        self._save()

    def _on_select_row(self, event):
        selection = self.tree.selection()
        if not selection:
            self.selected_index = None
            return
        # The Treeview item id is set to the student's index (as a string).
        self.selected_index = int(selection[0])

    # -- refresh / rendering -------------------------------------------

    def _refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        for idx, student in enumerate(self.students):
            marks_display = ", ".join(f"{m:g}" for m in student.marks) if student.marks else "—"
            self.tree.insert(
                "", "end", iid=str(idx),
                values=(
                    student.name,
                    marks_display,
                    f"{student.average():.1f}" if student.marks else "—",
                    f"{student.highest():g}" if student.marks else "—",
                    f"{student.lowest():g}" if student.marks else "—",
                ),
            )

    def _refresh_stats(self):
        students_with_marks = [s for s in self.students if s.marks]

        if not students_with_marks:
            self.stat_top_var.set("—")
            self.stat_low_var.set("—")
            self.stat_class_avg_var.set("—")
            return

        top = max(students_with_marks, key=lambda s: s.average())
        low = min(students_with_marks, key=lambda s: s.average())
        class_avg = sum(s.average() for s in students_with_marks) / len(students_with_marks)

        self.stat_top_var.set(f"{top.name}")
        self.stat_low_var.set(f"{low.name}")
        self.stat_class_avg_var.set(f"{class_avg:.1f}")

    # -- persistence -----------------------------------------------------

    def _save(self):
        save_students(self.students)

    def _on_close(self):
        self._save()
        self.root.destroy()


def main():
    root = tk.Tk()
    GradeManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()