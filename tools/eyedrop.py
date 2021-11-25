import cv2, numpy
from sty import *

class Eyedrop(object):
	def __init__(self, ui):
		self.ui = ui
		self.color_selected = numpy.zeros((150,150,3), numpy.uint8)
	
	# // Get the colors hex code
	def get_hex(self, r,g,b):
		return "#{:02x}{:02x}{:02x}".format(r,g,b)

	# // Get the colors "Android color" code
	def get_android_hex(self, hex_code):
		hex_code = hex_code.upper().strip('#')
		return f"0xFF{hex_code}"

	# // Display the color values to the screen
	def set_text(self, R, G, B):
		hex_color = self.get_hex(R, G, B)
		text = f"Selected Color:\n\nRGB: ({R},{G},{B})\n\nAndroid Hex: {self.get_android_hex(hex_color)}\n\nStandard Hex: {hex_color}"
		self.ui.selected_color.setPlainText(text)
		self.ui.color_display.setStyleSheet(f"background-color:rgb({R},{G},{B})")


	# // Show the newly captured image to the screen
	def read(self, image):
		cv2.namedWindow('image')
		self.image = cv2.imread(image)
		cv2.setMouseCallback('image', self.show_color)

		while (1):
			cv2.imshow('image', self.image)
			if cv2.waitKey(1) & 0xFF == 27:
				cv2.destroyAllWindows()
	

	# // Print out the values for the selected color
	def show_color(self, event, x, y, flags, param):
		B=self.image[y,x][0]
		G=self.image[y,x][1]
		R=self.image[y,x][2]
  
		if event == cv2.EVENT_LBUTTONDOWN:
			self.color_selected [:] = (B,G,R)
			self.set_text(R, G, B)
