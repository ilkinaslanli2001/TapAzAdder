# WebScrappingPython

This program  automatically add products which are located in photos folder to Azerbaijan website(www.tap.az) in Chrome Browser.
Cost of the products program takes from the name of the picture.


## How to use
### First of all you should install specific requirements.
### To do it enter "pip install -r requirements.txt" at the root of the project

After running the program,  you should input an information about the order and seller
The you should enter an interval (after how many seconds will each order be added).Set the interval based on your internet speed so that the picture has time to upload to the website
Finnaly click 'Start' and wait.


## How it works 
Libraries: PyQt5 (for Gui) , Selenium (for web-scrapping)
After clicking the 'Start' button, the program opens a cycle which is equal to the number of photos in selected folder.
Every order has the same name and description which was written before (customer desire)


## For creating .exe file of this program you should enter ``` python setup.py build ```
In ``` build.py ```  I collected all gui of program and code.
In ``` setup.py ```  You can see main settings for creating exe file
