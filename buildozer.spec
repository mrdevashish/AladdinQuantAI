[app]

title = AladdinQuantAI

package.name = aladdinquantai

package.domain = org.devashish

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,requests

orientation = portrait

fullscreen = 0


# ---------------- ANDROID PERMISSIONS ----------------

android.permissions = INTERNET


# ---------------- ANDROID BUILD SETTINGS ----------------

android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.build_tools_version = 33.0.2


# ---------------- ARCHITECTURE ----------------

android.archs = arm64-v8a, armeabi-v7a


# ---------------- BACKUP ----------------

android.allow_backup = True


# ---------------- IOS (leave unchanged) ----------------

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

ios.codesign.allowed = false


[buildozer]

log_level = 2
warn_on_root = 1
