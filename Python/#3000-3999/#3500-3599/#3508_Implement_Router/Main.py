class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memlimit = memoryLimit
        self.queue = deque()
        self.packset = set()
        self.destimemap = defaultdict(SortedList)

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        key = (source, destination, timestamp)
        if key in self.packset:
            return False

        if len(self.queue) >= self.memlimit:
            oldpacket = self.queue.popleft()
            oldkey = tuple(oldpacket)
            self.packset.remove(oldkey)
            self.destimemap[oldpacket[1]].remove(oldpacket[2])
        self.queue.append([source, destination, timestamp])
        self.packset.add(key)
        self.destimemap[destination].add(timestamp)
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.queue:
            return []

        packet = self.queue.popleft()
        key = tuple(packet)
        self.packset.remove(key)
        self.destimemap[packet[1]].remove(packet[2])
        return packet

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        timestamps = self.destimemap[destination]
        left = timestamps.bisect_left(startTime)
        right = timestamps.bisect_right(endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)