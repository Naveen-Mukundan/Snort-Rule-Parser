# Author: Naveen Mukundan Ravindran

import sys

# Your system should have installed idstools from Python 3 packages. Check the description for how to install it.
from idstools import rule

# Download the latest snort rules from the website provided in the description
filename="snort3-community.rules"

for rule in rule.parse_file(filename):
	
	# Print the Action of the rule
	print("Action: %s" %rule.action)

	# Print the Message Contents of the rule
  	print("Message: %s" %rule.msg)

	# Print the Generator ID of the rule
  	print("Generator id: %d" %rule.gid)

	# Print the Snort Rule ID of the rule
  	print("Rule id: %d" %rule.sid)

	# Print the Revision Integer of the rule
  	print("Revision Integer: %d" %rule.rev)

	# Print the Class type of the rule
  	print("Class Type: %s" %rule.classtype)

	# Print the Priority Integer of the rule
  	print("Priority Integer: %d" %rule.priority)

	# Print the Reference of the rule
  	print("Reference: %s" %rule.reference)

	# Print the Meta data of the rule
  	print("Metadata: %s" %rule.metadata)







