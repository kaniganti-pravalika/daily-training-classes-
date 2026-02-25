class RaniRestaurant:
    def __init__(self):
        self.menu = {
            "breakfast": ["idli", "boond", "dosa", "puri", "chapathi"],
            "lunch": ["sambar", "aavakaya", "masala brinjal", "paneer curry"],
            "dinner": ["pulka", "noodles", "veg rice"]
        }

        self.price = {
            "breakfast": [40, 30, 40, 40, 35],
            "lunch": [150, 100, 200, 170],
            "dinner": [50, 30, 50]
        }

        self.total = 0

    def display_menu(self, category):
        print("\n" + category.capitalize() + " Menu:")
        for i, item in enumerate(self.menu[category], 1):
            print(i, item, "- Rs.", self.price[category][i - 1])

    def select_item(self, category, choice):
        if 1 <= choice <= len(self.menu[category]):
            selected_item = self.menu[category][choice - 1]
            price = self.price[category][choice - 1]
            self.total += price

            print("Selected:", selected_item)
            print("Total so far: Rs.", self.total)
        else:
            print("Invalid Selection")


restaurant = RaniRestaurant()

while True:
    print("\nWelcome To Our Rani Restaurant!")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == '4':
        print("\nTotal Bill: Rs.", restaurant.total)
        print("Thank You! Visit Again 😊")
        break

    elif choice in ['1', '2', '3']:
        category = list(restaurant.menu.keys())[int(choice) - 1]
        restaurant.display_menu(category)
        item_choice = int(input("Select an item by number: "))
        restaurant.select_item(category, item_choice)

    else:
        print("Invalid option")
