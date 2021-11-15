# idleMiner

## Overview

idleMiner is a manager for lolMiner that starts mining when the PC has been in idle for a defined amout of time and stops it when the PC becomes active. Useful when you are using the same machine for mining and working. 


## Usage

### Prerequisites
 - A windows machine
 - installed and working lolMiner
 - Python 3

### Dependencies
Install dependencies

    pip install pywin32


#### Configuration

Copy both files to the folder, where you have lolMiner.exe

Edit the following values in idleminer.py

    IDLETIME = 900
    ALGO = 'ETHASH'
    POOL = ""
    WALLET = ""

#### Running idleMiner
Run idleminer.bat

#### Running idleMiner on startup (optional)
Make a shortcut of idleminer.bat and copy it to the windows startup folder


