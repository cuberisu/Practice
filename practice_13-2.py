# 2 TV 클래스 정의
class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 0
        self.on = False
        
    def turnOn(self):
        self.on = True
        
    def turnOff(self):
        self.on = False
        
    def setVolume(self, volume):
        self.volume = volume
        
    def setChannel(self, channel):
        self.channel = channel
    
tv = TV()
tv.turnOn()
tv.setChannel(11)
tv.setVolume(6)
print("채널: ", tv.channel, "음량:", tv.volume);