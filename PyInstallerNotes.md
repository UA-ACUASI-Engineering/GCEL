# For .exe file using pyinstaller
https://kivy.org/doc/stable/guide/packaging-windows.html#packaging-a-simple-app

PyInstaller --name GCEL main.py

PyInstaller GCEL.spec

PyInstaller --onefile --name GCEL_OneFile main.py

To package to exe run:
pyinstaller GCEL_OneFile.spec

# For android APK using buildozer
https://kivy.org/doc/stable/guide/packaging-android.html
https://github.com/kivy/buildozer

first init command
buildozer init
edit the buildozer.spec, then
buildozer android debug deploy run