from tkinter import *
import matplotlib.pyplot as pyp
import networkx as netx
import matplotlib
import matplotlib.figure
import matplotlib.backends.backend_tkagg



class Lab3:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x600')
        self.root.config(bg="light blue")

        self.info_about = Label(self.root, text=f"Студент: Скомороха Олег\n"
                                  f"Номер залікової книги: 2527\n"
                                  f"Мій варіант: 2529 mod 10+1 = {2527 % 10 + 1}", bg="#FFA07A", width=29,
                             relief=GROOVE)
        self.my_info.place(x=10, y=10)
        self.info_rebr = Label(self.root, text="Введыть вершини, між якими\nбуде ребро (через пробіл):", width=29)
        self.info_rebr.place(x=10, y=65)

        self.read_text = Entry(self.root, width=34)
        self.read_text.place(x=10, y=105)
        self.input_info = Button(self.root, text="Задати ребро", command=self.read_new_text, width=25)
        self.input_info.place(x=23, y=130)

        self.space = Label(self.root, text=f"{'-' * 40}", bg="light blue")
        self.space.place(x=10, y=157)
        self.save_info = Button(self.root, text="Зберегти список ребер", width=25)
        self.save_info.place(x=23, y=180)
        self.read_info = Button(self.root, text="Зчитати дані з файлу", width=25)
        self.read_info.place(x=23, y=210)

        self.info_list = Label(self.root, text="Список вже існуючих ребер", bg="light pink", relief=GROOVE)
        self.info_list.place(x=250, y=10)
        self.read_list = Listbox(self.root, width=20)
        self.read_list.place(x=270, y=31)

        self.info_text1 = Label(self.root, text='Перша вершина', relief=GROOVE, bg="light pink", fg="black", width=26)
        self.info_text1.place(x=510, y=10)
        self.see_info_get = Entry(self.root, width=30)
        self.see_info_get.insert(END, '---')
        self.see_info_get.place(x=510, y=33)
        self.info_text2 = Label(self.root, text="Друга вершина", relief=GROOVE, bg="light pink", fg="black", width=26)
        self.info_text2.place(x=510, y=56)
        self.see_info_get2 = Entry(self.root, width=30)
        self.see_info_get2.insert(END, '---')
        self.see_info_get2.place(x=510, y=79)
        self.but_road = Button(self.root, text='Прокласти найкорочший шлях', command=self.wayes_graph, width=25)
        self.but_road.place(x=510, y=100)

        self.grahper = None
        self.start_yes = None

        self.figure = pyp.figure(figsize=(5, 3))
        self.place = self.figure.add_subplot(111)

        self.wayes = None
        self.wayes_edges = None

        self.canva = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.figure, master=self.root)
        self.canva.draw()
        self.canva.get_tk_widget().place(x=10, y=250, width=880)
        self.draw()

    def levit(self, window):
        self.ariana = [[int(window.table_entries[i][j].get()) for i in range(self.read_text)] for j in
                       range(self.read_text)]
        self.Grapher = nx.Grapher()
        for i in range(self.read_text):
            self.Grapher.add_node("n" + str(i))

        for i in range(self.read_text):
            for j in range(self.read_text):
                if self.ariana[i][j] == 0:
                    continue
                if self.ariana[i][j] >= 1:
                    for k in range(self.ariana[i][j]):
                        self.Grapher.add_edges("n" + str(i), "n" + str(j))
                if self.ariana[i][j] == -1:
                    self.Grapher.add_edges("n" + str(j), "n" + str(i))
                else:
                    return

    def read_new_text(self):
        self.read_list.insert(END, self.read_text.get())
        edges = self.read_list.get(0, last=END)
        self.grahper = netx.parse_edgelist(list(edges))
        self.start_yes = netx.spring_layout(self.grahper)
        self.place.cla()
        self.draw()
        self.canva.resize_event()

    def my_window(self):
        self.root.title("ІО-25 Сокольчук Олексій lab3dm")
        self.root.mainloop()


    def draw(self):
        if self.grahper is not None:
            netx.draw(self.grahper, self.start_yes, with_labels=True)
        if self.wayes is not None:
            netx.draw_networkx_nodes(self.grahper, self.start_yes, nodelist=self.wayes, node_color='c')
            netx.draw_networkx_edges(self.grahper, self.start_yes, edgelist=self.wayes_edges, edge_color='m')

    def wayes_graph(self):
        point1 = self.see_info_get.get()
        point2 = self.see_info_get2.get()
        self.wayes = netx.shortest_path(self.grahper, source=point1, target=point2)
        self.wayes_edges = list(zip(self.wayes, self.wayes[1:]))
        self.place.cla()
        self.draw()
        self.canva.resize_event()


if __name__ == '__main__':
    graph = lab3dm()
    graph.my_window()