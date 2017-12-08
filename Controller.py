import Main
import Kahoot_Bot
import GUI
import getpass

kahooter = Main.KahootScraper()
bot = Kahoot_Bot.Bot()
gui = GUI.Gui()

game_id = raw_input("Game_id: ")


print("Confirming Board ID: " + game_id)

board_id = raw_input("Board_Id: ")


print("Confirming Board ID: " + board_id)

game_answers = kahooter.getAnswers(game_id)

print(game_answers)

questions_and_answers = kahooter.getQuestions(game_id)
times = kahooter.getTimes(game_id)

bot.joinGame("Jeff", board_id)
bot.playGame(game_answers, times)

gui.createScroll(questions_and_answers)


