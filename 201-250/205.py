class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds={}
        dt={}
        ls=[];lt=[]
        for cs,ct in zip(s,t):
            if cs in ds and ct in dt:
                if ds[cs]!=dt[ct]:
                    return False
            elif cs not in ds and ct not in dt:
                n=len(ds)
                ds[cs]=n
                dt[ct]=n
            else:
                return False
        return True
