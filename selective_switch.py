"""
More or less just l2_learning except it ignores a particular switch
"""
from pox.core import core
from pox.lib.util import str_to_dpid
from pox.lib.util import dpid_to_str
from pox.forwarding.l2_learning import LearningSwitch
from pox.misc.firewall import Firewall
from pox.misc.updated_load_balancer import iplb
from pox.misc.lb import LoadBalancer
 
 
def launch ():  
  #ignore_dpid = str_to_dpid(ignore_dpid)
 
  def _handle_ConnectionUp (event):
    if dpid_to_str(event.dpid) == "00-00-00-00-00-01":
      core.getLogger().info("Connection %s" % (event.connection,))
      Firewall(event.connection, False)
    elif dpid_to_str(event.dpid) == "00-00-00-00-00-02":
      core.getLogger().info("Connection %s" % (event.connection,))
      Firewall(event.connection, False)
    elif dpid_to_str(event.dpid) == "00-00-00-00-00-05":
      core.getLogger().info("Connection %s" % (event.connection,))
      LearningSwitch(event.connection, False)
    elif dpid_to_str(event.dpid) == "00-00-00-00-00-03":
      core.getLogger().info("Connection %s" % (event.connection,))
      LearningSwitch(event.connection, False)
      #LoadBalancer(event.connection)
    elif dpid_to_str(event.dpid) == "00-00-00-00-00-04":
      core.getLogger().info("Connection %s" % (event.connection,))
      LearningSwitch(event.connection, False)
      #LoadBalancer(event.connection)
   # elif dpid_to_str(event.dpid) == "00-00-00-00-00-04":
      #from proto.arp_responder import launch as arp_launch
      #arp_launch(eat_packets=False,**{str("10.0.0.10"):True})
      #import logging
      #logging.getLogger("proto.arp_responder").setLevel(logging.WARN)
      #core.getLogger().info("Connection %s" % (event.connection,))
      #iplb(event.connection, "10.0.0.10",["10.0.0.5","10.0.0.6"])
      #LoadBalancer(event.connection)
    
  
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)