# cloud_net_evi
#Introduce
Gather openstack multi_tenant network status as evidence. The network status include l2,l3,l4 layer.
l2 will gather topology info for multi tenants from openstack compute nodes hosts libvirt and will make a compare with the topology info
stored in the openstack DB, then we can see if there are other vms in the tenant's network.
l3 will parse the route's relationship between different tenants to see if there is improper route.
l4 will parse the security group policies of tenants network to see if the policies are safe enough for the tenant.
#Detail
The frontend directory is a web front for the module, which i use angularJs and bootstrap to construct the pages.
The backend directory is the network evidence gathering module. The module have mainly to parts:net_evi_plugin and net_evi_agent.

net_evi_plugin part will get the request from front end and will distribute the request to each net_evi_agent installed on each openstack
compute node;then net_evi_agent get the request message from net_evi_plugin, gather network evidence info from each compute node,and send
those evidence back to the net_evi_plugin module.
#Install
For net_evi_agent run:

pip install python-net_evi_agent
