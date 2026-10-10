from pypdf import PdfReader

reader = PdfReader("GEE-1104-CAT1-Preparation-Guide-v2.pdf")

print(f"Total pages: {len(reader.pages)}")

first_page = reader.pages[1]
print(first_page.extract_text())
