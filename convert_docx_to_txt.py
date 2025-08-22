import pypandoc

# Example file:
docxFilename = 'CV_Megan_0525.docx'
output = pypandoc.convert_file(docxFilename, 'plain', outputfile="CV_Megan_0525.txt")
assert output == ""