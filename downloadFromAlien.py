import os
import subprocess

local_dir = "/Users/oveis/Desktop/QC/23n/"
directory = "/alice/data/2023/LHC23n/"
runList =   ["536255", "536257", "536261", "536262", "536338", "536339", "536340", "536343", "536344", "536346", "536370", "536400"]
apass = "cpass0"

for run in runList:
    target = subprocess.run(["alien.py","find",directory+run+"/"+apass+"/QC/","QC.root"], capture_output=True)
    if len(target.stdout) > 0 : 
        target_path = target.stdout[:-1].decode('UTF-8')
        print("Downloading "+target_path)
        subprocess.run(["alien.py","cp","alien:"+target_path,"file:"+local_dir+run+".root"])
    else:
        target = subprocess.run(["alien.py","find",directory+run+"/"+apass+"/","QC_fullrun.root"], capture_output=True)
        if len(target.stdout) > 0 : 
            target_path = target.stdout[:-1].decode('UTF-8')
            print("Downloading "+target_path)
            subprocess.run(["alien.py","cp","alien:"+target_path,"file:"+local_dir+run+".root"])
        else: 
            print("File "+directory+run+"/"+apass+"/QC/001/QC.root"+ "  not found!")

