from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget

class Mywebbroswer():
    def __init__(self):

        self.window=QWidget()
        self.window.setWindowTitle("Soumya Web Broswer")

        self.layout=QVBoxLayout()
        self.horizontal=QHBoxLayout()

        self.url_bar=QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn=QPushButton("go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn=QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn=QPushButton(">")
        self.forward_btn.setMaximumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.broswer=QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.broswer.back)
        self.forward_btn.clicked.connect(self.broswer.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.broswer)

        self.broswer.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()
          
    def navigate(self, url):
        if not url.startswith("http"):
            url="http://" +url
            self.url_bar.setText(url)
        self.broswer.setUrl(QUrl(url))

app=QApplication([])
window=Mywebbroswer()
app.exec_()
