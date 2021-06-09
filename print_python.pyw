import win32print
import win32ui
from PIL import Image, ImageWin
import sys

#print ("The script has the name %s" % (sys.argv[0])

PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111

printer_name = win32print.GetDefaultPrinter ()
file_name = sys.argv[1]
file_name=file_name.replace('file:///', "",1)

hDC = win32ui.CreateDC ()
hDC.CreatePrinterDC (printer_name)
printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)

bmp = Image.open (file_name)
if bmp.size[0] < bmp.size[1]:
  bmp = bmp.rotate (90)

hDC.StartDoc (file_name)
hDC.StartPage ()

dib = ImageWin.Dib (bmp)
dib.draw (hDC.GetHandleOutput (), (0,0,printer_size[0],printer_size[1]))

hDC.EndPage ()
hDC.EndDoc ()
hDC.DeleteDC ()