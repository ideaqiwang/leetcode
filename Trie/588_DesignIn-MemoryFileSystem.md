## 588. Design In-Memory File System
### Description
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.

**List<String> ls(String path)**  
If path is a file path, returns a list that only contains this file's name.  
If path is a directory path, returns the list of file and directory names in this directory.  
The answer should in lexicographic order.  

**void mkdir(String path)** Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.  

**void addContentToFile(String filePath, String content)**  
If filePath does not exist, creates that file containing given content.  
If filePath already exists, appends the given content to original content.  
String readContentFromFile(String filePath) Returns the content in the file at filePath.  

Example 1:
Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation  
FileSystem fileSystem = new FileSystem();  
fileSystem.ls("/");                         // return []  
fileSystem.mkdir("/a/b/c");  
fileSystem.addContentToFile("/a/b/c/d", "hello");  
fileSystem.ls("/");                         // return ["a"]  
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"  

### Solution
* Use Trie

```python
class Node:
    def __init__(self):
        self.children = {}
        self.isFile = False
        self.content = ''
  
class FileSystem:
    def __init__(self):
        self.root = Node()
    
    def add(self, path):
        node = self.root
        for part in path.split('/')[1:]:
            if part not in node.children:
                node.children[part] = Node()
            node = node.children[part]
        return node

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted([*self.root.children.keys()])

        node = self.add(path)
        if node.isFile:
            return [path.split('/')[-1]]
        return sorted([*node.children.keys()])

    def mkdir(self, path: str) -> None:
        self.add(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.add(filePath)
        node.content += content
        node.isFile = True

    def readContentFromFile(self, filePath: str) -> str:
        node = self.add(filePath)
        return node.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
```
