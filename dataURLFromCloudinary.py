#!/usr/bin/env python

import sys
import cloudinary
import cloudinary.utils

if(len(sys.argv) != 2):
	print 'Invalid number of arguments:', len(sys.argv)
	print 'Requires the remote path to the file'
	exit(1)

url, other =cloudinary.utils.cloudinary_url(str(sys.argv[1]),  resource_type = "raw")
print url
#str(sys.argv[1]), public_id = str(sys.argv[2]),  resource_type = "raw")

exit(0)

