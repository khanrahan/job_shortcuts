#!/usr/bin/env python

import argparse
import os

JOB_TREE = "/jobs/ads/test_test_j1111111/"
DESTINATION = "/Users/kieran/Python/job_shortcuts"

JOB_NAME = os.path.basename(os.path.normpath(JOB_TREE))
DIRS = [i for i  in os.listdir(JOB_TREE)]
MATERIALS = [i for i in DIRS if i.isupper()]

for x in MATERIALS:
    shots = os.listdir(os.path.join(JOB_TREE, x))
    shot_numbers = [i[2:] for i in shots]
    for y in shots:
        source = os.path.join(JOB_TREE, x, y, "_".join(["n", y[2:]]),
                              "live_action")
        link_dir = os.path.join(DESTINATION, JOB_NAME, "_".join([x, y]), "nuke")
        os.makedirs(link_dir)
        os.symlink(source, os.path.join(link_dir, "live_action"))
