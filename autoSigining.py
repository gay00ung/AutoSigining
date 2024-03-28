import os
import subprocess

print("Let's start apk signing!")

APKTOOL = "{PATH}/apktool.jar"
KEYSTORE = "{PATH}/android-key.keystore"
KEYPASS = "your_password"

apk = input("+++ Enter path of apk to sign : ")
signed_apk = input("+++ Enter new name of apk which signed(with .apk) : ")

if os.path.exists(apk):
    subprocess.run(f"java -jar {APKTOOL} d -rf {apk} -o tmp", shell=True)
    print("+++ Decompile completed!\n")

    subprocess.run(f"java -jar {APKTOOL} b tmp -o tmp.apk", shell=True)
    print("+++ Repackaging completed!\n")

    subprocess.run(f"zipalign -p -f -v 4 tmp.apk {signed_apk}", shell=True)
    print("+++ Zipalign completed!\n")

    subprocess.run(f"apksigner sign --ks {KEYSTORE} --ks-pass pass:{KEYPASS} {signed_apk}", shell=True)
    print("+++ Signing completed!\n")

    os.remove("tmp.apk")
    os.remove(f"{signed_apk}.idsig")

    print("+++ Done!")

if not os.path.exists(apk):
    print("*** The file does not exist. Try again!!!\n")
    exit(1)