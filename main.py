from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(canvas_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(pady=50, padx=50)

canvas = Canvas(width= 300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=200, fill="white", font=("Arial", 20, "bold"))
canvas.grid(row=0, column=0)

kanye_button_img = PhotoImage(file="kanye.png")
button = Button(image=kanye_button_img, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()