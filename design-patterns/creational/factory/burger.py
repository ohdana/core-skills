class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def print(self):
        print(self.ingredients)
        
class BurgerFactory:
    def createBurger(self):
        ingredients = ['bun', 'patty', 'sauce']
        return Burger(ingredients)
    
    def createCheeseBurger(self):
        ingredients = ['bun', 'cheese', 'patty', 'sauce']
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ['bun', 'vegan cheese', 'vegan patty', 'vegan sauce']
        return Burger(ingredients)
    
burgerFactory = BurgerFactory()
burgerFactory.createBurger().print()
burgerFactory.createCheeseBurger().print()
burgerFactory.createVeganBurger().print()