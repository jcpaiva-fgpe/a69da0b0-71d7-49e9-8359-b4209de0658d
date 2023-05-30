def shopping_list(items):
    items.sort()
    result = "Your Shopping List:\n\n"
    for i in range(len(items)):
        result += str(i+1)+". "+items[i].capitalize()+"\n"
    return result