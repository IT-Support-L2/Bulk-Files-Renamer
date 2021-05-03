# Bulk-Files-Renamer

Bulk Files Renamer allows you to rename thousands files selected by its extension in few seconds only! Thanks to Python threading technique.


- tkinter GUI designed with PAGE but I modified most part of the generated code.

- Developed with Python 3.9.0 and tkinter. 


 • What should I input in Path?
 
   You should input the folder directory, where your files are located.
   
   Example:  ```C:/Users/user/Desktop/Folder/```
   
   Hint: In windows, you should replace all Backslash with Forward Slash
   and add another Forward Slash after the folder name like the following.
   
   Wrong path input:       ```C:\Users\user\Desktop\folder```
   
   Correct path input:     ```C:/Users/user/Desktop/folder/```
        
 • What should I input in extension?
 
   You should input the extension of the files your are willing to rename.
   Input example: 
   
   ```txt```
   ```pdf``` 
   ```doc```
   ```exe``` 
   
   ect..
        
 • What should I input in New Files names?
 
   You should input the name which will be used for all files with the same extension. Don't worry, each file with the new name will be incremented by one to maintain
   minimum distinction.
   
   Exemple: Let's suppose you have multiple xlsx files which are related to a single project of a Hotel financial report, simply input Hotel or the hotel's name.
   
   So if you have for exemple 100 xlsx file, new files names will be Hotel1 Hotel2 Hotel3 and so on.

To successfully compile the code into Windows executable, while you are in the BulkFileRenamer.py directory run:

```
pyinstaller --noconsole BulkFileRenamer.py
```

![BulkFilesRenamer.gif](https://github.com/IT-Support-L2/Bulk-Files-Renamer/blob/main/BulkFilesRenamer.gif)

