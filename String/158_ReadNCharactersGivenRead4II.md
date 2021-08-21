## 158. Read N Characters Given read4 II

### Description

Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4  
    Returns:    int  

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

Example 1:  
Input: file = "abc", queries = [1,2,1]  
Output: [1,2,0]  
Explanation: The test case represents the following scenario:  
File file("abc");  
Solution sol;  
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.  
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.  
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.  
Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.  

### Solution

```python
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque()

    def read(self, buf: List[str], n: int) -> int:
        """
        Input: file = "abc", queries = [1,2,1]
        Output: [1,2,0]
        """
    
        buf4 = [''] * 4
        idx = 0
        while idx < n:
            if self.q:
                buf[idx] = self.q.popleft()
                idx += 1
            else:
                nread = read4(buf4)
                if nread == 0:
                    break
                for i in range(nread):
                    self.q.append(buf4[i])
        return idx
```
## 158. Read N Characters Given read4 II

### Description

Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Method read:

By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.

The return value is the number of actual characters read.

Example 1:  
Input: file = "abc", queries = [1,2,1]  
Output: [1,2,0]  
Explanation: The test case represents the following scenario:  
File file("abc");  
Solution sol;  
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.  
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.  
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.  
Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.  

### Solution

```python
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque()

    def read(self, buf: List[str], n: int) -> int:
        """
        Input: file = "abc", queries = [1,2,1]
        Output: [1,2,0]
        """
    
        buf4 = [''] * 4
        idx = 0
        while idx < n:
            if self.q:
                buf[idx] = self.q.popleft()
                idx += 1
            else:
                nread = read4(buf4)
                if nread == 0:
                    break
                for i in range(nread):
                    self.q.append(buf4[i])
        return idx
```
