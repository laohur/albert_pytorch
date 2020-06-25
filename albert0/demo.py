from subprocess import Popen

with open("log.txt",'w') as fout:
    child=Popen(["python","demo2.py"],stdout=fout)
re=child.wait()
print(re)