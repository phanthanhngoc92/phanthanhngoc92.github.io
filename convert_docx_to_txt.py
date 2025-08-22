import pypandoc

# Example file:
docxFilename = 'CV_Megan_0525.docx'
output = pypandoc.convert_file(docxFilename, 'md', outputfile="CV_Megan_0525.md")
assert output == ""