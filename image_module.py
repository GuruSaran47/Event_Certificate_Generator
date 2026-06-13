from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import csv

class read_csv:
    __read_data__ = []
    def __init__(self,file_path):
        self.__file_path__ = file_path
        self.__read_csv__()

    def debug(self):
        print("path",self.__file_path__)
        print(self.__read_data__)
        
    def __read_csv__(self):
        with open(self.__file_path__,"r") as openfile:
            data = csv.reader(openfile,delimiter=',',quotechar='|')
            for line in data:
                self.__read_data__.append(line)
    
    def get_data(self):
        return self.__read_data__
    

class write_text:
    __p_designation = (600,490)
    __p_name = (690,490) 
    __p_institute = (230,550)
    __p_event = (500,610)
    
    # Add your new fields here, FOR EXAMPLE follow the below (Uncomment the new line below while execution)
    #__p_add1 = (50,50)
    
    def __init__(self,image_path,data):
        self.__image_path__ = image_path
        self.__template__ = Image.open(self.__image_path__)
        self.__font__type__ = ImageFont.truetype(r'.\Calibri.ttf',45)
        self.__data__= data
        self.__run_generator__()
    
    def debug(self):
        print(self.__image_path__)
        print(self.__data__)
        print(self.__p_designation)
        print(self.__p_name)
        print(self.__p_institute)
        print(self.__p_event)
        #In case you need a new debug line use it here
        # print(self.__p_add1)

    def __run_generator__(self):
        # skip the first line
        for index in range (len(self.__data__)):
            if(index < -1):
                continue
            else:
                print_desig = self.__data__[index][0]
                print_name = self.__data__[index][1]
                print_institute = self.__data__[index][2]
                print_event = self.__data__[index][3]
                #for the new addition of data you need to add the new index here.(Uncomment the new line below while execution)
                #print_add1 = self.__data__[index][4] #fourth index means the 4th column to the right inside the csv

                template = Image.open(self.__image_path__)
                font = self.__font__type__
                image = ImageDraw.Draw(template)
                print_name.replace(' ','_')
                image.text(self.__p_designation,print_desig,font=font,fill=(0,0,0))
                image.text(self.__p_name,print_name,font=font,fill=(0,0,0))
                image.text(self.__p_institute,print_institute,font=font,fill=(0,0,0))
                image.text(self.__p_event,print_event,font=font,fill=(0,0,0))
                #add a line here to print it onto the image (Uncomment the new line below while execution)
                #image.text(self.__p_add1,print_add1,font=font,fill=(0,0,0))
                template.save(f'.\Destination\{print_name}.jpeg')
                template.close()




