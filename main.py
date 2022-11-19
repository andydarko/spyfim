import hashlib
import os
import time
import datetime

def clearConsole(): os.system('cls' if os.name == 'nt' else 'clear')

def getFileHash(filePath):
    
    with open(filePath, 'rb') as file:

            BLOCKSIZE = 65536
            hasher = hashlib.sha256()

            buffer = file.read(BLOCKSIZE)

            while len(buffer) > 0:

                hasher.update(buffer)
                buffer = file.read(BLOCKSIZE)

    file.close

    return hasher.hexdigest().upper()

def createFingerprintFile(fingerprintFile, scanDirectory):

    print("Creating new fingerprint file ...")

    fileList = os.listdir(scanDirectory)    # Load file names from scan directory;
    
    with open(fingerprintFile, 'w') as file:

        for fileName in fileList:
            
            filePath = scanDirectory + '/' + fileName  
            file.write(filePath + ' | ' + getFileHash(filePath) + '\n') # ADD EACH FILE PATH AND SHA256 HASH TO FINGERPRINT FILE;

    file.close

    print("\033[92mFingerprint file created!\033[00m") 

def startActiveMonitoring(fingerprintFile, scanDirectory):
    
    print("\nStart monitoring '" + scanDirectory + "' ...\n")

    fileList = []
    hashList = []

    # LOAD FINGERPRINT FILE IN MEMORY #
    with open(fingerprintFile) as file:
        data = file.read()

    dataset = data.split("\n")          # Split dataset each new line;
    dataset = dataset[:-1]              # Remove last empty spot from dataset;

    for set in dataset:
        hashList.append(set.split(" | ")[1])

    for set in dataset:
        fileList.append(set.split(" | ")[0])

    while True:
        # CHECK IF FINGERPRINT IN FILE = CALCULATED HASH (EACH SECOND) #       
        fileIndex = 0
        
        for file in fileList:

            fileName = fileList[fileIndex]
            storedHash = hashList[fileIndex]

            fileHash = getFileHash(fileName)
            
            timestamp = datetime.datetime.now()
            
            if (str(fileHash) == str(storedHash)):
                print(timestamp.strftime('%Y-%m-%d %H:%M:%S') + "\033[92m [OK]\033[00m" + " - " + "\033[92m{}\033[00m" .format(fileName) + " | " + fileHash)
            else:
                print("\033[91m{}\033[00m" .format(timestamp.strftime('%Y-%m-%d %H:%M:%S')) + "\033[91m [MISMATCH !]\033[00m" + " - " + "\033[91m{}\033[00m" .format(fileName) + " | " + fileHash)

            fileIndex +=1
            time.sleep(1)

def main():

    clearConsole()

    scanDirectory = input("Enter FULL PATH to the directory you want to check: ")
    fingerprintFile = input("Enter FULL PATH to the fingerprint file you want to use: ")

    if not (os.path.exists(fingerprintFile)):

        print("\033[91m\nFingerprint file not found!\033[00m")
        createFingerprintFile(fingerprintFile, scanDirectory)

    startActiveMonitoring(fingerprintFile, scanDirectory)

if __name__ == '__main__':
    main()