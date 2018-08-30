import insert_picture_into_cells
from docx import Document

doc = Document()

insert_picture_into_cells.insert_picture(document=doc,rows=1,cols=1,picture_path="IMG_TEST.png",picture_width=3,picture_height=3)

doc.save('demo.docx')