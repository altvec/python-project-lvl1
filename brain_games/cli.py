import prompt


def run():
    username = prompt.string('May I have your name? ')
    greeting = 'Hello, {}!'.format(username)
    print(greeting)
