# TugaRecon - HackerTarget module, write by skynet0x01
# TugaRecon, tribute to Portuguese explorers reminding glorious past of this country
# Bug Bounty Recon, search for subdomains and save in to a file
# Coded By skynet0x01
# import modules
################################################################################
import time
import requests
# Import internal modules
from modules import tuga_useragents #random user-agent
# Import internal functions
from functions import write_file
from functions import DeleteDuplicate
from functions import G, W
################################################################################
class Hackertarget:

    def __init__(self, target, output):

        self.target = target
        self.output = output
        self.module_name = "HackerTarget"
        self.engine = "hackertarget"

        print(G + f"HackerTarget: Enumerating subdomains now for {target} \n" + W)

        self.response = self.engine_url()
        self.enumerate(self.response, output, target)

        #if self.output is not None:
            #DeleteDuplicate(self.engine + '_' + self.output, target)
################################################################################
    def engine_url(self):
        url = f"https://api.hackertarget.com/hostsearch/?q={self.target}"
        response = requests.get(url, headers=tuga_useragents.useragent())
        return response
################################################################################
    def enumerate(self, response, output, target):
        subdomains = []
        subdomainscount = 0
        sub = []
        start_time = time.time()
        try:
            while subdomainscount < 10000:

                # Remove "," an IP from list
                remove_ip = response.text.replace(",", " ")
                subdomains = remove_ip.split()

                subdomainscount = subdomainscount + 2
                print(f"[*] {subdomains[subdomainscount]}")

                # Write  to a file
                if self.output is not None:
                    write_file(subdomains[subdomainscount], self.engine + '_' + self.output, target)

            if self.output:
                print(f"\nSaving result... {self.engine + '_' + self.output}")


        except IndexError:
            pass

        if not subdomains:
            print(f"[x] No data found for {self.target} using  HackerTarget.")
        else:
            print(
                G + f"\n[**] TugaRecon is complete.  HackerTarget: {int((subdomainscount / 2) - 1)} subdomains have been found in %s seconds" % (
                        time.time() - start_time) + W)
