import datetime
class FSEntry:
    # parentDir = None
    # fileCreated = self.fileLastRetrieved = self.fileLastModified = datetime.datetime
    # fileName = ''
    # size = 0
    def __init__(self, fileName, parentDir):
        self.fileName = fileName
        self.parentDir = parentDir
        self.fileCreated = self.fileLastModified = self.fileLastRetrieved = datetime.datetime.now()
        self.size = 0
        if not parentDir is None:
            parentDir.addEntry(self)
    
    def __repr__(self):
        return str([self.fileName, self.parentDir, self.fileCreated.ctime(), self.fileLastModified.ctime()])

    def entryModified(self):
        self.fileLastModified = datetime.datetime.now()

    def entryRead(self):
        self.fileLastRetrieved = datetime.datetime.now()

class File(FSEntry):
    # fileContent = None
    # size = 0
    def __init__(self, fileName, parentDir):
        super().__init__(fileName, parentDir)
        self.fileContent = None
        self.fileType = 'NoneType'
        self.size = 0

    def __repr__(self):
        return str([self.fileName, self.getPath()])
    
    def setContents(self, content):
        self.fileContent = content
        try:
            self.size = len(content)
        except:
            self.size = -1
            # len didn't work, maybe int or boolean
        self.fileType = type(content)
        self.entryModified()
    
    def getPath(self):
        if self.parentDir == None:
            return self.fileName + "\nThis file is not saved anywhere."
        else:
            return self.parentDir.getPath() + self.fileName
    
    def readContents(self):
        self.entryRead()
        return self.fileContent

    def isDir(self):
        return False
    
class Directory(FSEntry):
    def __init__(self, fileName=str(datetime.datetime.now()), parentDir=None):
        super().__init__(fileName, parentDir)
        self.contents = []
        self.size = 0
    
    def __repr__(self):
        return str([self.fileName, self.getPath()])

    def updateSize(self):
        size = 0
        for content in self.contents:
            try:
                size += content.updateSize()
            except:
                size += content.size
        self.size = size

    def getPath(self):
        if self.parentDir == None:
            return '/'
        else:
            return self.parentDir.getPath() + self.fileName + '/'
    def noOfFiles(self):
        return len(self.contents)
    
    def deleteEntry(self, contentFile):
        if self.contents.remove(contentFile):
            self.updateSize()
            return True
        return False
    
    def addEntry(self, contentFile):
        self.contents.append(contentFile)
        self.updateSize()
        return True
    
    def getContents(self):
        contents = []
        for content in self.contents:
            contents.append(content.fileName)
        return contents
    
    def isDir(self):
        return True
