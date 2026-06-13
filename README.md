# Event_Certificate_Generator
This is the software is for printing the data collected on the gforms or any forms application on a certificate template.
##########################################################################################
Intended Audience: College clubs or Instructors who are looking for generating many certs
of your event at a time.
===========================================================================================
Purpose of the Tool: One execution to generate certificates, based on the input template.
===========================================================================================
------------------------------------------------------------------------------------------
How to use?
------------------------------------------------------------------------------------------
In the current version, we support addition of Basic Details to the certificate like:
1. "Title"
2. "Name"
3. "College"
4. "Event"

[Note]: The above mentioned fields remain the same in case 
------------------------------------------------------------------------------------------
How to give the input?
------------------------------------------------------------------------------------------
1. The application accepts the input in-terms of the .csv file.
2. From which ever google form you collect the person data, Pls organize it into a CSV as 
given in the present directory ".\source\names.csv"
3. Give the Template folder in the present directory itself. [Note]: Follow the current 
example in the directory ".\template.jpeg"
4. Run the image.py file or run the image.exe

[Note]: For specific adjustment in the text follow NEXT SECTION.

------------------------------------------------------------------------------------------
How to customise the output?
------------------------------------------------------------------------------------------
Customizations here literally means that you need to cut into the source code and do 
the changes you are quite looking for.
__________________________________________________________________________________________

1. Changes in the position of the "Basic Details"

S0: Go to file: ".\image_module.py"
S1: Go to the class "write_text" (You can search this upon opening the editor)
	S1.1: Here please edit the fields __p_xxx = (x_coordinate,y_coordinate)
image.text(self.__p_add1,print_add1,font=font,fill=(0,0,0))

2. Add new columns or new data field inside the software output

S0: Go to file: ".\image_module.py"
S1: Go to the class "write_text" (You can search this upon opening the editor)
	S1.1: Add your class private member parameter "self.__p_xxx"
	S1.2: Go to the class function "__run_generator__"
	S1.3: Add your present variable "print_xxx" to hold the new field extracted from 
	      the csv file. e.g: print_xxx = self.__data[index][n] #where n is the nth index
              you are referring to.
	S1.4: Add the last line image.text(self.__p_xxx,print_add1,font=font,fill=(0,0,0))

[Note]: For the Steps S1.3 and S1.4 follow the comments in the code.
__________________________________________________________________________________________
------------------------------------------------------------------------------------------
==========================================================================================
Message from Developer:

I regret that I couldn't develop proper UI, due to constraint of time which we had. I hope 
to make it one day.

If you have anything to contribute, pls feel free.

e-mail: gurusaranreddy206@gmail.com
