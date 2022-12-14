import sys
import kikuchipy as kp
import matplotlib.pyplot as plt

#path = sys.argv[1]

def signalNavigation(file_path):
    try:
        s = kp.load(file_path, lazy=True)
    except Exception as e:
        raise e
    s.plot()
    plt.show()

#if __name__ == "__main__":
#    signalNavigation(path)