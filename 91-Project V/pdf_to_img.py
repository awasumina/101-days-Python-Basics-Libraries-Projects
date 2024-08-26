# # pip install pdf2image
# # install poppler
# # with the help of poppler we caan read, write and edit the pdfs directly

# from pdf2image import convert_from_path

# # r represents the reference path
# old_pdf = convert_from_path("pdf1.pdf", poppler_path = "D:/vs code/my_folder/python/py_projects/Awesome_Project/working_with_pdfs/poppler-23.08.0/Library/bin")

# for i in range(len(old_pdf)) :
    
#     old_pdf[i].save("new" + str(i) + ".jpg","JPEG")
#     # old_pdf[i].save("new" + str(i) + ".png","PNG")

# Install the necessary libraries using pip
# pip install pdf2image

# Import the required module
from pdf2image import convert_from_path

# Set the path to the Poppler executable
poppler_path = "D:/vs code/my_folder/python/py_projects/Awesome_Project/working_with_pdfs/poppler-23.08.0/Library/bin"

# Specify the input PDF file
pdf_file = "pdf1.pdf"

# Convert the PDF to images
try:
    images = convert_from_path(pdf_file, poppler_path=poppler_path)

    for i, image in enumerate(images):
        image.save(f"new_{i}.jpg", "JPEG")
except Exception as e:
    print(f"An error occurred: {e}")

# Note:
# 1. The code sets the Poppler path in a separate variable, which can make it easier to manage.
# 2. It catches any exceptions that might occur during the conversion process and prints an error message if needed.
# 3. Make sure to replace "pdf1.pdf" with the actual path to your input PDF file.

