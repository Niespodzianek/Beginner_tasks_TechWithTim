import random

colors = ["red", "yellow", "blue", "pink", "green", "brown", "cyan", "orange"]
print(f"Dostępne kolory to:\n{colors}")
random.shuffle(colors)
choosen_colors = colors[:4]
print(f"Debug: wylosowane kolory to: {choosen_colors}")

counter = 0
while counter < 10:
	finded_colors = []
	counter += 1
	print(f"Debug - kolejka: {counter}")
	print(f"Debug - Odgadnione kolory to: {finded_colors}")
	answer = input("Write 4 colors: ")
	answer_2 = answer.split()
	print(f"Debug: proponowane kolory {answer_2}")
	for index, element in enumerate(answer_2):
		if element in choosen_colors:
			if element == choosen_colors[index]:
				print(f"Debug: pozycja {[index + 1]} - CZARNY")
				finded_colors.append(element)
				if len(finded_colors) == 4:
					print(f"Debug: WYGRAŁEŚ w {counter} kolejkach")
					counter = 10
			else:
				print(f"Debug: pozycja {[index + 1]} - BIAŁY")
		else:
			print(f"Debug: pozycja {[index + 1]} - PUSTY")
print("Debug: GAME OVER")

