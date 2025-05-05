# RCGen
RCGen is a piece of Free/Libre and Open Source Software that generates swimming report cards.

### How To Install on MacOS
https://www.youtube.com/watch?v=IpwnmOiC8PQ
1. Click `Releases` on the right ->
2. Click the latest version of the software.
3. Click on `Assets`.
4. Click on the installer relevant to your operating system.
  (Mac = `.dmg`)
5. Click `allow` when asked if you want to allow downloads on "github.com".
6. Click on the search icon in the top right and type in `terminal`.
7. Click on the terminal application.
8. In the black box, type in `sudo spctl --master-disable` and hit `return` on your keyboard.
9. Enter the password for your Mac and hit `return` on your keyboard.
9. Find the saved file in your downloads, double click it, and drag `RCGen` into `Applications`.
10. Open `RCGen` in `Applications` or from your `Launchpad`.
11. Click `Open` in response to: _"'RCGen' is an app downloaded from the Internet. Are you sure you want to open it?"_
12. Go back to the terminal, type `sudo spctl --master-enable`, and hit `return` on your keyboard.
13. Enter the password for your Mac and hit `return` on your keyboard.
14. Close the terminal and anything else. Enjoy the software.

### How To Install on PC
https://www.youtube.com/watch?v=tUdrqg-P9dc
1. Click `Releases` on the right ->
2. Click the latest version of the software.
3. Click on `Assets`.
4. Click on the installer relevant to your operating system.
  (Windows = `.exe`)
5. Save the file in your `Downloads` folder (or wherever you want) if prompted.
6. Find the saved file and double click it.
7. In response to the _Microsoft Defender SmartScreen_ prompt, click `More Info` and then click `Run Anyway`.
8. Click `Yes` in response to the "Do you want to allow this app..." prompt.
9. Walk through the installer.
10. Enjoy the software.

***  

## Build/Packaging Instructions</br>**[Not relevant for most users]**

  ### MacOS
  https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/
1. Download the source code and install pyinstaller:
  `pip3 install PyInstaller`
2. Run the following command within the "RCGen-main" folder:
  `pyinstaller --windowed --icon="WindowIcon.icns" RCGen.py`
3. Install "Brew": https://brew.sh/
4. Install create-dmg:
`brew install create-dmg`
5. Create the following text document and name it "builddmg.sh":
```
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
```
6. Place your newly-created "builddmg.sh" script within the "RCGen-main" folder (the root directory).
7. Run the following command on the newly-created file to make it executable: `chmod +x builddmg.sh`
8. Run the newly-created script: `zsh -x ./builddmg.sh`
9. Enjoy your RCGen Installer within the "dist" folder (within RCGen-main").

  ### Windows
  https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/
1. Download the source code and install pyinstaller:\
  `pip3 install PyInstaller`
2. Run the following command within the "RCGen-main" folder:\
  `pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import PyQt5 --noconsole --add-data "WindowIcon.ico;." RCGen.py`\
  At this point, you will have a functional .exe file within the "dist" folder (within "RCGen-main").\
  If you wish to create an installer, the solution I used was InstallForge.
4. Install InstallForge: https://installforge.net/download/
5. Within InstallForge, on the left side, click "General" under "General"
6. Type "RCGen" to the right of "Product Name".
7. Type "v0.1.0" to the right of "Product Version".
8. Type "Lucas Filici" to the right of "Company Name".
9. On the left side, click on "Files" under "Setup".
10. Click on "Add Files" on the top ribbon and add all files within the "RCGen" folder (within ~/RCGen-main/dist/).
11. Click on "Add Folders" on the top ribbon and add the "PyQt5" folder.
12. Within the "Uninstallation" tab, click the checkbox next to "Include Uninstaller".
13. On the left side, under "Dialogs", click "Finish" and click the checkbox next to "Run Application". Edit the text box next to "Run Application" to say '<InstallPath>\RCGen.exe'.
14. On the left side, under "System", click "Shortcuts". Feel free to Add a Desktop and Start Menu shortcut. The only difference in these steps is whether you click "Startmenu" or "Desktop" under "Destination".\
&nbsp;&nbsp;&nbsp;&nbsp;a. Type 'RCGen' under "Shortcut Name".\
&nbsp;&nbsp;&nbsp;&nbsp;b. Type '<InstallPath>\RCGen' under "Target File".\
&nbsp;&nbsp;&nbsp;&nbsp;c. Type '<InstallPath>\WindowsIcon.ico' under "Icon File".
15. On the left side, under "Build", click "Build".
16. To the right of "Setup File" and to the right of the blank text box, click the ellipsis and designate the name of your Installer along with the location you want it to be saved.
17. Click the ellipsis to the right of "Setup Icon" and select "WindowIcon.ico" (within ~/RCGen-main/dist/RCGen). Do the same for the Uninstaller Icon.
18. Enjoy your RCGen installer.

# Limitations

- Currently, RCGen is tailored for instructors teaching Lifesaving Society courses ranging from Parent & Tot 1 to Preschool 5.

- RCGen runs on Windows and Mac. Though, I will "soon" begin work on a website as I am aware that the average person does not know how to even install third-party software anymore.. If you would like a Linux build, please ask.

- There are a few instances of the wrong pronouns being used and a number of instances in which run-on sentences are used. The latter issue typically happens when optional feedback is added... This will be fixed after a bit of beta testing is done.
