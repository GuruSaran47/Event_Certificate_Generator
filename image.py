from image_module import *
template = Image.open(r'.\template.jpeg')
font = ImageFont.truetype(r'.\Calibri.ttf',45)
obj1 = read_csv(r'.\Source\names.csv') 
obj2 = write_text(r'.\template.jpeg',obj1.get_data())
