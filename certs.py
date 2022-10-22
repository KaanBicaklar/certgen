from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont 
 
font = ImageFont.truetype('Arial.ttf', 85) 
left=0 
dosya = open("userlist.txt","r") 
for satir in dosya: 
   location=int(len(satir)/2) 
   img = Image.open('../clearcert.png') 
   width, height = img.size 
   draw = ImageDraw.Draw(img) 
   widthloc=(width / 2)-location
   draw.text((widthloc, 900), satir, font=font, align="center" ,anchor="mm", fill =(0, 0, 0)) 
   img.show() 
   dosya_adi="k-"+satir+".png" 
   img.save(dosya_adi)
