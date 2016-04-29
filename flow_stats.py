#!/usr/bin/python
# Copyright 2012 William Yu
# wyu@ateneo.edu
#
# This file is part of POX.
#
# POX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# POX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with POX. If not, see <http://www.gnu.org/licenses/>.
#

"""
This is a demonstration file created to show how to obtain flow 
and port statistics from OpenFlow 1.0-enabled switches. The flow
statistics handler contains a summary of web-only traffic.
"""

# standard includes
from pox.core import core
from pox.lib.util import dpidToStr
import pox.openflow.libopenflow_01 as of

# include as part of the betta branch
from pox.openflow.of_json import *

log = core.getLogger()

# handler for timer function that sends the requests to all the
# switches connected to the controller.
def _timer_func ():
  for connection in core.openflow._connections.values():
    
    #log.debug("!!!!!!" + dpidToStr(connection.dpid))
    if(dpidToStr(connection.dpid) == "00-00-00-00-00-05"):
      connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))
      connection.send(of.ofp_stats_request(body=of.ofp_port_stats_request()))

    log.debug("Sent %i flow/port stats request(s)", len(core.openflow._connections))

# handler to display flow statistics received in JSON format
# structure of event.stats is defined by ofp_flow_stats()
def _handle_flowstats_received (event):
  stats = flow_stats_to_list(event.stats)
  log.debug("FlowStatsReceived from %s: %s", 
      (event.connection.dpid), stats)

  # Get number of bytes/packets in flows for web traffic only
  web_bytes1 = 0
  web_flows1 = 0
  web_packet1 = 0
  for f in event.stats:
    #log.info(f.match.nw_src)
    if (f.match.tp_dst == 80 or f.match.tp_src == 80) and (f.match.nw_src == '10.0.0.1' or f.match.nw_dst == '10.0.0.1'):
      #log.info("lololol")
      web_bytes1 += f.byte_count
      web_packet1 += f.packet_count
      web_flows1 += 1
  log.info("HTTP traffic for 10.0.0.1 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes1, web_packet1, web_flows1)


  web_bytes_https1 = 0
  web_flows_https1 = 0
  web_packet_https1 = 0
  for f in event.stats:
    if (f.match.tp_dst == 443 or f.match.tp_src == 443) and (f.match.nw_src == '10.0.0.1' or f.match.nw_dst == '10.0.0.1'):
      web_bytes_https1 += f.byte_count
      web_packet_https1 += f.packet_count
      web_flows_https1 += 1
  log.info("HTTPS traffic for 10.0.0.1 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes_https1, web_packet_https1, web_flows_https1)

   # Get number of bytes/packets in flows for web traffic only
  web_bytes2 = 0
  web_flows2 = 0
  web_packet2 = 0
  for f in event.stats:
    #log.info(f.match.nw_src)
    if (f.match.tp_dst == 80 or f.match.tp_src == 80) and (f.match.nw_src == '10.0.0.2' or f.match.nw_dst == '10.0.0.2'):
      #log.info("lololol")
      web_bytes2 += f.byte_count
      web_packet2 += f.packet_count
      web_flows_https2 += 1
  log.info("HTTP traffic for 10.0.0.2 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes2, web_packet2, web_flows2)


  web_bytes_https2 = 0
  web_flows_https2 = 0
  web_packet_https2 = 0
  for f in event.stats:
    if (f.match.tp_dst == 443 or f.match.tp_src == 443) and (f.match.nw_src == '10.0.0.2' or f.match.nw_dst == '10.0.0.2'):
      web_bytes_https2 += f.byte_count
      web_packet_https2 += f.packet_count
      web_flows_https2 += 1
  log.info("HTTPS traffic for 10.0.0.2 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes_https2, web_packet_https2, web_flows_https2)

   # Get number of bytes/packets in flows for web traffic only
  web_bytes3 = 0
  web_flows3 = 0
  web_packet3 = 0
  for f in event.stats:
    #log.info(f.match.nw_src)
    if (f.match.tp_dst == 80 or f.match.tp_src == 80) and (f.match.nw_src == '10.0.0.3' or f.match.nw_dst == '10.0.0.3'):
      #log.info("lololol")
      web_bytes3 += f.byte_count
      web_packet3 += f.packet_count
      web_flows3 += 1
  log.info("HTTP traffic for 10.0.0.3 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes3, web_packet3, web_flows3)


  web_bytes_https3 = 0
  web_flows_https3 = 0
  web_packet_https3 = 0
  for f in event.stats:
    if (f.match.tp_dst == 443 or f.match.tp_src == 443) and (f.match.nw_src == '10.0.0.3' or f.match.nw_dst == '10.0.0.3'):
      web_bytes_https3 += f.byte_count
      web_packet_https3 += f.packet_count
      web_flows_https3 += 1
  log.info("HTTPS traffic for 10.0.0.3 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes_https3, web_packet_https3, web_flows_https3)

   # Get number of bytes/packets in flows for web traffic only
  web_bytes4 = 0
  web_flows4 = 0
  web_packet4 = 0
  for f in event.stats:
    #log.info(f.match.nw_src)
    if (f.match.tp_dst == 80 or f.match.tp_src == 80) and (f.match.nw_src == '10.0.0.4' or f.match.nw_dst == '10.0.0.4'):
      #log.info("lololol")
      web_bytes4 += f.byte_count
      web_packet4 += f.packet_count
      web_flows4 += 1
  log.info("HTTP traffic for 10.0.0.4 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes4, web_packet4, web_flows4)


  web_bytes_https4 = 0
  web_flows_https4 = 0
  web_packet_https4 = 0
  for f in event.stats:
    if (f.match.tp_dst == 443 or f.match.tp_src == 443) and (f.match.nw_src == '10.0.0.4' or f.match.nw_dst == '10.0.0.4'):
      web_bytes_https4 += f.byte_count
      web_packet_https4 += f.packet_count
      web_flows_https4 += 1
  log.info("HTTPS traffic for 10.0.0.4 from %s: %s bytes (%s packets) over %s flows", 
    dpidToStr(event.connection.dpid), web_bytes_https4, web_packet_https4, web_flows_https4)

# handler to display port statistics received in JSON format
def _handle_portstats_received (event):
  stats = flow_stats_to_list(event.stats)
  log.debug("PortStatsReceived from %s: %s", 
    dpidToStr(event.connection.dpid), stats)
    
# main functiont to launch the module
def launch ():
  from pox.lib.recoco import Timer

  # attach handsers to listners
  core.openflow.addListenerByName("FlowStatsReceived", 
    _handle_flowstats_received) 
  core.openflow.addListenerByName("PortStatsReceived", 
    _handle_portstats_received) 

  # timer set to execute every five seconds
  Timer(5, _timer_func, recurring=True)