class Reindeer(object):

    def __init__(self, name, speed, flight_duration, rest):
        self.name = name
        self.speed = int(speed)
        self.flight_duration = int(flight_duration)
        self.rest = int(rest)
        self.state = 'flying'
        self.time_remaining = int(flight_duration)
        self.distance_travelled = 0

    def tick(self):
        if self.state == 'flying':
            self.distance_travelled += self.speed
            self.time_remaining -= 1
            if not self.time_remaining:
                self.state = 'resting'
                self.time_remaining = self.rest
        else:
            self.time_remaining -= 1
            if not self.time_remaining:
                self.state = 'flying'
                self.time_remaining = self.flight_duration

    def __str__(self):
        return ('{} has flown {}'.format(self.name, self.distance_travelled))

reindeer = []

f = open('a14_input.txt','r')
for line in f:
    element = line.strip().split()
    reindeer.append(Reindeer(element[0], element[3], element[6], element[13]))
f.close()

for _ in range(2503):
    for r in reindeer:
        r.tick()

for x in reversed(sorted(reindeer, key=lambda x: x.distance_travelled)):
    print(str(x))


