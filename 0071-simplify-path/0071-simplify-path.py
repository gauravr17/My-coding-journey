class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        components = path.split('/')
        
        for part in components:
            if part == '' or part == '.':
                continue  # skip empty pieces (from consecutive slashes) and current-dir markers
            elif part == '..':
                if stack:
                    stack.pop()  # go up to parent directory, if possible
            else:
                stack.append(part)  # a valid directory/file name
        
        return '/' + '/'.join(stack)