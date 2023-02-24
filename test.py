import folium, io, sys, json
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

"""
Folium in PyQt5
"""


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Z...PA')
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)

        # layout = QVBoxLayout()
        # self.setLayout(layout)

        pagelayout = QHBoxLayout()
        self.setLayout(pagelayout)

        setings_layout = QVBoxLayout()
        map_layout = QVBoxLayout()


        # self.setLayout(setings_layout)
        # self.setLayout(map_layout)


        pagelayout.addLayout(setings_layout)
        pagelayout.addLayout(map_layout)

        # LABEL 1

        label1 = QLabel("Введите номер машины")
        self.LineEdit1 = QLineEdit()
        setings_layout.addWidget(label1)
        setings_layout.addWidget(self.LineEdit1)

        # LABEL 2

        label2 = QLabel("Введите координаты (через пробел)")
        self.LineEdit2 = QLineEdit()
        setings_layout.addWidget(label2)
        setings_layout.addWidget(self.LineEdit2)

        # LABEL 3

        label3 = QLabel("Введите почту для оповещения")
        self.LineEdit3 = QLineEdit()
        setings_layout.addWidget(label3)
        setings_layout.addWidget(self.LineEdit3)

        # BUTTON 1

        btn = QPushButton("Показать результат")
        btn.clicked.connect(self.on_click)
        setings_layout.addWidget(btn)

        # LABEL 3

        self.label4 = QLabel("")
        setings_layout.addWidget(self.label4)




        coordinate = (52.2978, 104.296)
        m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=12,
            location=coordinate
        )
        # Markers
        folium.Marker(location=[52.25102272646012, 104.40029507901323], popup="В824ТУ, 52.25102272646012 104.40029507901323", icon=folium.Icon(color='gray')).add_to(m)
        folium.Marker(location=[52.27334456734613, 104.31116193826796], popup="Х158МУ, 52.27334456734613 104.31116193826796", icon=folium.Icon(color='gray')).add_to(m)
        folium.Marker(location=[52.28578920225783, 104.39101093249656], popup="Н639ОН, 52.28578920225783 104.39101093249656", icon=folium.Icon(color='gray')).add_to(m)
        folium.Marker(location=[52.31240620221297, 104.31152609456728], popup="М654ВМ, 52.31240620221297 104.31152609456728", icon=folium.Icon(color='gray')).add_to(m)
        folium.Marker(location=[52.29192480346046, 104.24960326596431], popup="К718ХТ, 52.29192480346046 104.24960326596431", icon=folium.Icon(color='gray')).add_to(m)
        folium.Marker(location=[52.23807065463703, 104.28061615247321], popup="В218УТ, 52.23807065463703 104.28061615247321", icon=folium.Icon(color='gray')).add_to(m)

        # Области
        world = 'world.json'
        folium.GeoJson(world,name="madhyapradesh").add_to(m)

        cars = ['В824ТУ','Х158МУ','Н639ОН','М654ВМ','К718ХТ','В218УТ']



        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        map_layout.addWidget(webView)

    def on_click(self):
        # self.label4.setText(self.LineEdit1.text())
        if self.LineEdit1.text() == "В824ТУ":
            self.label4.setText("Статус: данные отправлены \n Событие 1")
        elif self.LineEdit1.text() == "Х158МУ":
            self.label4.setText("Статус: данные отправлены \n Событие 2")
        elif self.LineEdit1.text() == "Н639ОН":
            self.label4.setText("Статус: данные отправлены \n Событие 3")
        elif self.LineEdit1.text() == "М654ВМ":
            self.label4.setText("Статус: данные отправлены \n Событие 4")
        elif self.LineEdit1.text() == "К718ХТ":
            self.label4.setText("Статус: данные отправлены \n Событие 5")
        else:
            self.label4.setText("Машина не найдена!")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')