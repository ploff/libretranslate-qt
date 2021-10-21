import sys
import requests
import json
from PyQt5 import QtWidgets, uic

url = 'https://translate.mentality.rip/translate'
cu = requests.get(url)

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'actionButton')
        self.button.clicked.connect(self.translationAction)
        self.show()

        if cu:
            self.serverStat.setText('OK!')
        else:
            self.serverStat.setText('NOT OK!')

    def translationAction(self, text):
        req = requests.post(url, data = json.dumps({"q": self.InputField.toPlainText(), "source": "en", "target": "ru"}), headers={"Content-Type": "application/json"})
        sts = req.status_code
        data = req.json()
        self.OutputField.setText(data["translatedText"])
        
app = QtWidgets.QApplication([])
application = Ui()
application.show()
sys.exit(app.exec())
