#!/usr/bin/python
import sys
#sys.path.append("/usr/local/net_evi_plugin/")
import send
def getEviFromCompute():
	evi_list=["l2-topology_info","l2-openflow_BDD","l2-sec_group"]
	controller=send.Controller()
	for message in evi_list:
		response=controller.request(message)
		print response
getEviFromCompute()
