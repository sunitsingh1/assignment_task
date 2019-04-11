from PIL import Image,ImageDraw,ImageFont

class ImageText():

	def __init__(self,image,draw,font,a,imageText):
		self.image=image
		self.draw=draw
		self.font=font
		self.a=(x,y)
		self.imageText=imageText


	def textImage(self):
		draw.text(self.a,self.imageText,font=self.font)
		image.save('textImage.png')

	def maskImage(self):
			draw.text(self.a,self.imageText,font=self.font)
			size=draw.textsize(self.imageText,font=self.font)
			offset=font.getoffset(self.imageText)
			draw.rectangle((x,y, x+size[0],x+size[1]-10),fill='red')
			#draw.rectangle((200, 200, 200 + size[0] + offset[0], 200 + size[1] + offset[1]),fill='red')

			image.save('masked.png')

if __name__ == '__main__':

	#image=Image.open(input("Enter image path: "))
	image=Image.open('clouds-595x335_1.jpg')
	#image=Image.new('RGBA',(500,500),'blue')
	#print(image.show())
	draw = ImageDraw.Draw(image)
	font=ImageFont.truetype('FrankRuhlLibre-Bold.ttf',size=50)
	(x,y)=(200,200)
	#imageText= "Hello World!"
	imageText= input("Enter Text: ")
	obj=ImageText(image,draw,font,(x,y),imageText)
	obj.textImage()
	obj.maskImage()
