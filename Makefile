# Makefile

.PHONY: default clean
default:
	csc /nologo /out:btsdripper.exe btsdripper.cs
clean:
	rm -f btsdripper.exe
