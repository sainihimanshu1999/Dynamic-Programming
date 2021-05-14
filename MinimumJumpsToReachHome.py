'''
This question is little tricky, neverthless, it's solved by bfs
'''
def minjump(self,forbidden,a,b,x):
    if not x:
        return -1

    forbidden = set(forbidden)
    threshold = max(forbidden+[x])+a+b
    seen = set([0])
    q = [[0,0]]

    while q:
        pos,jump = q.pop(0)

        if pos+a not in forbidden and pos+a not in seen and pos+a<=threshold:
            if pos+a == x:
                return jump+1
            q.append([pos+a,jump+1])
            seen.add(pos+a)

        if pos-b>0 and pos-b not in forbidden and pos-b not in seen:
            if pos-b==x:
                return jump+1
            seen.add(pos-b)

            if pos-b+a not in forbidden and pos-b+a not in seen and pos-b+a<=threshold:
                if pos-b+a == x:
                    return jump+2
                q.append([pos-b+a,jump+2])
                seen.add(pos-b+a)


    return -1