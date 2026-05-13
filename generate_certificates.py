# ============================================
# Certificate Generator Project
# ============================================

# Import Libraries
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import reportlab.rl_config

import pandas as pd
import io
import os

# ============================================
# Create Certificates Folder
# ============================================

os.makedirs("Certificates", exist_ok=True)

# ============================================
# Check Required Files
# ============================================

if not os.path.exists("participants.xlsx"):
    print("❌ participants.xlsx file not found!")
    exit()

if not os.path.exists("Input/certificate_template1.pdf"):
    print("❌ certificate_template1.pdf not found!")
    exit()

# ============================================
# Read Excel File
# ============================================

try:
    participants = pd.read_excel("participants.xlsx")
except Exception as e:
    print("❌ Error reading Excel file:")
    print(e)
    exit()

# ============================================
# Register Fonts (Only Once)
# ============================================

reportlab.rl_config.warnOnMissingFontGlyphs = 0

pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

# ============================================
# Generate Certificates
# ============================================

for _, row in participants.iterrows():

    try:
        # ====================================
        # Get Data from Excel
        # ====================================

        student = str(row["Student"])
        course = str(row["Course"])

        # Format Date Properly
        date = pd.to_datetime(row["Date"]).strftime("%d-%m-%Y")

        print(f"📄 Generating certificate for: {student}")

        # ====================================
        # Create Temporary PDF
        # ====================================

        packet = io.BytesIO()

        width, height = letter

        c = canvas.Canvas(packet, pagesize=(width * 2, height * 2))

        # ====================================
        # Write Student Name
        # ====================================

        c.setFillColorRGB(139/255, 119/255, 40/255)
        c.setFont("VeraBd", 50)

        c.drawCentredString(422, 310, student)

        # ====================================
        # Write Course Name
        # ====================================

        c.setFillColorRGB(139/255, 119/255, 40/255)
        c.setFont("Vera", 25)

        c.drawCentredString(422, 210, course)

        # ====================================
        # Write Date
        # ====================================

        c.setFillColorRGB(0, 0, 0)
        c.setFont("VeraBI", 16)

        c.drawCentredString(578, 77, date)

        # Save Canvas
        c.save()

        # ====================================
        # Move to Beginning of Buffer
        # ====================================

        packet.seek(0)

        # ====================================
        # Read Overlay PDF
        # ====================================

        new_pdf = PdfReader(packet)

        # ====================================
        # Read Certificate Template
        # ====================================

        with open("Input/certificate_template1.pdf", "rb") as template_file:

            existing_pdf = PdfReader(template_file)

            page = existing_pdf.pages[0]

            # =================================
            # Merge Text with Template
            # =================================

            page.merge_page(new_pdf.pages[0])

            # =================================
            # Create Output PDF
            # =================================

            output = PdfWriter()
            output.add_page(page)

            # =================================
            # Output File Name
            # =================================

            safe_name = student.replace(" ", "_")

            output_file = os.path.join(
                "Certificates",
                f"{safe_name}_certificate.pdf"
            )

            # =================================
            # Save Final PDF
            # =================================

            with open(output_file, "wb") as outputStream:
                output.write(outputStream)

        print(f"✅ Certificate saved: {output_file}")

    except Exception as e:
        print(f"❌ Error generating certificate for {student}")
        print(e)

# ============================================
# Completed
# ============================================

print("\n🎉 All Certificates Generated Successfully!")