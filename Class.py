from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry('600x250')
window.title('Hausa Dictionary')

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

yoruba_dictionary = {

"God":'Oluwa',

"Rest":'Simi',

"Enjoyment":'igbadun',

"Obirin":'woman',

"woman":'Obirin',

"Come":'Wa',

"Child":'Omo',

"Man":'Okurin',

"Cap":'Fila',

"House":'Ile',

"Beans":'Ewa',

"Friend":'Ore',

"Festival":'Odun',

"Crown":'Ade',

"Clock":'Ago',

}
