import PyPDF2

merger = PyPDF2.PdfMerger()
file_list = []

no_of_files = int(input("Enter the number of files to be merged: "))
for i in range(no_of_files):
    file_name = input("Enter the file name along with extension: ")
    file_list.append(file_name)

for file in file_list:
    pdf_file = open(file, 'rb')
    merger.append(pdf_file)

output_filename = input("Enter the output merged file name along with extension: ")
merger.write(output_filename)

# Close all the input PDF files and the merged file
for pdf_file in merger.inputs:
    pdf_file.close()

print(f"Merged PDF saved as {output_filename}")
