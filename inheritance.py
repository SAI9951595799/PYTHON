class animal:
    def speak(self):
        print("This animal make a sound")
class dog(animal):
    def speak(self):
        print("Dog barks: Woof! Woof!")
class cat(animal):
    def speak(self):
        print("Cat meows: Meow! Meow!")
dog = dog()
cat= cat()
dog.speak()
cat.speak()
