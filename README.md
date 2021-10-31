# TugaRecon

                               ______                  ____                      
                              /_  __/_  ______ _____ _/ __ \___  _________  ____ 
                               / / / / / / __ `/ __ `/ /_/ / _ \/ ___/ __ \/ __ \                
                              / / / /_/ / /_/ / /_/ / _, _/  __/ /__/ /_/ / / / /               
                             /_/  \__,_/\__, /\__,_/_/ |_|\___/\___/\____/_/ /_/              
                                       /____/                                    
  
                                           # Coded By skynet0x01 #

  tugarecon is a python tool designed to enumerate subdomains using modules. It helps penetration testers and bug hunters collect and gather subdomains for the domain they are targeting.  Bruteforce was integrated was a module to increase the possibility of finding more subdomains using bruteforce with an improved wordlist.
TugaRecon, tribute to Portuguese explorers reminding glorious past of this country.

During the 15th and 16th centuries, Portuguese explorers were at the forefront of European overseas exploration, which led them to reach India, establish multiple trading posts in Asia and Africa, and settle what would become Brazil, creating one of the most powerful empires.

# Version
1.0

More modules will be added!
And much more... :)

# Screenshots

![tugarecon_bughunters](https://user-images.githubusercontent.com/39160972/76518858-cb105900-6457-11ea-9ac3-7ecfffc74fd8.png)

![tugarecon1](https://user-images.githubusercontent.com/39160972/72821211-1da77300-3c68-11ea-80a9-db8ea6716e4b.png)

![Screenshot from 2020-01-26 20-59-16](https://user-images.githubusercontent.com/39160972/73141832-4d97b180-4080-11ea-9adc-a83667ea9687.png)

# Installation

git clone https://github.com/skynet0x01/tugarecon.git

# Usage

        python3 tugarecon.py -d google.com
        python3 tugarecon.py -d google.com --enum ssl
        python3 tugarecon.py -d google.com --enum certspotter --savemap
        python3 tugarecon.py -d google.com -o google.txt
        python3 tugarecon.py -d google.com --savemap
        python3 tugarecon.py -d google.com --bruteforce
        python3 tugarecon.py -d google.com --bruteforce --full
        python3 tugarecon.py -d google.com -b --full

# Modules

    bruteforce (tugascan - wildcards, wordlist)
    certspotter
    hackertarget
    virustotal
    threatcrowd
    ssl
    entrust
    googlesearch

# Dependencies
You need to install [dnspython](http://www.dnspython.org) to do DNS query

        dnspython version 1.16.0
        threading
        queue
        re
        os
        time
        sys
        webbrowser
        urllib3
        random

# DONATIONS:

Donations are welcome. This will help improved features, frequent updates and better overall support.

BTC:   1C1q8c2bpSvRBpupD43p1CAV98YXkNnnDx

Doge:  DRU62QbterkCpMHEG7ZMSZXEJQzyR13CRB

# News
- [x] Save results: results/domain_target/ files
- [x] Releasing a new version 0.45b
- [x] Fast enumerate BruteForce scan upgrade
- [x] Wordlist
- [x] Mapping the domain and save image
- [x] add new module
- [x] add new folder results/domain_target/  ex: results/tesla.com/ 
- [x] Random User-Agent
- [ ] Add more modules

   ![tugarecon](https://user-images.githubusercontent.com/39160972/75924110-45d8e300-5e5e-11ea-8832-55c08ecc2902.jpg)
