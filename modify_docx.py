from docx import Document

doc = Document("CareerBridge_SRS_Report.docx")

# Print all paragraphs to find "Submitted By" and "yash kisan Patil"
for i, para in enumerate(doc.paragraphs):
    if "Submitted" in para.text or "yash" in para.text.lower() or "patil" in para.text.lower():
        print(f"Para {i}: {para.text}")

# Also check tables
for i, table in enumerate(doc.tables):
    for row_idx, row in enumerate(table.rows):
        for cell_idx, cell in enumerate(row.cells):
            if "Submitted" in cell.text or "yash" in cell.text.lower() or "patil" in cell.text.lower():
                print(f"Table {i}, Row {row_idx}, Cell {cell_idx}: {cell.text}")