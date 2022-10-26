import json
from os import remove
from os.path import exists
from app.worker.modules.Sublist3r import sublist3r
# import sublist3r 

def run_sublister(url:str):
    subdomains = sublist3r.main(url, 40, url, ports= None, silent=False, verbose= True, enable_bruteforce= False, engines="google,bing,PassiveDNS")
    return subdomains


def sublister_wrapper(url: str):
    try:
        print('sublister is running for {}'.format(url))
        result = run_sublister(url)
        if result:
            print('RESULTS', result)
        return result
    except:
        print('sublister failed for {}.'.format(url))

