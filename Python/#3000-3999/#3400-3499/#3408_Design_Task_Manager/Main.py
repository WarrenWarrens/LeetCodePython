import heapq
class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.tasks = []
        self.taskPrior = {}
        self.taskOwn = {}
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        heapq.heappush(self.tasks, (-priority, -taskId, taskId))
        self.taskPrior[taskId] = priority
        self.taskOwn[taskId] = userId

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        heapq.heappush(self.tasks, (-newPriority, -taskId, taskId))
        self.taskPrior[taskId] = newPriority

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        self.taskPrior[taskId] = -1

    def execTop(self):
        """
        :rtype: int
        """
        while self.tasks:
            priority, negTaskId, taskId = heapq.heappop(self.tasks)
            if self.taskPrior[taskId] != -1 and -priority == self.taskPrior[taskId]:
                self.taskPrior[taskId] = -1
                return self.taskOwn[taskId]
        return -1
