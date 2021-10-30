#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:46:49 2021

@author: thierry
"""

import logging
#logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('nb')
def run(app, *argv):
    argv = list(argv)
    argv.insert(0, '--num-workers=4')  # <1>
    log.info("Running: {}({!r}).main()".format(app, argv))
    
    
run("app_test", 3, 4, 5, 10)