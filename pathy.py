import os

class Path:
    expanded = None
    def __init__(self,*components):
        self.cs = components
    def join(self,expand=False):
        result = []
        for c in self.cs:
            if isinstance(c,Path):
                if expand:
                    result.append(c.expand())
                else:
                    result.extend(c.join())
            else:
                result.append(str(c))
        return result
    def __str__(self):
        return os.path.join(*self.join())
    def expand(self):
        if self.expanded is None:
            self.expanded = self.derpexpand()
        return self.expanded
    def derpexpand(self):
        return os.path.join(*self.join(expand=True))
    def __call__(self,*components):
        return type(self)(*(self.cs+components))
    def exists(self):
        return os.path.exists(self.derpexpand())
    def mkdir(self):
        try: os.makedirs(self.expand())
        except OSError: pass
    def rename(self,other):
        print(Path(other).expand())
        os.rename(self.expand(),Path(other).expand())
    def tail(self,tail):
        return Path(*(self.cs[:-1]+(self.cs[-1]+tail,)))
class Expand(Path):
    def derpexpand(self):
        return os.path.expanduser(str(self))
        
def maybePath(component):
    return component if isinstance(component,Path) else Path(component) 
