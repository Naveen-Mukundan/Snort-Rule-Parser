# Snort-Rule-Parser

Snort is a free open source network intrusion detection system and intrusion prevention system. Snort's open source network-based intrusion detection/prevention system (IDS/IPS) has the ability to perform real-time traffic analysis and packet logging on Internet Protocol (IP) networks. Snort performs protocol analysis, content searching and matching. The program can also be used to detect probes or attacks, including, but not limited to, operating system fingerprinting attempts, semantic URL attacks, buffer overflows, server message block probes, and stealth port scans. Snort can be configured in three main modes: sniffer, packet logger, and network intrusion detection. In sniffer mode, the program will read network packets and display them on the console. In packet logger mode, the program will log packets to the disk. In intrusion detection mode, the program will monitor network traffic and analyze it against a rule set defined by the user. The program will then perform a specific action based on what has been identified.

# Requirements:
	1) Install idstools.
	2) Download the latest Snort rules from the link provided below.
	3) Program file and "snort3-community.rules" file should be in the same directory.
	
To install idstools: 
Latest Release (Recommended):

   	pip install idstools

or on Fedora and CentOS (with EPEL):

  	yum install python-idstools

Latest from Git:
  
    pip install https://github.com/jasonish/py-idstools/archive/master.zip

Manually:
The idstools programs do not have to be installed to be used, they can be executable directly from the archive directory:

        ./bin/idstools-rulecat

        Or to install manually:

        python setup.py install

For more information about idstools, visit: https://github.com/jasonish/py-idstools

To download latest snort rules, visit: https://www.snort.org/downloads


Methods:

     msg - The msg keyword tells the logging and alerting engine the message to print with the packet dump or alert.

    reference - The reference keyword allows rules to include references to external attack identification systems.

    gid - The gid keyword (generator id) is used to identify what part of Snort generates the event when a particular rule fires.

    sid - The sid keyword is used to uniquely identify Snort rules.

    rev - The rev keyword is used to uniquely identify revisions of Snort rules.

    classtype - The classtype keyword is used to categorize a rule as detecting an attack that is part of a more general type of attack class.

    priority - The priority keyword assigns a severity level to rules.

    metadata - The metadata keyword allows a rule writer to embed additional information about the rule, typically in a key-value format.


For more information, visit: http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node31.html

