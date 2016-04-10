#!/usr/bin/env python

import sys
import cloudinary
import cloudinary.uploader

if(len(sys.argv) != 3):
	print 'Invalid number of arguments:', len(sys.argv)
	print 'Requires the local path to the file and the remote path to the file'
	exit(1)

cloudinary.uploader.upload(str(sys.argv[1]), public_id = str(sys.argv[2]),  resource_type = "raw")

exit(0)
