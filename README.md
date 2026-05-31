# Certificate Generator

A Python-based automated certificate generation system that creates personalized PDF certificates for participants based on data from an Excel spreadsheet.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Input Requirements](#input-requirements)
- [Output](#output)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This project automates the generation of professional PDF certificates by merging participant data with a customizable PDF template. It reads participant information from an Excel file and generates personalized certificates with custom fonts, colors, and positioning.

## ✨ Features

- **Batch Certificate Generation**: Process multiple participants at once
- **Customizable Templates**: Use any PDF template as the base certificate
- **Excel Integration**: Read participant data from `.xlsx` files
- **Custom Fonts Support**: Support for TrueType fonts (TTF)
- **Professional Formatting**: Adjustable text color, size, and positioning
- **Automated Output Organization**: All certificates saved to a dedicated folder
- **Error Handling**: Comprehensive validation and error messages

## 📦 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone or download the project** to your local machine

2. **Install required dependencies**:

   ```bash
   pip install PyPDF2 reportlab pandas openpyxl
   ```

   Or use the requirements file (if available):

   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

```
certificate-generator/
├── generate_certificates.py      # Main script
├── participants.xlsx             # Input: Participant data (template provided below)
├── Input/
│   └── certificate_template1.pdf # Certificate PDF template
├── Certificates/                 # Output folder for generated certificates
├── VeraBd.ttf                   # Font files 
├── Vera.ttf                      # Font files (Regular)
├── VeraBI.ttf                    # Font files (Bold Italic
└── README.md                     # This fil
```

## 💻 Usage

### Step 1: Prepare Your Data

Create an Excel file named `participants.xlsx` with the following columns:

| Student    | Course          | Date       |
| ---------- | --------------- | ---------- |
|   Veda     | Python Basics   | 2026-05-13 |
|  Ram    | Web Development | 2026-05-12 |

### Step 2: Prepare Your Certificate Template

Place your PDF certificate template in the `Input/` folder with the name `certificate_template1.pdf`.

### Step 3: Set Up Font Files

Ensure the required font files are in the project root:

- `VeraBd.ttf` (Bold)
- `Vera.ttf` (Regular)
- `VeraBI.ttf` (Bold Italic)

### Step 4: Run the Script

Execute the certificate generator:

```bash
python generate_certificates.py
```

### Step 5: Retrieve Generated Certificates

All generated certificates will be saved in the `Certificates/` folder with filenames based on participant names.

## 📥 Input Requirements

### participants.xlsx

- **Student**: Full name of the participant
- **Course**: Name of the course/certification
- **Date**: Date of completion (any standard date format)

### Certificate Template

- PDF file located at `Input/certificate_template1.pdf`
- Should have a blank area where participant information will be added

## 📤 Output

- **Location**: `Certificates/` folder
- **Format**: PDF files
- **Naming Convention**: `{Student_Name}.pdf`
- **Quality**: High-resolution, suitable for printing

## ⚙️ Configuration

You can customize the certificate appearance by modifying these parameters in `generate_certificates.py`:

```python
# Text Color (RGB format - values 0-255)
c.setFillColorRGB(139/255, 119/255, 40/255)  # Gold color

# Font Selection
c.setFont("VeraBd", 50)  # Font name and size

# Text Position
c.drawCentredString(422, 310, student)  # X, Y coordinates
```

## 🐛 Troubleshooting

### Error: "participants.xlsx file not found!"

- Ensure `participants.xlsx` exists in the project root directory
- Check the filename spelling and extension

### Error: "certificate_template1.pdf not found!"

- Verify the PDF template is in the `Input/` folder
- Check the filename matches exactly

### Error: "Error reading Excel file"

- Ensure the Excel file has the required columns: Student, Course, Date
- Check that the file is not corrupted or password-protected

### Fonts not displaying correctly

- Verify font files (TTF) are in the project root
- Check font names match registered font names in the script
- Ensure fonts support the characters being used

### PDF looks incorrect

- Verify certificate template dimensions
- Adjust text coordinates (X, Y values) in the script
- Check text color and font size settings

## 📝 Notes

- The script creates the `Certificates/` folder automatically if it doesn't exist
- All errors are logged to the console with emoji indicators for easy identification
- Processing time depends on the number of participants and template complexity

## 📄 License

This project is provided as-is for personal and educational use.

## 🤝 Support

For issues or questions, review the troubleshooting section or check the console output for error messages.

---

**Last Updated**: May 2026
