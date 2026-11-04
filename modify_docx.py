from docx import Document

doc = Document("CareerBridge_SRS_Report.docx")

# Change paragraph 13: "Yash Kisan Patil" -> "Gourav Dash"
doc.paragraphs[13].text = "Gourav Dash"

# Change table 0, row 1, cell 0: "Yash Kisan Patil" -> "Gourav Dash"
doc.tables[0].rows[1].cells[0].text = "Gourav Dash"

# Add registration number after the name in the table
# Let's check the table structure first
table = doc.tables[0]
print("Table rows:")
for i, row in enumerate(table.rows):
    for j, cell in enumerate(row.cells):
        print(f"  Row {i}, Cell {j}: '{cell.text}'")

# Save the modified document
doc.save("CareerBridge_SRS_Report_modified.docx")
print("Document saved as CareerBridge_SRS_Report_modified.docx")