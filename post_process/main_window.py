# coding: utf-8

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, \
    QPushButton, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap

from sys import argv, exit
from functools import partial


class Main_window(QMainWindow):

  def __init__(self, app: QApplication):
      super().__init__()
      self._app = app

      self.setWindowTitle('Post processing interface')
      self._general_layout = QHBoxLayout()
      self._central_widget = QWidget(self)
      self.setCentralWidget(self._central_widget)
      self._central_widget.setLayout(self._general_layout)

      self._files_layout = QVBoxLayout()
      self._button = QPushButton("Test")
      self._button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
      self._files_layout.addWidget(self._button)
      self._general_layout.addLayout(self._files_layout)

      self._images_layout = QHBoxLayout()
      self._label = QLabel()
      self._image = QPixmap(QImage())
      self._label.setPixmap(self._image)
      self._label.setStyleSheet("border: 1px solid black;")
      self._images_layout.addWidget(self._label)
      self._general_layout.addLayout(self._images_layout)

      self._button.clicked.connect(partial(self._pass, None))

  def __call__(self, *args, **kwargs):
      self.showMaximized()

  def _pass(self, *_, **__):
      pass


if __name__ == '__main__':

  app = QApplication(argv)
  Main_window(app)()
  exit(app.exec())
