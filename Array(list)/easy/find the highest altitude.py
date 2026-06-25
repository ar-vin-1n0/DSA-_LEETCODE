#FIND THE HIGHEST ALTITUDE
class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        max_altitude = 0
        for i in gain:
            highest += i
            if highest > max_altitude:
                max_altitude = highest

        return max_altitude     
