#!/usr/bin/env python

import os

JOB_TREE = "/jobs/ads/test_test_j1111111/"
DESTINATION = "/Users/kieran/Python/job_shortcuts"

job_name = os.path.basename(os.path.normpath(job_tree))
dirs = [i for i  in os.listdir(job_tree)]
materials = [i for i in dirs if i.isupper()]

def find_shots():
	

def create_link():
	

for i in materials:
    shots = os.listdir(os.path.join(JOB_TREE, i)
