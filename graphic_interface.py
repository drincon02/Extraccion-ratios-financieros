from tkinter import *
from finacial_ratios_download import *
from tkinter import messagebox
import webbrowser

hyperlink1 = "https://financialmodelingprep.com/"
hyperlink2 = "https://financialmodelingprep.com/register"
root = Tk()
root.title("Descarga de ratios financieros")
root.iconbitmap("DR (1).ico")

def descarga_ratios():
    api_key = apikey.get()
    tickets = ticket.get()

    if "," in tickets:
        tickets = tickets.split(",")

    if single_period.get() == 1:
        try:
            dataf = financialratios(tickets, True, api_key)
            transform(dataf, tickets)
            messagebox.showinfo("Exito", "Los ratios financieros han sido descargados con exito")
            if peeranalysis.get() == 1:
                peerfinancialratios(tickets, api_key)
        except:
            messagebox.showerror("Algo salio mal",
                                 "Algo salio mal verifica que tu API key y tus tickers sean correctos")

    else:
        try:
            dataf = financialratios(tickets, False, api_key)
            transform(dataf, tickets)
            messagebox.showinfo("Exito", "Los ratios financieros han sido descargados con exito")
            if peeranalysis.get() == 1:
                peerfinancialratios(tickets, api_key)
        except:
            messagebox.showerror("Algo salio mal",
                                 "Algo salio mal verifica que tu API key y tus tickers sean correctos")


def informacion_links():
    messagebox.showinfo("Informacion", f"Este es un programa hecho en python que se conecta a la API"
                                                      f" de la pagina {hyperlink1} y extrae ratios financieros de las empresas"
                                                      "que se deseen. \n \n Para obtener tu Api Key dirigite al "
                                                      f"siguiente link {hyperlink2} y registrate para que te den una Api Key "
                                                      "gratis.")

def webpage():
    webbrowser.open('https://rincondiego.com/')

ticket = Entry(root, width=40)
apikey = Entry(root, width=40)
ticket.grid(row=0, column=2)
apikey.grid(row=2, column=2)

ticket_label = Label(root, text="Ticker de la o las empresas")
apikey_label = Label(root, text="Api Key")
ticket_label.grid(row=0, column=1)
apikey_label.grid(row=2, column=1)

single_period = IntVar()
c = Checkbutton(root, text="Descargar solo los ratios del ultimo periodo", var=single_period)
c.grid(row=4, column=1)

peeranalysis = IntVar()
ch = Checkbutton(root, text="Descargar comparativo de varios tickers", var=peeranalysis)
ch.grid(row=5, column=1)


download_button = Button(root, text="Descargar Ratios Financieros", command=descarga_ratios)
download_button.grid(row=7, column=1, columnspan=2)

info_button = Button(root, text="Mas informacion", command=informacion_links)
info_button.grid(row=9, column=2)

contacto_button = Button(root, text="Contactame", command=webpage)
contacto_button.grid(row=9, column=1)

root.mainloop()
