def item_order(order):
    ham = order.count("hamburger")
    sal = order.count("salad")
    wat = order.count("water")
    result = "salad:" + str(sal) + " hamburger:" + str(ham) + " water:" + str(wat);
    return result;