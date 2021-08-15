## 468. Validate IP Address

### Description
Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4  
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').  
Leading zeros are allowed in xi.  
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and  "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:  
Input: IP = "172.16.254.1"  
Output: "IPv4"  
Explanation: This is a valid IPv4 address, return "IPv4".  

Example 2:  
Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"  
Output: "IPv6"  
Explanation: This is a valid IPv6 address, return "IPv6".  

### Solution
* Time Complexity: O(n)

```python
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validIPv4(IP)
        if IP.count(':') == 7:
            return self.validIPv6(IP)
        return 'Neither'
        
    def validIPv4(self, ip):
        sections = ip.split('.')
 
        for section in sections:
            if not section or len(section) > 3:
                return 'Neither'
            if section[0] == '0' and len(section) != 1:
                return 'Neither'
            if not section.isdigit():
                return 'Neither'
            if not (0 <= int(section) <= 255):
                return 'Neither'
        return 'IPv4'
        
    def validIPv6(self, ip):
        charSet = set([str(x) for x in range(10)]+list('abcdefABCDEF'))
        sections = ip.split(':')
        if len(sections) != 8:
            return 'Neither'
        for section in sections:
            if not section or len(section)>4:
                return 'Neither'
            for c in section:
                if c not in charSet:
                    return 'Neither'
        return 'IPv6'
```
