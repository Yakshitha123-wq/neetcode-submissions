class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                a=stack.pop()
                b=stack.pop()
                if ch=="+":
                    res=b+a
                    stack.append(res)
                elif ch=="-":
                    res=b-a
                    stack.append(res)
                elif ch=="*":
                    res=b*a
                    stack.append(res)
                else:
                    res=b/a
                    stack.append(int(res))
        return stack[0]
        