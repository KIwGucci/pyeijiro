# coding UTF-8
import requests
from bs4 import BeautifulSoup
import re
import sys
from PyQt5.QtWidgets import (QWidget, QApplication)
import uiEnglishdictionary


# 末尾の除去する文字リスト
striplist = ("?", ".", "!", ' ')


def translatew(word):
    """英辞郎検索"""
    base_url = "http://eow.alc.co.jp/search"
    query = {}
    query["q"] = word
    ret = requests.get(base_url, params=query)
    soup = BeautifulSoup(ret.content, "lxml")
    # print(soup)
    outext = []
    result = ""
    try:
        for l in soup.findAll('div', {"id": "resultsList"})[0]:
            try:
                outext.append(l.text)
            except AttributeError:
                pass
    except IndexError:
        return False

    for i in outext[1:]:
        # print(i)
        i = i.replace("<!--", "")
        i = i.replace("// -->", "")
        stlist = i.split("result_list();")
        for j in stlist:
            j = j.strip()
            result += j
    result = re.sub('◆【|【', '\n【', result)
    result = re.sub("\n\n\n", '\n', result)
    result = re.sub('｛.*?｝', '', result)
    # result = re.sub(r"・", r' ◇ ', result)
    try:
        preresult = result.split('#div-gpt-ad-')[0]
        afresult = result.split(r'});')[1]
        result = preresult.strip()+'\n'+afresult.strip()
    except IndexError:
        pass
    return result


def translate_enen(word):
    """Oxford英英検索"""
    outext = ""
    headers = {
        'User-Agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"}
    base_url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}?"
    query = {}
    query["q"] = word
    ret = requests.get(base_url, headers=headers, params=query)
    soup = BeautifulSoup(ret.content, "lxml")
    idioms = soup.find_all("span", {"id": re.compile(
        f'^{word}_'), 'class': re.compile("idm|def")})
    for idi in idioms:
        chtext = str(idi)
        if "Add to" in chtext:
            pass
        elif "def" in chtext:
            outext += "* " + idi.get_text() + "\n"
        else:
            outext += "[ idiom ]\n" + idi.get_text() + "\n"
    return outext


class MainWindow(QWidget):
    """Guiを構築"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uiEnglishdictionary.Ui_Dialog()
        self.ui.setupUi(self)
        mainLayout = self.ui.verticalLayout
        self.setLayout(mainLayout)
        # Action Eijiro
        self.ui.lineEdit_en.returnPressed.connect(self.dotrans)
        self.ui.pushButton_cl.clicked.connect(self.doclear)

    def dotrans(self):
        word = self.ui.lineEdit_en.text().lower()
        if word == "":
            jaword = None
            enenword = None
        else:
            jaword = translatew(word)
            enenword = translate_enen(word)
        if jaword:
            self.ui.textEdit_ja.setText(jaword)
        else:
            self.ui.textEdit_ja.clear()
        if enenword:
            self.ui.textEdit_dic.setText(enenword)
        else:
            self.ui.textEdit_dic.clear()

    def doclear(self):
        self.ui.lineEdit_en.clear()
        self.ui.textEdit_ja.clear()
        self.ui.textEdit_dic.clear()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
