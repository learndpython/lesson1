answers = {
	"привет": "Привет!",
	"как дела": "Отлично, а у тебя?",
	"пока": "Ещё увидимся!"
}


def get_answer(questions, answers):
	return answers.get(questions)


def ask_user(answers):
	while True:
		user_input = input("Скажи что-нибудь: ")
		answer = get_answers(user_input, answers)
		print(answer)

		if user_input == 'пока':
			break

if __name__ == "__main__":
	ask_user(answers)

		