import logging
import requests, json, utils, pictures
import numpy
logger = logging.getLogger('mail_ru_parser')

	
def get_answers(question, need_figure=False):
	try:
		clear_question = utils.clear_html_tags(question)
		r = requests.get('https://go.mail.ru/answer_json?q=' + clear_question, timeout=20)
		# logger.info('request time: %s' % (r.elapsed.total_seconds()))
		j = json.loads(r.content.decode(r.encoding))
		answers = []
		catname = ['Еда, Кулинария', 'Знакомства, Любовь, Отношения', 'Программное обеспечение', 'Вокруг света', 'Юмор', 'Кино, Театр', 'Религия, Вера', 'Политика',
		'Новый Год', 'Строительство и Ремонт', 'Мода', 'Компьютеры, Связь', 'Свадьба, Венчание, Брак', 'Прочие социальные темы', 'Другие языки и технологии', 'Техника, темы, жанры съемки',
		'Железо', 'Музыка', 'Прочее о здоровье и красоте', 'Прочие юридические вопросы', 'Прочие взаимоотношения', 'Семья, Дом, Дети', 'Литература', 'Прочее кулинарное', 'Выбор, покупка аппаратуры',
		'Гороскопы', 'Жилищное право']
		for result in j['results']:
			if result['catname'] not in catname:
				if need_figure and 'qstcomment' in result:
					fine = True
					url1 = pictures.make_http_opentests(question)
					url2 = pictures.make_http_mail(result['qstcomment'])
					if url2 == False:
						continue
					data1 = pictures.get_to_small(url1)
					data2 = pictures.get_to_small(url2)
					if pictures.compare(data1, data2) == False:
						continue
				if 'banswer' in result:
					answers.append(result['banswer'])
				if 'answer' in result:
					answers.append(result['answer'])
		return answers
	except:
		logger.warning('Houston, We\'ve Got a Problem With Mail.ru')
		return []
	