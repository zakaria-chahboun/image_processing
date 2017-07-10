from PIL import Image

# main
def main():
	try:
		# ---- Choose image ----
		img = Image.open('images/avocado.jpg');
		

		# ---- Informations ----
		print(img.format) # JPEG ,PNG ..
		print(img.mode) # RGB ...
		print(img.size) # tuple : (x,y)


		# ---- Resize ----
		mysize = (800,600) # 800px x 600px
		img.thumbnail(mysize) # resize
		img.save('images/test_resize.jpg') # you can changing the format like(png)

		
		# ---- Cut (Crop) ----
		box = (100, 100, 500, 500) # (left, upper, right, lower) | rectangle : (x, y, w+x, h+y)
		tmp = img.crop(box) # return image
		tmp.save('images/test1_crop.jpg')


		# ---- Rotate (transpose) ----
		tmp = img.transpose(Image.ROTATE_180) # return image
		tmp.save('images/test2_rotate_180.jpg')


		# ---- Revese color ----
		pix = img.load() # return pixels : [x,y]
		H,W = img.size # H: height, W: width

		for x in range(0,H):
			for y in range(0,W):
				color = pix[x,y] # reurn RGB tuple : (red,green,blue)
				neagtive = (255-color[0],255-color[1],255-color[2])
				pix[x,y] = neagtive

		img.save('images/test3_reverse_color.jpg')


		# ---- Change Color ----
		img2 = Image.open('images/gnome_logo.png');
		pix2 = img2.load() # return pixels : [x,y]
		H,W = img2.size # H: height, W: width

		for x in range(0,H):
			for y in range(0,W):
				color = pix2[x,y]
				if color != (0,0,0,0): # Black color
					pix2[x,y] = (255,0,0) # Red color
		img2.save('images/test4_change_color.png')
		

		# ---- Lighting ----
		img = Image.open('images/avocado.jpg');
		out = img.point(lambda i: i * 1.4) # multiply each pixel by 1.4
		out.save('images/test5_ligthing.jpg')



		# ---- Generate HTML Image ----
		# img2 = Image.open('images/gnome_logo.png');
		# pix2 = img2.load() # return pixels : [x,y]
		# H,W = img2.size # H: height, W: width

		# myfile = open('images/test5_html_image.html','w')
		# HTML = '<!DOCTYPE html><html>'
		# HTML +=	'<head><meta charset="utf-8"><title>Zaki Draw</title></head>'
		# HTML += '<body>'
		
		# Draw = 'z'
		# myfile.write(HTML) # write in html file

		# for x in range(0,H):
		# 	HTML += '<br>'
		# 	for y in range(0,W):
		# 		color = pix2[x,y] # reurn RGB color
		# 		style = 'style="color:rgb{};"'.format(color) # (style) attribute in HTML
		# 		elem = '<span '+style+'>'+Draw+'</span>' # (span) element in HTML
		# 		HTML += elem

		# HTML += '</body></html>'
		# myfile.write(HTML)


	except Exception as e:
		print(e)


# Start
if __name__ == '__main__':
		main()


"""
Overview ::
	The Python Imaging Library adds
		image processing capabilities to your Python interpreter.
			for more : https://pillow.readthedocs.io/en/4.2.x/handbook/overview.html


for more details and examples : http://www.effbot.org/imagingbook/image.htm
-----------------------
zakaria chahboun | 2017
twitter : @zaki_chahboun
-----------------------
"""