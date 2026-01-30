from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo or decorative line
        self.set_line_width(1)
        self.line(10, 10, 200, 10)
        self.ln(10)
        
        # Title
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Project Submission', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def create_submission_pdf():
    pdf = PDF()
    pdf.add_page()
    
    # Project Info
    pdf.set_font("Arial", size=12)
    
    # Content Data
    info = {
        "Project Title": "Data Engineering Road-map: End-to-End E-Commerce Pipeline",
        "Student Name": "Ali Cihan Ozdemir",
        "Student ID": "9091405",
        "Course": "PROG8245 - Data Collection & Pre-Processing",
        "Date": "2026-01-30"
    }

    # Draw Info Box
    pdf.set_fill_color(240, 240, 240)
    pdf.rect(10, 35, 190, 60, 'F')
    pdf.set_y(40)

    for key, value in info.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(50, 10, key + ":", 0, 0)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, value, 0, 1)

    pdf.ln(20)

    # GitHub Link Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "GitHub Repository", 0, 1)
    pdf.set_font("Arial", '', 12)
    
    repo_link = "https://github.com/alicih4n/DataCollectionPreProcessing.git"
    pdf.set_text_color(0, 0, 255)
    pdf.cell(0, 10, repo_link, 0, 1, link=repo_link)
    pdf.set_text_color(0, 0, 0)
    
    pdf.ln(10)

    # Project Source Section
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Project Details", 0, 1)
    
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, 
        "This submission contains a Jupyter Notebook implementing a 15-step Data Engineering workflow. "
        "It includes data loading, cleaning, transformation, and serialization (JSON) of e-commerce sales data.\n\n"
        "Files included in the repository:\n"
        "- notebooks/data_engineering_lab.ipynb\n"
        "- data/sales_data.csv\n"
        "- data/product_metadata.csv\n"
        "- requirements.txt\n"
        "- README.md\n"
    )

    # Save
    output_filename = "Submission_AliCihanOzdemir_9091405.pdf"
    pdf.output(output_filename)
    print(f"PDF generated: {output_filename}")

if __name__ == "__main__":
    create_submission_pdf()
