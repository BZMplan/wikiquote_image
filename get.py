import datetime
import pywikibot
import re
from PIL import Image,ImageDraw,ImageFont
from regex import R
from scipy import constants
from zhconv import convert_for_mw
from bottle import route,run,template
from bottle import error

curretn_date_m = datetime.datetime.now().strftime('%m')
current_date_d = datetime.datetime.now().strftime('%d')

if current_date_d.startswith("0"):
    current_date_d = current_date_d[1:]
if curretn_date_m.startswith("0"):
    curretn_date_m = curretn_date_m[1:]
    
str = 'Wikiquote:每日名言'+'/'+curretn_date_m+'月'+current_date_d+'日'
site = pywikibot.Site('zh','wikiquote')
page = pywikibot.Page(site,str)

#显示的文字
context = convert_for_mw(re.sub(r'\[\[(.*?)\|.*?\]\]', r'\1', page.text),'zh-hans')


@route('/wikiquote',medthod='POST')
def wikiquote():
    #return template('<b>{{context}}<b>',context=context)
    return context
@error(404)
def error404(error):
    return 'Nothing here, sorry'
print(context)
run(host='localhost',port=5000)


#current_date = datetime.datetime.now().strftime("%Y-%m-%d")
#file_name = f"output_{current_date}.jpg"

''' generate image
if os.path.exists(file_name):
    print("已生成")
else:
    image = Image.new('RGB',(1920,1080),color=(	255,240,245))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('simsun.ttc', 70, encoding='unic')

    text_width, text_height = draw.textsize(context,font=font) # type: ignore


    text_x = (image.width - text_width) / 2
    text_y = (image.height - text_height) / 2

    draw.text((text_x,text_y),context,fill=(0,0,0),font=font)
    file_name = f"output_{current_date}.jpg"
    image.save(file_name)
'''






 


