import random
from tkinter import *

BACKGROUND_COLOR = "#f9ead3"
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
play_pick = 0
total_candies = 11


def game():
    canvas = Canvas(width=800, height=526)

    def print_num():
        print_text = canvas.create_text(400, 500, text="how many candies do you want to take?",
                                        font=("poppins", 10, "bold"))

    candy1 = PhotoImage(file="pics/candy1.png")
    candy_one = candy1.subsample(2, 2)
    candy2 = PhotoImage(file="pics/candy2.png")
    candy_two = candy2.subsample(2, 2)
    candy3 = PhotoImage(file="pics/candy3.png")
    candy_three = candy3.subsample(2, 2)
    candy4 = PhotoImage(file="pics/candy4.png")
    candy_four = candy4.subsample(2, 2)
    candy5 = PhotoImage(file="pics/candy5.png")
    candy_five = candy5.subsample(2, 2)
    candy6 = PhotoImage(file="pics/candy6.png")
    candy_six = candy6.subsample(2, 2)
    candy7 = PhotoImage(file="pics/candy7.png")
    candy_seven = candy7.subsample(2, 2)
    candy8 = PhotoImage(file="pics/candy8.png")
    candy_eight = candy8.subsample(2, 2)
    candy9 = PhotoImage(file="pics/candy9.png")
    candy_nine = candy9.subsample(2, 2)
    candy10 = PhotoImage(file="pics/candy10.png")
    candy_ten = candy10.subsample(2, 2)
    candy11 = PhotoImage(file="pics/candy11.png")
    candy_eleven = candy11.subsample(2, 2)
    candies = [candy_one, candy_two, candy_three, candy_four, candy_six, candy_seven, candy_eight,
               candy_nine, candy_ten, candy_eleven]
    widths = [50, 100, 80, 250, 300, 350, 400, 450, 600, 680, 580, 150, 700, 750]
    heights = [90, 110, 140, 200, 240, 280, 320, 360, 400, 440, 480]

    def put_image():
        candy_len = len(candies)
        while candy_len > 0:
            canvas.create_image((random.choice(widths)), (random.choice(heights)), image=candies[(candy_len - 1)])
            candy_len -=1
    def pick_num_one():
        global play_pick
        play_pick = 1
        global total_candies
        total_candies -= 1
        del candies[play_pick]
        return total_candies

    def pick_num_two():
        global play_pick
        play_pick = 2
        global total_candies
        total_candies -= 2
        return total_candies

    put_image()
    card_background = canvas.create_image(400, 263)
    card_title = canvas.create_text(400, 20, text="CANDY GRAB GAME", font=("poppins", 30, "bold"))
    canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    print_num()
    one_button = Button()
    one_button.grid(row=1, column=0, sticky='EWNS')
    one_button.config(background=BACKGROUND_COLOR, text="1", font=("poppins", 10, "bold"), command=pick_num_one)
    two_button = Button()
    two_button.grid(row=1, column=1, sticky='EWNS')
    two_button.config(background=BACKGROUND_COLOR, text="2", font=("poppins", 10, "bold"), command=pick_num_two)

    window.mainloop()


game()
