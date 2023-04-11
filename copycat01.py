#!/usr/bin/env python3
"""Working with imports and copying files"""

import shutil
import os

# moving into the working directory
os.chdir("/home/student/mycode/")

# copying a single file within the directory
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copying an entire directory/tree within that directory
shutil.copytree("5g_research/", "5g_research_backup/")
