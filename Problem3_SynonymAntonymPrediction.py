from functions import io

def main():
    model = io.load_w2v('word2vec/W2V_150.txt')

if __name__ == '__main__':
    main()