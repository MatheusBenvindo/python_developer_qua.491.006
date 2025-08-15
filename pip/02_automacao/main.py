import pyautogui as auto

def main():
    auto.hotkey("win")
    auto.write("word")
    auto.hotkey("enter")
    auto.sleep(5)
    auto.hotkey("enter")
    auto.sleep(2)
    auto.write("Boo! Eu sou o fantasma da máquina, e vou te assombrar!!!")

if __name__ == "__main__":
    main()


    git config --global --unset user.name 
