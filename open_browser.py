"""Simple script to open web browser
"""

import os
import time
import random
import logging
import yaml
import argparse
import webbrowser


# Define web browser to use
use_browser = "google-chrome"
# Logging level
log = logging.getLogger('aux_log')
log.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
log.addHandler(ch)


def get_arg():
    """Method to get required info from user
    """
    txt_ini = "Script to launch web browser for list of urls in"
    txt_ini += " random order"
    arg = argparse.ArgumentParser(description=txt_ini)
    #
    h1 = 'Name of the YAML file containing the urls'
    arg.add_argument('in_yaml', help=h1)
    #
    f = "url"
    h2 = "Field to use from the YAML input file. Default: {0}".format(f)
    arg.add_argument("--field", help=h2, default=f)
    #
    h3 = "Flag to NOT open urls at random times, from N1 to N2 seconds"
    arg.add_argument("--rdm", help=h3, action="store_false")
    # Parse
    arg = arg.parse_args()
    return arg

def yaml_to_dict(fname, loader=yaml.FullLoader):
    """ Read YAML file and return a dcitionary to work with. If CLASS is
    used, this should go into the constructor/init

    Parameters
    ----------
    fname : string
        Filename of the YAML file
    loader : YAML constructor
        Default is FullLoader, but other options are available too.

    Returns
    -------
    x_yaml : dict
        Dictionary containing the hierarchical structure of the YAML
        file
    """
    try:
        with open(fname, "r") as tmp:
            x_yaml = yaml.load(tmp, Loader=loader)
    except:
        log.error("YAML file {0} unreadable".format(fname))
        log.error("Unexpected error: {0}".format(sys.exc_info()[0]))
        # print("YAML file {0} unreadable".format(fname))
        # print("Unexpected error: {0}".format(sys.exc_info()[0]))
        raise
    return x_yaml

def aux_main():
    """Auxiliary method to call the execution
    """
    # Get the arguments
    xarg = get_arg()
    # Load the YAML file
    url_dict = yaml_to_dict(xarg.in_yaml)
    # Infinite loop to open urls until script is stopped
    # Initialise a counter, to close the web browser after N openings
    cnt = 0
    cnt2 = 0
    while True:
        log.info("Call number: {0}".format(cnt2 + 1))
        random.seed()
        # Select randomly one of the urls
        tmp_url = random.choice(url_dict[xarg.field])
        # Define a callable
        if (use_browser == "google-chrome"):
            webbr = webbrowser.get(using="google-chrome")
        webbr.open(tmp_url, new=2, autoraise=False)
        log.info(tmp_url)
        # From second openning onwards, wait some seconds
        if xarg.rdm:
            # Randomly select a number in the range, to wait
            # until going to the next loop
            nsec = random.randrange(40, 40 * 2.2)
            log.info("Waiting {0} s".format(nsec))
            time.sleep(nsec)
        else:
            nsec = 40
            log.info("Waiting {0} s".format(nsec))
            time.sleep(nsec)
        # After 10 openings, close the web browser and reset counter
        if cnt > 4:
            logging.info("Restarting browser")
            if (use_browser == "google-chrome"):
                os.system("killall -9 'chrome'")
                log.info("Terminated web browser")
            cnt = 0
        cnt += 1
        cnt2 += 1
    return

if __name__ == "__main__":
    aux_main()
