"""
Filip Hajduch
RSA Cypher
"""

from PyQt6 import QtCore, QtGui, QtWidgets
import math
import random

"""
Moje funkce
"""


# 0. Vygenerovani klicu
def generateKey():
    n = 0
    phi_n = 0
    e = 0
    d = 0
    p = generate_prime(11, 12)
    q = generate_prime(11, 12)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randint(2, phi_n - 1)
    # overeni nesoudelnosti
    while True:
        e = random.randint(2, phi_n - 1)
        if math.gcd(e, phi_n) == 1:
            break
    d = pow(e, -1, phi_n)

    publicKey = (n, e)
    privateKey = (n, d)
    return publicKey, privateKey


# Kontrola cisla jestli je prvocislo
def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# EN 1. Prevod textu na ASCII
def stringToASCII(text):
    utf8_bytes = text.encode('utf-8')
    print(utf8_bytes)
    ascii_values = [byte for byte in utf8_bytes]
    return ascii_values


# EN 6. Sifrovani
def encrypt(textInt, publicKey):
    n, e = publicKey
    encrypted_text = [pow(char, e, n) for char in textInt]
    return encrypted_text


# DE 1. Desifrovani
def decrypt(encryptedText, privateKey):
    n, d = privateKey
    decrypted_text = [pow(char, d, n) for char in encryptedText]
    return decrypted_text


# Generovani prvocisla
def generate_prime(x, y):
    lower_limit = 10 ** x
    upper_limit = 10 ** y

    while True:
        potential_prime = random.randint(lower_limit, upper_limit)

        if isPrime(potential_prime):
            return potential_prime


def asciiToString(ascii_values):
    utf8_bytes = bytes(ascii_values)
    text = utf8_bytes.decode('utf-8')
    return text


# EN 2. Ascii na BIN
def decimalListToBinary(decimal_list):
    binary_list = [bin(decimal)[2:].zfill(8) for decimal in decimal_list]
    return binary_list


# EN 3. Spojeni BIN cisla / DE 3.
def binaryListToSuperNumber(binary_list):
    super_number = ''.join(binary_list)
    return super_number


# EN 4. Rozdeleni supercisla na bloky po 10
def blockSuperNumber(super_number):
    # Přidej nuly na začátek, aby délka byla násobkem 10
    super_number = '0' * (10 - (len(super_number) % 10)) + super_number
    # Rozděl číslo na bloky po 10 bitech
    blocks = [super_number[i:i + 10] for i in range(0, len(super_number), 10)]
    return blocks


def splitSuperNumberToBinaryList(super_number):
    # Přidej nuly na začátek, aby délka byla násobkem 8
    super_number = '0' * (8 - (len(super_number) % 8)) + super_number
    # Rozděl číslo na binární hodnoty po 8 bitech
    binary_list = [super_number[i:i + 8] for i in range(0, len(super_number), 8)]
    return binary_list


# EN 5. Prevedeni bin listu do decimal
def binaryListToDecimalList(binary_list):
    decimal_list = [int(binary, 2) for binary in binary_list]
    decimal_list = [num for num in decimal_list if num != 0]
    return decimal_list


# DE 2. Prevedeni cisel zpet na bin s pevnou delkou 10 bitu
def decimalListToBinary10(decimal_list):
    binary_list = [bin(decimal)[2:].zfill(10) for decimal in decimal_list]
    return binary_list


"""
GUI 
"""


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 800)
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(-11, -1, 1100, 820))
        self.widget.setStyleSheet("QWidget#widget{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, "
                                  "y2:1, stop:0 rgba(139, 171, 193, 255), stop:1 rgba(147, 211, 160, 255));}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(420, 20, 171, 51))
        self.label.setStyleSheet("font: 600 30pt \"Raleway\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.text_sifrovani = QtWidgets.QTextEdit(parent=self.widget)
        self.text_sifrovani.setGeometry(QtCore.QRect(50, 340, 381, 81))
        self.text_sifrovani.setStyleSheet("QTextEdit{\n"
                                          "background-color:rgb(255, 255, 255);\n"
                                          "font: 18pt \"Raleway\"; background-color: white;\n"
                                          "color: black;\n"
                                          "border-radius: 15px;\n"
                                          "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                          "padding-left:5px;\n"
                                          "padding-top:5px;\n"
                                          "}\n"
                                          "\n"
                                          "QTextEdit:focus{\n"
                                          "border: 2px solid rgb(126, 145, 191);\n"
                                          "\n"
                                          "}\n"
                                          "")
        self.text_sifrovani.setObjectName("text_sifrovani")
        self.encrypt = QtWidgets.QPushButton(parent=self.widget)
        self.encrypt.setGeometry(QtCore.QRect(170, 450, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encrypt.sizePolicy().hasHeightForWidth())
        self.encrypt.setSizePolicy(sizePolicy)
        self.encrypt.setStyleSheet("QPushButton#encrypt{\n"
                                   "background-color:rgba(166, 205, 255,0.5);\n"
                                   "font: 600 25pt \"Raleway\";\n"
                                   "border-radius: 15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#encrypt:hover{\n"
                                   "background-color:rgb(126, 145, 191);\n"
                                   "font: 700 26pt \"Raleway\";\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#encrypt:pressed{\n"
                                   "font: 600 24pt \"Raleway\";\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.encrypt.setObjectName("encrypt")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 510, 311, 41))
        self.label_3.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_3.setObjectName("label_3")
        self.numberTextEncrypt = QtWidgets.QTextEdit(parent=self.widget)
        self.numberTextEncrypt.setGeometry(QtCore.QRect(50, 560, 381, 81))
        self.numberTextEncrypt.setStyleSheet("QTextEdit{\n"
                                             "background-color:rgb(255, 255, 255);\n"
                                             "font: 18pt \"Raleway\"; background-color: white;\n"
                                             "color: black;\n"
                                             "border-radius: 15px;\n"
                                             "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                             "padding-left:5px;\n"
                                             "padding-top:5px;\n"
                                             "}\n"
                                             "\n"
                                             "QTextEdit:focus{\n"
                                             "border: 2px solid rgb(126, 145, 191);\n"
                                             "\n"
                                             "}\n"
                                             "")
        self.numberTextEncrypt.setReadOnly(True)
        self.numberTextEncrypt.setAcceptRichText(False)
        self.numberTextEncrypt.setObjectName("numberTextEncrypt")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(60, 650, 311, 41))
        self.label_4.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_4.setObjectName("label_4")
        self.encryptedText = QtWidgets.QTextEdit(parent=self.widget)
        self.encryptedText.setGeometry(QtCore.QRect(50, 700, 381, 81))
        self.encryptedText.setStyleSheet("QTextEdit{\n"
                                         "background-color:rgb(255, 255, 255);\n"
                                         "font: 18pt \"Raleway\"; background-color: white;\n"
                                         "color: black;\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                         "padding-left:5px;\n"
                                         "padding-top:5px;\n"
                                         "}\n"
                                         "\n"
                                         "QTextEdit:focus{\n"
                                         "border: 2px solid rgb(126, 145, 191);\n"
                                         "\n"
                                         "}\n"
                                         "")
        self.encryptedText.setReadOnly(True)
        self.encryptedText.setObjectName("encryptedText")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(170, 70, 141, 41))
        self.label_5.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(80, 120, 21, 31))
        self.label_6.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(80, 210, 21, 31))
        self.label_7.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.publicKeyN = QtWidgets.QLineEdit(parent=self.widget)
        self.publicKeyN.setGeometry(QtCore.QRect(70, 160, 341, 40))
        self.publicKeyN.setStyleSheet("QLineEdit{\n"
                                      "background-color:rgb(255, 255, 255);\n"
                                      "font: 18pt \"Raleway\"; background-color: white;\n"
                                      "color: black;\n"
                                      "border-radius: 15px;\n"
                                      "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus{\n"
                                      "border: 2px solid rgb(126, 145, 191);\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.publicKeyN.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.publicKeyN.setObjectName("publicKeyN")
        self.publicKeyE = QtWidgets.QLineEdit(parent=self.widget)
        self.publicKeyE.setGeometry(QtCore.QRect(70, 250, 341, 40))
        self.publicKeyE.setStyleSheet("QLineEdit{\n"
                                      "background-color:rgb(255, 255, 255);\n"
                                      "font: 18pt \"Raleway\"; background-color: white;\n"
                                      "color: black;\n"
                                      "border-radius: 15px;\n"
                                      "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus{\n"
                                      "border: 2px solid rgb(126, 145, 191);\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.publicKeyE.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.publicKeyE.setObjectName("publicKeyE")
        self.text_desifrovani = QtWidgets.QTextEdit(parent=self.widget)
        self.text_desifrovani.setGeometry(QtCore.QRect(570, 340, 381, 81))
        self.text_desifrovani.setStyleSheet("QTextEdit{\n"
                                            "background-color:rgb(255, 255, 255);\n"
                                            "font: 18pt \"Raleway\"; background-color: white;\n"
                                            "color: black;\n"
                                            "border-radius: 15px;\n"
                                            "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                            "padding-left:5px;\n"
                                            "padding-top:5px;\n"
                                            "}\n"
                                            "\n"
                                            "QTextEdit:focus{\n"
                                            "border: 2px solid rgb(126, 145, 191);\n"
                                            "\n"
                                            "}\n"
                                            "")
        self.text_desifrovani.setObjectName("text_desifrovani")
        self.label_23 = QtWidgets.QLabel(parent=self.widget)
        self.label_23.setGeometry(QtCore.QRect(580, 650, 311, 41))
        self.label_23.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_23.setObjectName("label_23")
        self.decryptedText = QtWidgets.QTextEdit(parent=self.widget)
        self.decryptedText.setGeometry(QtCore.QRect(570, 700, 381, 81))
        self.decryptedText.setStyleSheet("QTextEdit{\n"
                                         "background-color:rgb(255, 255, 255);\n"
                                         "font: 18pt \"Raleway\"; background-color: white;\n"
                                         "color: black;\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                         "padding-left:5px;\n"
                                         "padding-top:5px;\n"
                                         "}\n"
                                         "\n"
                                         "QTextEdit:focus{\n"
                                         "border: 2px solid rgb(126, 145, 191);\n"
                                         "\n"
                                         "}\n"
                                         "")
        self.decryptedText.setReadOnly(True)
        self.decryptedText.setObjectName("decryptedText")
        self.decrypt = QtWidgets.QPushButton(parent=self.widget)
        self.decrypt.setGeometry(QtCore.QRect(690, 450, 141, 51))
        self.decrypt.setStyleSheet("QPushButton#decrypt{\n"
                                   "background-color:rgba(166, 205, 255,0.5);\n"
                                   "font: 600 25pt \"Raleway\";\n"
                                   "border-radius: 15px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#decrypt:hover{\n"
                                   "background-color:rgb(126, 145, 191);\n"
                                   "font: 700 26pt \"Raleway\";\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton#decrypt:pressed{\n"
                                   "font: 600 24pt \"Raleway\";\n"
                                   "}\n"
                                   "")
        self.decrypt.setObjectName("decrypt")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(680, 70, 161, 41))
        self.label_9.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.generate = QtWidgets.QPushButton(parent=self.widget)
        self.generate.setGeometry(QtCore.QRect(430, 200, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate.sizePolicy().hasHeightForWidth())
        self.generate.setSizePolicy(sizePolicy)
        self.generate.setStyleSheet("QPushButton#generate\n"
                                    "{\n"
                                    "background-color:rgba(166, 205, 255,0.5);\n"
                                    "font: 600 25pt \"Raleway\";\n"
                                    "border-radius: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#generate:hover{\n"
                                    "background-color:rgb(126, 145, 191);\n"
                                    "font: 700 26pt \"Raleway\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#generate:pressed{\n"
                                    "font: 600 24pt \"Raleway\";\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.generate.setObjectName("generate")
        self.privateKeyN = QtWidgets.QLineEdit(parent=self.widget)
        self.privateKeyN.setGeometry(QtCore.QRect(590, 160, 341, 40))
        self.privateKeyN.setStyleSheet("QLineEdit{\n"
                                       "background-color:rgb(255, 255, 255);\n"
                                       "font: 18pt \"Raleway\"; background-color: white;\n"
                                       "color: black;\n"
                                       "border-radius: 15px;\n"
                                       "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:focus{\n"
                                       "border: 2px solid rgb(126, 145, 191);\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.privateKeyN.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.privateKeyN.setObjectName("privateKeyN")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(600, 210, 21, 31))
        self.label_8.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.privateKeyD = QtWidgets.QLineEdit(parent=self.widget)
        self.privateKeyD.setGeometry(QtCore.QRect(590, 250, 341, 40))
        self.privateKeyD.setStyleSheet("QLineEdit{\n"
                                       "background-color:rgb(255, 255, 255);\n"
                                       "font: 18pt \"Raleway\"; background-color: white;\n"
                                       "color: black;\n"
                                       "border-radius: 15px;\n"
                                       "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit:focus{\n"
                                       "border: 2px solid rgb(126, 145, 191);\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.privateKeyD.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.privateKeyD.setObjectName("privateKeyD")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(600, 120, 21, 31))
        self.label_10.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.widget)
        self.label_11.setGeometry(QtCore.QRect(600, 210, 21, 31))
        self.label_11.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.widget)
        self.label_12.setGeometry(QtCore.QRect(580, 510, 311, 41))
        self.label_12.setStyleSheet("font: 500 30pt \"Raleway\";")
        self.label_12.setObjectName("label_12")
        self.numberTextDecrypt = QtWidgets.QTextEdit(parent=self.widget)
        self.numberTextDecrypt.setGeometry(QtCore.QRect(570, 560, 381, 81))
        self.numberTextDecrypt.setStyleSheet("QTextEdit{\n"
                                             "background-color:rgb(255, 255, 255);\n"
                                             "font: 18pt \"Raleway\"; background-color: white;\n"
                                             "color: black;\n"
                                             "border-radius: 15px;\n"
                                             "border: 2px solid rgba(166, 205, 255,0.5);\n"
                                             "padding-left:5px;\n"
                                             "padding-top:5px;\n"
                                             "}\n"
                                             "\n"
                                             "QTextEdit:focus{\n"
                                             "border: 2px solid rgb(126, 145, 191);\n"
                                             "\n"
                                             "}\n"
                                             "")
        self.numberTextDecrypt.setReadOnly(True)
        self.numberTextDecrypt.setAcceptRichText(False)
        self.numberTextDecrypt.setObjectName("numberTextDecrypt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RSA cypher"))
        self.label.setText(_translate("Dialog", "RSA Cypher"))
        self.text_sifrovani.setPlaceholderText(_translate("Dialog", "Zadejte text k šifrování..."))
        self.encrypt.setText(_translate("Dialog", "Zašifrovat"))
        self.label_3.setText(_translate("Dialog", "Číselná hodnota"))
        self.label_4.setText(_translate("Dialog", "Zašifrovaný text"))
        self.label_5.setText(_translate("Dialog", "Public key"))
        self.label_6.setText(_translate("Dialog", "n"))
        self.label_7.setText(_translate("Dialog", "e"))
        self.text_desifrovani.setPlaceholderText(_translate("Dialog", "Zadejte text k dešifrování..."))
        self.label_23.setText(_translate("Dialog", "Dešifrovaný text"))
        self.decrypt.setText(_translate("Dialog", "Dešifrovat"))
        self.label_9.setText(_translate("Dialog", "Private key"))
        self.generate.setText(_translate("Dialog", "Generuj"))
        self.label_10.setText(_translate("Dialog", "n"))
        self.label_11.setText(_translate("Dialog", "d"))
        self.label_12.setText(_translate("Dialog", "Číselná hodnota"))

        self.generate.clicked.connect(self.generateKeyGui)
        self.encrypt.clicked.connect(self.encryptGui)
        self.decrypt.clicked.connect(self.decryptGui)

    def generateKeyGui(self):
        public_key, private_key = generateKey()
        self.publicKeyE.setText(str(public_key[1]))
        self.publicKeyN.setText(str(public_key[0]))
        self.privateKeyN.setText(str(private_key[0]))
        self.privateKeyD.setText(str(private_key[1]))

    def encryptGui(self):
        text = self.text_sifrovani.toPlainText()
        try:
            n = int(self.publicKeyN.text())
            e = int(self.publicKeyE.text())

            if len(str(n)) < 12 or len(str(e)) < 12:
                raise ValueError("Key length is too short. Minimum key length is 12.")

            public_key = (n, e)
            ascii_values = stringToASCII(text)
            bin_values = decimalListToBinary(ascii_values)
            superNumber = binaryListToSuperNumber(bin_values)
            blockSuperNmbr = blockSuperNumber(superNumber)
            superDecNmbr = binaryListToDecimalList(blockSuperNmbr)
            superDecNmbr_text = ' '.join(map(str, superDecNmbr))  # Convert the list to a space-separated string
            encryptText = encrypt(superDecNmbr, public_key)
            encryptTextString = ' '.join(map(str, encryptText))  # Convert the list to a space-separated string

            self.numberTextEncrypt.setText(superDecNmbr_text)
            self.encryptedText.setText(encryptTextString)

        except KeyError:
            QtWidgets.QMessageBox.critical(None, "Error", "Invalid key or text. Check your input.")
        except ValueError as ve:
            QtWidgets.QMessageBox.critical(None, "Error", str(ve))
        except UnboundLocalError:
            QtWidgets.QMessageBox.critical(None, "Error", "Invalid key or text. Check your input.")

    def decryptGui(self):
        text = self.text_desifrovani.toPlainText()
        try:
            n = int(self.privateKeyN.text())
            d = int(self.privateKeyD.text())

            if len(str(n)) < 12 or len(str(d)) < 12:
                raise ValueError("Key length is too short. Minimum key length is 12.")

            private_key = (n, d)

            # Convert the input string to a list of integers
            encryptedText = [int(char) for char in text.split()]

            decryptedText = decrypt(encryptedText, private_key)
            decListToBin10 = decimalListToBinary10(decryptedText)
            binSuperNumber = binaryListToSuperNumber(decListToBin10)
            splitSuperNmbr = splitSuperNumberToBinaryList(binSuperNumber)
            binListToDec = binaryListToDecimalList(splitSuperNmbr)
            stringFromAscii = asciiToString(binListToDec)
            decryptTextString = ' '.join(map(str, decryptedText))  # Convert the list to a space-separated string
            self.numberTextDecrypt.setText(decryptTextString)
            self.decryptedText.setText(stringFromAscii)
        except KeyError:
            QtWidgets.QMessageBox.critical(None, "Error", "Invalid key or text. Check your input.")
        except ValueError as ve:
            QtWidgets.QMessageBox.critical(None, "Error", str(ve))
        except UnboundLocalError:
            QtWidgets.QMessageBox.critical(None, "Error", "Invalid key or text. Check your input.")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
