class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """

        foodToInfo = {}
        cuisineToFoods = {}

        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            foodToInfo[food] = (cuisine, rating)
            insert(-rating, food)
            into
            cuisineToFoods[cuisine]

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)