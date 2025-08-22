import docx

def extract_cv_content():
    try:
        doc = docx.Document('CV_Megan_0525.docx')
        content = []
        
        for i, paragraph in enumerate(doc.paragraphs):
            if paragraph.text.strip():
                content.append(f"Paragraph {i}: {paragraph.text}")
        
        return '\n'.join(content)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(extract_cv_content())
