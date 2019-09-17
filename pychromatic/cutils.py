
import colorsys

class color_utils:
	
	def __init__(self):
		self.a = 1

	def hex_to_rgb(self, hexval):
		hexstr = hexval.strip('#')
		r = int(d[0:2], 16)
		g = int(d[2:4], 16)
		b = int(d[4:7], 16)
		return [r, g, b]

	def rgb_to_hsv(self, rgbval):
		h, s, v = colorsys.rgb_to_hsv(rgbval[0], rgbval[1], rgbval[2])
		return [h, s, v]
		
