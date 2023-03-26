# -*- coding: utf-8 -*-
import sys
import subprocess
import json

# main function
if __name__ == "__main__":

    # get docker inspect info as json
    command = ["docker", "inspect", "cranky_shockley"]
    res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    inspect_str = res.stdout.decode('UTF-8')
    inspect = json.loads(inspect_str)
    #print (json.dumps(inspect, indent=4, ensure_ascii=False))

    ##
    ## generate docker run command
    ##

    # port mapping




