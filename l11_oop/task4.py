from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self) -> str:
        """What does the Animal say?

        Returns:
            str: the sound that the animal makes
        """


# Modify classes Dog and Cat to make the script work.
#
# HINT: Dog and Cat must inherit class Animal
class Dog:
    def speak(self):
        return "woof"


class Cat:
    def speak(self):
        return "meow"


if __name__ == "__main__":
    assert Dog().speak() == "woof"
    assert Cat().speak() == "meow"
