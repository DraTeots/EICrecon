desc = """

THIS IS A TEMPLATE

This script is a simple demonstration of how to run eicrecon with available digitization/reconstruction flag
Currently this script is created manually (TODO automatic generation) so if flags here is outdated, please file an issue

    python3 full_flags_run.py input_file.edm4hep.root output_name_no_ext
    
Script should successfully run and create files:

    output_name_no_ext.edm4eic.root    # with output flat tree
    output_name_no_ext.ana.root        # with histograms and other things filled by monitoring plugins
    
One can add -n/--nevents file with the number of events to process    

"""

import subprocess
from datetime import datetime
import argparse

start_time = datetime.now()

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('input_file', help="Input file name")
parser.add_argument('output_base_name', help="Output files names (no file extensions here)")
parser.add_argument('-n', '--nevents', default="0", help="Number of events to process")
args = parser.parse_args()

run_command = [
    f"eicrecon",
    f"-Pplugins=default_flags",
    f"-Pjana:debug_plugin_loading=1",
    f"-Ppodio:output_file={args.output_base_name}.tree.edm4eic.root",
    f"-Pjana:nevents={args.nevents}",
    f"-Pacts:MaterialMap=calibrations/materials-map.cbor",
    f"-Phistsfile={args.output_base_name}.ana.root",
    f"{args.input_file}",
]

# (!) NEXT LINE WILL BE REPLACED BY TEMPLATE #
reco_parameters_flags = []

run_command.extend(reco_parameters_flags)

subprocess.run(" ".join(run_command), shell=True, check=True)


print("Start date and time: ")
print(start_time.strftime('%Y-%m-%d %H:%M:%S'))

end_time = datetime.datetime.now()
print("End date and time: ")
print(end_time.strftime('%Y-%m-%d %H:%M:%S'))
print(end_time-start_time)


