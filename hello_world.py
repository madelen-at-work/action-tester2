''' hello_world module '''

NAME="action-tester2"

def main(name=NAME):
    ''' The main function '''
    print(f"Hello world! from {name}")

if __name__ == "__main__":
    main("main caller")
