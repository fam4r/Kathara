import sys
import netkit_commons as nc
import argparse

DEBUG = nc.DEBUG
nc.DEBUG = False

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('-d', '--directory', required=False, help='Folder contining the lab.')
parser.add_argument('-f', '--full', required=False, action="store_true")

args, unknown = parser.parse_known_args()

lab_path = args.path.replace('"', '')
if args.directory:
    lab_path = args.directory.replace('"', '')

if args.full:
    has_invalid_characters = False
    (machines, links, _, _) = nc.lab_parse(lab_path)
    for machine_name, _ in machines.items():
        if (' ' in machine_name) or ('"' in machine_name) or ("'" in machine_name):
            has_invalid_characters = True
            break
    if not has_invalid_characters:    
        for link in links:
            if (' ' in link) or ('"' in link) or ("'" in link):
                has_invalid_characters = True
                break

    if has_invalid_characters:  
        print "Invalid characters in machine names or link names\n"
        sys.exit(1)

if sys.version_info >= (3, 0):
    print ("Requires Python 2.x, not Python 3.x\n")
    sys.exit(1)
