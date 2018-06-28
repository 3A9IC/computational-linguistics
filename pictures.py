from PIL import Image
import numpy, os, requests, re
from io import BytesIO

BLOCK_SIZE = 20
BLOCK_SIZE2 = 30
TRESHOLD = 50
def make_http_mail(img):
	pic='https:'
	result = re.search('img src=\"(.*)" a', img)
	try:
		pic +=result.group(1)
	except:
		try:
			result = re.search('img src=\"(.*)" data-lsrc', img)
			pic +=result.group(1)
		except:
			return False
	return pic
def make_http_opentests(question):
	pic = "http://www.opentests.ru"
	result = re.search('img src="(.*)" b', question)
	pic+=result.group(1)
	return pic
def get_to_small(pic):
	response = requests.get(pic)
	img = Image.open(BytesIO(response.content))
	img = img.convert("RGB")
	small = img.resize((BLOCK_SIZE, BLOCK_SIZE2), Image.BILINEAR)
	data = numpy.array([sum(list(x)) for x in small.getdata()])
	del img, small
	return data
def compare(data1, data2):
	if (sum(1 for x in data1 - data2 if abs(x) > TRESHOLD)) < 200:
		return True
	else:
		return False
