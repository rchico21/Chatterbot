#import logging
#logging.basicConfig(level=logging.INFO)
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot(
    "Terminator",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
	database_uri = "mysql+mysqldb://rchico:1234@localhost/chatterbot",
	#database='chatterbot1',
	#response_selection_method="get_most_frequent_response",
    logic_adapters=[
		{
				"import_path": "chatterbot.logic.BestMatch",
				#"chatterbot.logic.MathematicalEvaluation"
        #"chatterbot.logic.TimeLogicAdapter",
				"statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
				"response_selection_method": "chatterbot.response_selection.get_most_frequent_response",
		}
	],
	filters=["chatterbot.filters.RepetitiveResponseFilter"],
	input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)

bot.set_trainer(ListTrainer)

bot.train([
	#"C:\Users\roich\Desktop\tutorial\myfile.json",
	"How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome."
	#"chatterbot.corpus.english"
])




print("Type something to begin...")

while True:
    try:
			print("You: "),
			bot_input = bot.get_response(None)


    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break