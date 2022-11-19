# Description:

This is a simple cross-platform "File Integrity Monitor" written in python.

# What is a FIM (File Integrity Monitor):

A File Integrity Monitor is a software that checks file's integrity in real time.

# Why file integrity monitoring is important:

"File integrity monitoring (FIM), sometimes referred to as file integrity management, is a security process that monitors and analyzes the integrity of critical assets, including file systems, directories, databases, network devices, the operating system (OS), OS components and software applications for signs of tampering or corruption, which may be an indication of a cyberattack." - CROWDSTRIKE

For more informations about why File Integrity Monitoring is important read the following article:

https://www.crowdstrike.com/cybersecurity-101/file-integrity-monitoring/

# How does this proof-of-concept works?

The script creates a hash list (SHA256) for the files in a specific folder.
It then starts a monitoring phase in wich the script calculate each second a hash for each file and then compair it against the original hash stored in the hash list.

# Video of the POC:

[![Watch the video](https://img.youtube.com/vi/mBDkxkRw5ig/sddefault.jpg)](https://www.youtube.com/watch?v=mBDkxkRw5ig)
