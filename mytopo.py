"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1', ip ='10.0.0.1', mac = '00:00:00:00:00:01' )
        Host2 = self.addHost( 'h2', ip ='10.0.0.2', mac = '00:00:00:00:00:02' )
        Host3 = self.addHost( 'h3', ip ='10.0.0.3', mac = '00:00:00:00:00:03' )
        Host4 = self.addHost( 'h4', ip ='10.0.0.4', mac = '00:00:00:00:00:04' )
        Host5 = self.addHost( 'h5', ip ='10.0.0.5', mac = '00:00:00:00:00:05' )
        Host6 = self.addHost( 'h6', ip ='10.0.0.6', mac = '00:00:00:00:00:06' )

        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )
        #Switch5 = self.addSwitch( 's5' )


        
        # Add links
        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch1 )
        self.addLink(Host3, Switch2)
        self.addLink( Host4, Switch2 )
        self.addLink(Switch1, Switch3)
        self.addLink( Switch2, Switch3 )
        self.addLink(Switch3, Switch4)
        self.addLink(Switch4, Host5)
        self.addLink(Switch4, Host6)
        # self.addLink(Switch4, Host4)
        # self.addLink(Switch5, Host3)
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
