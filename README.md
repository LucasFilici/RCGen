## RCGen
RCGen is a piece of Free/Libre and Open Source Software that generates swimming report cards.

## How To Install on MacOS
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
14. Close the terminal and anything else. You're good now. Enjoy the software.

## How To Install on PC
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
10. You're good now. Enjoy the software.

## Packaging Instructions [For advanced users who wish to have complete control over their installation.]
  ### MacOS [For advanced users who wish to have complete control over their installation.]
  - https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/
    1.Download the source code and install pyinstaller:
      `pip3 install PyInstaller`
    2. Run the following command within the "RCGen-main" folder:
      `pyinstaller --windowed --icon="WindowIcon.icns" RCGen.py`
    3. [I'll get to this in a second.]
  ### Windows
  - https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/
    1. Download the source code and install pyinstaller:
       `pip3 install PyInstaller`
    2. Run the following command within the "RCGen-main" folder:
       `pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import PyQt5 --noconsole --add-data "WindowIcon.ico;." RCGen.py`
       At this point, you will have a functional .exe file within the "dist" folder.
       If you wish to create an installer, the solution I used was InstallForge.
    3. Install InstallForge: https://installforge.net/download/
    4. Within InstallForge, on the left side, click "General" under "General"
    5. Type "RCGen" to the right of "Product Name".
    6. Type "v0.1.0" to the right of "Product Version".
    7. Type "Lucas Filici" to the right of "Company Name".
    8. On the left side, click on "Files" under "Setup".
    9. Click on "Add Files" on the top ribbon and add all files within the "RCGen" folder (within ~/RCGen-main/dist/).
    10. Click on "Add Folders" on the top ribbon and add the "PyQt5" folder.
    11. Within the "Uninstallation" tab, click the checkbox next to "Include Uninstaller".
    12. On the left side, under "Dialogs", click "Finish" and click the checkbox next to "Run Application". Edit the text box next to "Run Application" to say '<InstallPath>\RCGen.exe'.
    13. On the left side, under "System", click "Shortcuts". Feel free to Add a Desktop and Start Menu shortcut. The only difference in these steps is whether you click "Startmenu" or "Desktop" under "Destination".
       a. Type 'RCGen' under "Shortcut Name".
       b. Type '<InstallPath>\RCGen' under "Target File".
       c. Type '<InstallPath>\WindowsIcon.ico' under "Icon File".
    14. On the left side, under "Build", click "Build".
    15. To the right of "Setup File" and to the right of the blank text box, click the ellipsis and designate the name of your Installer along with the location you want it to be saved.
    16. Click the ellipsis to the right of "Setup Icon" and select "WindowIcon.ico" (within ~/RCGen-main/dist/RCGen). Do the same for the Uninstaller Icon.
    17. Enjoy your RCGen installer.

## Limitations

- Currently, RCGen is tailored for instructors teaching Lifesaving Society courses ranging from Parent & Tot 1 to Preschool 5.

- RCGen runs on Windows and Mac. There may possibly be a website as well. If you would like a Linux build, please ask.

- There are a few instances of the wrong pronouns being used and a number of instances in which run-on sentences are used. The latter issue typically happens when optional feedback is added... This will be fixed after a bit of beta testing is done.
