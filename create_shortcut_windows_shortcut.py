import os, winshell, win32com.client, Pythoncom

desktop = winshell.desktop()
#desktop = r"path to where you wanna put your .lnk file"
path = os.path.join(desktop, 'File Shortcut Demo.lnk')
target = r"C:\Users\lenovo\Documents\sample2.txt" 
icon = r"C:\Users\lenovo\Documents\sample2.txt"
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()