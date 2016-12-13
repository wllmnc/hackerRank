import subprocess
import sys
## call date command ##

def getPath(program):
        (output, err) = execute("locate "+ program)
        if output!="":
                cmd=output.split("\n")[0]
                return cmd
        else:
                return ""
def execute(cmd):
        print cmd
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        return (output, err)



path=getPath(sys.argv[1])
if(path!=""):
        print path
else:
        print "NO coincidenses with " + sys.argv[1]


print output
