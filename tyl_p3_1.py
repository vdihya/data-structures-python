def reverse(str):
    words = str.split(" ")
    reversewordlist = words[::-1]
    print(" ".join(reversewordlist))

reverse("I love cmrit")
reverse(input("enter a string to be reversed: "))