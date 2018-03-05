while True:
    try:
        n = input("\nPls enter an integer.\n> ")
        n = int(n)
        break

    except ValueError:
        print("\nWTF? That is NOT an integer.\nTry again, Dipshit.")

print('Well, %i is an integer. Good job. You may live the rest of the day without\nworrying about be raping your butt.' % n)
