
class NumberPairFinder:
    def __init__(self):
        self.numbers = []

    def add_numbers(self, num_list):
        
        self.numbers = num_list

    def find_pair_with_sum(self, target_sum):
        
        seen = {}
        for i, num in enumerate(self.numbers):
            complement = target_sum - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return -1


finder = NumberPairFinder()
finder.add_numbers([1, 2, 3, 4, 5])
print(finder.find_pair_with_sum(9)) 
print(finder.find_pair_with_sum(10))


