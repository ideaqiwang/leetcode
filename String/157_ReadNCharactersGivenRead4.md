## 157. Read N Characters Given Read4

### Description

Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

#### Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

#### Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

Example 1:  
Input: file = "abc", n = 4  
Output: 3  
Explanation: After calling your read method, buf should contain "abc". We read a total of 3   characters from the file, so return 3.  
Note that "abc" is the file's content, not buf. buf is the destination buffer that you will   have to write the results to.  

Example 2:  
Input: file = "abcde", n = 5  
Output: 5  
Explanation: After calling your read method, buf should contain "abcde". We read a total of 5   characters from the file, so return 5.  

### Solution

```python
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [''] * 4
        idx = 0
        while True:
            nread = read4(buf4)
            if nread == 0:
                return idx
            for i in range(nread):
                buf[idx] = buf4[i]
                idx += 1
                if idx == n:
                    return idx
```
