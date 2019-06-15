import win32gui,win32con,win32clipboard

def getPathAndList():
    with open('垃圾话.txt','r') as file:
        path = file.readline()
        fivelist = []
        five = file.readline()
        while five:
            fivelist.append(five)
            five = file.readline()
        return path,fivelist

def sendTo(handle):
	win32gui.SendMessage(handle,258, 22, 2080193)
	win32gui.SendMessage(handle,770,0,0)
	win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
	win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def setClip(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()

def clearPath(path):
    return path.strip('PATH=').strip('\n')


def main():
    path, fivelist = getPathAndList()
    windowname = clearPath(path)
    handle = win32gui.FindWindow(None,windowname)
    for five in fivelist:
        if five:
            print(five)
            setClip(five)
            sendTo(handle)

if __name__ == '__main__':
    main()