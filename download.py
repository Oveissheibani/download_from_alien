import os
import subprocess

local_dir = "/Users/oveis/Desktop/child1_extra/"
directory = "/alice/data/2016/LHC16q/000265500/pass2_CENT_wSDD/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_1/"

# Fetch all AnalysisResults.root file paths
output = subprocess.run(["alien.py","find",directory,"AnalysisResults.root"], capture_output=True)
file_paths = output.stdout.decode('utf-8').split('\n')

# Extract unique run directories
run_directories = {os.path.dirname(path) for path in file_paths}

for run_dir in run_directories:
    target_path = run_dir + "/AnalysisResults.root"
    run_id = os.path.basename(run_dir)
    print("Downloading "+target_path)
    subprocess.run(["alien.py","cp","alien:"+target_path,"file:"+local_dir+"AnalysisResults_"+run_id+".root"])
    
    
    
#/alice/data/2016/LHC16q/000265424/pass2_CENT_wSDD/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_1
    
#/alice/data/2016/LHC16q/000265378/pass2_CENT_wSDD/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_1


#/alice/data/2016/LHC16q/000265344/pass2_CENT_wSDD/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_1


#/alice/data/2016/LHC16q/000265343/pass2_CENT_wSDD/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_1


#/alice/data/2016/LHC16q/000265500/pass2_FAST/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_2

#/alice/data/2016/LHC16q/000265378/pass2_FAST/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_2


#/alice/data/2016/LHC16q/000265344/pass2_FAST/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_2

#/alice/data/2016/LHC16q/000265343/pass2_FAST/AOD244/PWGHF/D2H_pPb/1488_20230412-0508_child_2
