def longest_common_prefix(strs):
    """
    Finds the longest common prefix in a list of strings.

    Args:
        strs: the list of strings

    Returns:
        the longest common prefix, or an empty string if none exists
    """
    if strs==[]:
        return ""
    elif len(strs)==1:
        return strs[0]
    prefix=strs[0]
    for i in range(len(strs)-1):
        j=0
        temp=''
        while j<len(strs[i]) and j<len(strs[i+1])  and strs[i][j]==strs[i+1][j]:
            temp+=strs[i][j]
            j+=1
        if len(temp)<len(prefix):
            prefix=temp
    return prefix
            


if __name__ == '__main__':
    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["interspecies", "interstellar", "interstate"]
    test4 = ["apple", "apricot", "ape"]
    test5=[]
    test6=["Tameer"]
    print(f"Longest Common Prefix: {longest_common_prefix(test1)}")  # Output: "fl"
    print(f"Longest Common Prefix: {longest_common_prefix(test2)}")  # Output: ""
    print(f"Longest Common Prefix: {longest_common_prefix(test3)}")  # Output: "inter"
    print(f"Longest Common Prefix: {longest_common_prefix(test4)}")  # Output: "ap"
    print(f"Longest Common Prefix: {longest_common_prefix(test5)}") 
    print(f"Longest Common Prefix: {longest_common_prefix(test6)}") 
