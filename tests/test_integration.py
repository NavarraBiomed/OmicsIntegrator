#!/usr/local/bin/python
'''
Large integration test script.
'''

import os, sys, subprocess, filecmp, shutil, shlex
from optparse import OptionParser

def test_integration(msgsteiner):

    parser=OptionParser()  

    parser.add_option('--msgsteiner',dest='msgsteiner',type='string',help='Path to msgsteiner9 code, be sure to include!')

    phos_weights='Tgfb_phos.txt'

    #garnet requires a configuration file that has all the data
    forest_out='tgfb_garnet_forest_output'
    garnet_conf='tgfb_garnet.cfg' #provided config file
    gcmd='python ../scripts/garnet.py --outdir=%s %s'%(forest_out,garnet_conf) #command

    #forest requires more inputs
    forest_conf='tgfb_forest.cfg' #provided config file
    edge_file='../data/iref_mitab_miscore_2013_08_12_interactome.txt' #interactome

    msgsteinerpath=msgsteiner ##WE NEED MSGSTEINER9 INSTALLED!!!
    
    if msgsteinerpath == None:
	print 'Please provide path to msgsteiner using --msgsteiner option'
	assert 0
	
    forest_out='temp'
    seed = 2
    if not os.path.exists(forest_out): ##FOREST WILL NOT CREATE DIRECTORY FOR YOU, GARNET WILL
	
	script_dir = os.path.dirname(__file_)
	abs_file_path = os.path.join(script_dir, forest_out)
        os.makedirs(abs_file_path)

        fcmd='python ../scripts/forest.py --prize=%s --edge=%s --conf=%s  --outpath=%s --msgpath=%s --seed=%s'%(phos_weights, edge_file, forest_conf, forest_out, msgsteinerpath, seed)
        subprocess.call(shlex.split(fcmd), shell=False)	

	results = filecmp.cmpfiles('temp', 'tgfb_forest_output', ['result_augmentedForest.sif', 'result_dummyForest.sif', 'result_edgeattributes.tsv',
							  'result_info.txt', 'result_nodeattributes.tsv', 'result_optimalForest.sif'], shallow=False)
	shutil.rmtree('temp')
	if len(results[0]) != 6:
		assert 0
	else:
		assert 1

	


	

     
	assert 1

