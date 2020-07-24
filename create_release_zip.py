#!/usr/bin/env python
# create_release_zip.py

import sys
import zipfile

if len(sys.argv) != 2:
	print("usage: {} [version]".format(sys.argv[0]), file=sys.stderr)
	exit(1)

version = sys.argv[1]

zf = zipfile.ZipFile("btsdripper-{}.zip".format(version), mode="w", compression=zipfile.ZIP_DEFLATED)
zf.write("btsdripper.exe")
zf.write("GPS here.bat")
zf.writestr("readme.txt", "BTSD Ripper " + version + " by LDA_suku\r\n\r\nMicrosoft .NET Core is required: https://dotnet.microsoft.com/download\r\n\r\nMake sure to read the ENTIRE OUTPUT of the program!\r\n\r\nSource code at https://github.com/LDAsuku/BTSD-Ripper\r\n")
zf.close()
