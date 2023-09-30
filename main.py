import sys

from PyQt5.QtWidgets import QWidget, QApplication
# pyQt5 必须的类


def main():
    # create QApplication class
    app = QApplication(sys.argv)

    # create a Q window
    # noinspection PyArgumentList
    w = QWidget()

    # set size of window
    w.resize(600, 600)

    # move the window
    w.move(100, 100)

    # set title
    w.setWindowTitle("MATRIX Calculator")

    # show window
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
