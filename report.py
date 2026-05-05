from reportlab.pdfgen import canvas

def generate_pdf(row, filename):
    c = canvas.Canvas(filename)

    c.drawString(50, 750, "Employee Report")
    c.drawString(50, 700, f"Name: {row['Name']}")
    c.drawString(50, 680, f"Score: {row['Score']:.2f}")

    c.save()