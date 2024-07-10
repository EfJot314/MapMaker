# Map Maker
## Description
This application is intended to create maps for text-based games such as SUD or MUD.
## Requirements
The application has the following list of requirements:
1. Python 3
2. ```Pip``` tool
3. ```Tkinter``` library
4. ```Pygame``` library
## How to run
Before first usage it is required to install application requirements mentioned above. Having Python with Pip tool, you can install required libraries running following command in project directory:
```
pip3 install -r requirements.txt
```
After succesful installation, you can run application:
```
python main.py
```
## How to use Map Maker
### Creating new map nodes
To create new node, you have to press ```n``` key. New node will be created at the mouse position. 
### Moving map nodes
To move node, you have to click chosen node using left mouse button and then drag it to its new position.
### Changing name of map node
After creation, nodes have default name (```Unnamed```), if you would like to change it, you have to click chosen node using right mouse button, type new name and press ```enter``` key.
### Creating new conections between map nodes
To create new connection, you have to press ```m``` key. Then you have to click chosen nodes using left mouse button. 
### Removing map nodes
To remove node, you have to press ```x``` key with mouse over chosen map node.
### Moving map (map nodes and connections)
To move map, you can use ```w```, ```s```, ```a``` and ```d``` keys.
### Saving map
If you would like to save created map, then you have to press ```v``` key and choose destination using file dialog window. The file extension can be any.
### Loading map
If you would like to load saved map to the application, then you have to press ```c``` key and choose saved map using file dialog window. Note, that any unsaved changes in currently using map will be lost.
###  Application appearance
The application provides two appearance modes:
1. ```Bright mode``` - white background (press ```1``` key)
2. ```Dark mode``` - black background (press ```2``` key)