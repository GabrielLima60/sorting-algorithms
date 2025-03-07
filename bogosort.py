import time

array = [1, 4, 2, 6, 2, 1, 6, 1, 9]

class bogosort:
    def __init__(self, array):
        start = time.time()
        self.array = array

        while True:
            if self.is_sorted():
                time_result = round(time.time() - start, 4)

                print(f'it took {time_result} seconds')
                break
            else:
                self.randomize()
                print(self.array)

    def is_sorted(self):
        return all(self.array[i] <= self.array[i+1] for i in range(len(self.array)) if i < len(self.array) - 1)

    def randomize(self):
        n = len(self.array)
        for i in range(len(self.array) - 1, 0, -1):
            j = int(time.time()*10000000) % (i + 1)

            self.array[i], self.array[j] = self.array[j], self.array[i]        

bogosort(array)


 
