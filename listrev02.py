#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    anotheremptylist = []

    ## This will throw an ERROR
    ## the extend method expects exactly one argument
    a = ['10.0.0.1', 'retro_game_server']
    anotheremptylist.extend(a)

    print(anotheremptylist)

if __name__ == "__main__":
    main()

