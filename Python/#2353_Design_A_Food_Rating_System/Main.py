import heapq


class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foodtocuisine = {}
        self.foodrating = {}
        self.cuisinefood = {}
        for fo, cu, ra in zip(foods, cuisines, ratings):
            self.foodtocuisine[fo] = cu
            self.foodrating[fo] = ra
            if cu not in self.cuisinefood:
                self.cuisinefood[cu] = []
            heapq.heappush(self.cuisinefood[cu], (-ra, fo))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.foodtocuisine[food]
        self.foodrating[food] = newRating
        heapq.heappush(self.cuisinefood[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cuisinefood[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.foodrating[food]:
                return food
            heapq.heappop(heap)
