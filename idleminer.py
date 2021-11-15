import os, sys, subprocess, time, signal, win32api

IDLETIME = 900
ALGO = 'ETHASH'
POOL = ""
WALLET = ""


def main():
    lolminerWorking = False
    print("idleMiner Started")
    try:
        while(True):
            if getIdleTime() >= IDLETIME and not lolminerWorking:
                print("Starting lolMiner")
                lolminer = subprocess.Popen(['lolMiner.exe', '--algo', ALGO, '--pool', POOL, '--user', WALLET, '--watchdog', 'exit'])
                lolminerWorking = True
            elif getIdleTime() < IDLETIME and lolminerWorking:
                print("Stopping lolMiner")
                lolminer.kill()
                lolminerWorking = False
            time.sleep(1)
    except KeyboardInterrupt:
        print('idleMiner stopped')


def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0
    

if __name__ == "__main__":
    main()