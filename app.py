import logging, os
import solver, iq_test


def run(qid):
	try:
		qc = iq_test.init_session(qid)
		ticket_id = iq_test.get_ticket(qid)

		if not os.path.exists('logs'):
			os.makedirs('logs')
		logging.basicConfig(format=u'[%(levelname)s] [%(name)s] [%(asctime)s]  %(message)s',
							filename='logs/%s.log' % ticket_id, level=logging.INFO)

		logging.info('ticket_id: %s' % ticket_id)
		for i in range(qc):
			logging.info('question #%i' % (i + 1))
			print(i + 1)
			q_obj = iq_test.get_question(ticket_id)
			question = q_obj['questionText']
			logging.info('question: %s' % question)
			answer = solver.get_possible_answer(question)
			logging.info('answer: %s' % answer)
			iq_test.save_question(answer, ticket_id, q_obj['questionId'])

		lnk = iq_test.get_result_link(ticket_id)
		logging.info('result: %s' % lnk)
		print('result: %s' % lnk)
	except Exception as e:
		print('Some problems')
		raise e


run(36)
