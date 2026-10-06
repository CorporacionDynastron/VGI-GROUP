import sys
try:
    import PyPDF2
    with open(r"C:\Dynastron_Code\VGI\BROCHURE VGI A3 - MEJORADO.pdf", "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for i in range(min(5, len(reader.pages))):
            print(f"--- Page {i+1} ---")
            print(reader.pages[i].extract_text())
except Exception as e:
    print("Error:", e)
