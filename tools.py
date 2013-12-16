#!/usr/bin/env python
# MYndMap toolkit

import logging

# Logging facility
logging.basicConfig(filename="myndmap.log",
                    format='%(asctime)s - %(name)s - %(levelname)-6s - %(message)s',
                    level=logging.DEBUG)
log = logging.getLogger('myndmap')


def info(msg):
    log.info(msg)

def debug(msg):
    log.debug(msg)
    
def warning(msg):
    log.warning(msg)
    
def error(msg):
    log.error(msg)
    
