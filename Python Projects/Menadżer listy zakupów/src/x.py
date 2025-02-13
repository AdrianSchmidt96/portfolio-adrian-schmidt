def getShoppingListAsString(self):
    result = ""
    for category, items in self.shoppingList.items():
        result += f"\n{category}:\n"
        for item in items:
            result += f"  - {item['nazwa']} ({item['waga/ilość']})\n"
    return result.strip()