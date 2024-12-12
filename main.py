from logic import *

def main():
    """
    Main program to load UI
    """
    application =  QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()