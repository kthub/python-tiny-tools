# -*- coding: utf-8 -*-
#
# This script is rest client sample using urllib.request
#
import urllib.request as ur
import json

##
## Set Basic Authentication Parameters
##
def set_basic_auth(top_level_url, user, pwd):

    # create a password manager
    password_mgr = ur.HTTPPasswordMgrWithDefaultRealm()

    # add the username and password    
    password_mgr.add_password(None, top_level_url, user, pwd)

    # create "handler"
    handler = ur.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = ur.build_opener()
    opener.add_handler(handler) # can add another opener with same way if required. (ex. proxy)

    # install the opener
    # Now all calls to urllib.request.urlopen use this opener
    ur.install_opener(opener)

##
## Main
##
if __name__ == "__main__":

    url = "https://api.github.com/users/kthub/repos"

    # set password for the basic authentication
    set_basic_auth(url, "kthub", "ghubpass2")

    # set HTTP header
    req = ur.Request(url, method='GET')
    req.add_header("Accept", "application/vnd.github.v3+json")

    # connect to the api provider (HTTP/1.1)
    conn = ur.urlopen(req)

    # print response header
    for key, value in conn.getheaders():
        print(key, ' : ', value)

    # print response body
    data = conn.read()
    res_json_str = data.decode('UTF-8') # decode (binary to string)
    #print(res_json_str)

    res_json = json.loads(res_json_str) # convert string to object

    # pretty print
    print (json.dumps(res_json, indent=4, ensure_ascii=False))

    # traverse sample
    for repos in res_json:
        print(repos["name"]) # print the name of the each repository
