import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from dataprocessor import calculate_score, detect_risk
from report import generate_pdf
from emailservice import send_email


class App:
    def __init__(self, root):

        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("800x500")

        self.data = None

        # -------- BUTTON FRAME --------
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Upload CSV", command=self.load_file).pack(side="left")
        tk.Button(btn_frame, text="Analyze", command=self.analyze).pack(side="left")
        tk.Button(btn_frame, text="Show Risks", command=self.show_risks).pack(side="left")
        tk.Button(btn_frame, text="Chart", command=self.show_chart).pack(side="left")
        tk.Button(btn_frame, text="Send Reports", command=self.send_reports).pack(side="left")

        # -------- OUTPUT BOX --------
        self.output = tk.Text(root, height=8)
        self.output.pack(fill="x")

        # -------- CHART FRAME --------
        self.chart_frame = tk.Frame(root, bg="white")
        self.chart_frame.pack(fill="both", expand=True)
    def load_file(self):
        file = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if file:
            self.data = pd.read_csv(file)

            # clean column names (IMPORTANT FIX)
            self.data.columns = self.data.columns.str.strip()

            messagebox.showinfo("Success", "File Loaded")

    def analyze(self):
        if self.data is None:
            return

        self.data = calculate_score(self.data)

        avg = np.mean(self.data['Score'])
        top = self.data.loc[self.data['Score'].idxmax()]['Name']

        self.output.insert(tk.END, f"Avg: {avg:.2f}, Top: {top}\n")

    def show_risks(self):
        print(self.data)
        self.data['Score']
        risks = detect_risk(self.data)

        self.output.insert(tk.END, "\nRisks:\n")
        for name, r in risks:
            self.output.insert(tk.END, f"{name}: {', '.join(r)}\n")

    def show_chart(self):

        if self.data is None:
            messagebox.showerror("Error", "Load CSV first")
            return

        if 'Score' not in self.data.columns:
            messagebox.showerror("Error", "Click Analyze first")
            return

        if 'Name' not in self.data.columns:
            messagebox.showerror("Error", "'Name' column missing")
            return

        # clear old chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))

        ax.bar(self.data['Name'], self.data['Score'], color='green')
        ax.set_title("Employee Performance")
        ax.set_ylabel("Score")

        plt.xticks(rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def send_reports(self):

        if self.data is None:
            messagebox.showerror("Error", "No data loaded")
            return

        for _, row in self.data.iterrows():
            try:
                pdf_file = f"{row['Name']}_report.pdf"

                print("Generating:", pdf_file)

                # Step 1: Generate PDF
                generate_pdf(row, pdf_file)

                # Step 2: Send email
                send_email(
                    row['email'],  # make sure column name is correct
                    "Performance Report",
                    f"Hi {row['Name']}, your report is ready.",
                    pdf_file
                )

            except Exception as e:
                print("Error:", e)

        messagebox.showinfo("Success", "Reports Sent!")