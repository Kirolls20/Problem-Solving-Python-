class Solution:
    """
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
    """
    def defagIpaddr(self,address:str) -> str:
        defanged_version = address.replace('.','[.]')
        return defanged_version


obj = Solution()
print(obj.defagIpaddr("255.100.50.0")) # "255[.]100[.]50[.]0" 
# https://leetcode.com/problems/defanging-an-ip-address/description/
