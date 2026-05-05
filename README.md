# Employee-Performance-Dashboard
This is a desktop-based dashboard built using Python that analyzes employee performance data from a CSV file. It calculates performance scores, detects risks, visualizes data using charts, generates PDF reports, and automatically sends them via email.
🎯 Features
-> 📂 Upload CSV file
-> 📊 Analyze employee performance
-> ⚠️ Detect risky employees
-> 📈 Visualize data using bar charts
-> 📄 Generate PDF reports
-> 📧 Send reports via email (with attachments)

🛠️ Tech Stack
-> Python
-> Tkinter – GUI development
-> Pandas & NumPy – Data processing
-> Matplotlib – Data visualization
-> ReportLab – PDF generation
-> smtplib – Email automation

📂 Project Structure
project-folder/
│
├── main.py            # Entry point
├── ui.py              # GUI logic
├── dataprocessor.py   # Score calculation & risk detection
├── report.py          # PDF generation
├── emailservice.py    # Email sending
├── sample.csv         # Sample dataset
└── README.md

📌 How It Works
-> User uploads a CSV file containing employee data
-> System calculates performance scores using weighted metrics
-> Risk detection identifies low-performing employees
-> Data is visualized using a bar chart
-> Individual PDF reports are generated
-> Reports are sent via email automatically

⚙️ Installation & Setup
  1. Clone the repository
  2. Install dependencies
    pip install pandas numpy matplotlib reportlab
  3. Run the application
     main.py
    📄 CSV Format Example
        Your CSV file should contain columns like:
        Name, email, TotalTickets, P1_Critical, Incidents_Handled, KT_Sessions, Appreciations, Ticket_Breaches, Escalations
  ⚠️ Important Notes
    Make sure column names are correct


Author
--------
Arpita Das Rakshit
Email sending requires a Gmail App Password
Do not expose your credentials in code
