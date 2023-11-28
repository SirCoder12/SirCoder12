import os

def cwd(file):
    cwds={".py":r"C:\\Users\\micha\\OneDrive\\Documents\\Programing\\.py",
          ".txt":r"C:\\Users\\micha\\OneDrive\\Documents\\Programing\\.txt",
          ".java":r"C:\\Users\\micha\\OneDrive\\Documents\\Programing\\.java",
          ".html":r"C:\\Users\\micha\\OneDrive\\Documents\\Programing\\.html",
          ".csv":r"C:\\Users\\micha\\OneDrive\\Documents\\Programing\\.csv",
          ".mp3":f"C:\\Users\\micha\\OneDrive\\Documents\\Programing\\{file}",
          "Jarvis":r"C:\\Users\\micha\\OneDrive\\Documents\\Programing\\Jarvis" }
    os.chdir(str(cwds[file]))