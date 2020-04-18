# gehujeleTOT

gehujeleTOT is a module for ITeung to automation e-Haki and Aptimas.

## MODULE

to moving files from downloads to development directory example:
```python
def moveFiles(filename):
    move = True
    while move:
        try:
            source = 'downloads path' + str(namafile)
            destination = r'development path'
            shutil.move(source, destination)
            move = False
        except Exception as e:
            if 'already exists' in str(e):
                move = False
            else:
                move = True
```

incremental for creating directory if the directory is exist and still used, for the future the folder will be deleted if the process is complete:
```python
def makeDirectory():
    mkdir = True
    create = '1'
    while mkdir:
        try:
            os.mkdir(str(create))
            mkdir = False
        except:
            create = int(create) + 1
            mkdir = True
    return create
```
make directory function return the folder that succesfully created and will be used for extraction.

extracting file must be compressed file like .zip or .rar (has not been tried for the .tar.gz, etc format):
```python
def extractFiles(filename):
    try:
        create=self.makeDirectory()
        Archive(filename).extractall('.\\' + str(create))
        result = []
        for root, dirs, files in os.walk(r'.\{folder}'.format(folder=create)):
            for i in files:
                if 'file to search' in i:
                    result.append(os.path.join(root, i))
    except:
        result=''
        self.typeAndSendMessage('file must be .zip or .rar')
        os.remove(namafile)
        os.rmdir(create)
    return result
```
after the extracting, the system will trying to find the file in the folder that was created on makeDirectory() with the file want to search, example: *file.pdf*. on the 'file to search' you can replace with 'file.pdf' and if founded it will return the path to the *file.pdf*.

License
----
MIT

**NOTE**
This development adapted (or using) wanda 