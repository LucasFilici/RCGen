# Windows
https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/

1. build the thing
pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import PyQt5 --noconsole --add-data "WindowIcon.ico;." RCGen.py

2. InstallForge Build (change version and replace old files first)


# MacOS
https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/

1. Build the thing
pyinstaller --windowed --icon"WindowIcon.icns" RCGen.py

2. create-dmg script file (call it "builddmg.sh"):
#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/RCGen.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/RCGen.dmg" && rm "dist/RCGen.dmg"
create-dmg \
  --volname "RCGen" \
  --volicon "WindowIcon.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "RCGen.app" 175 120 \
  --hide-extension "RCGen.app" \
  --app-drop-link 425 120 \
  "dist/RCGen.dmg" \
  "dist/dmg/"

3. chmod +x builddmg.sh
4. ./builddmg.sh
