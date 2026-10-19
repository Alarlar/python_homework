#Task 1

def hello():
    return "Hello!"
print(hello())

#Task 2

def greet(name):
    return f"Hi {name}"
print(greet("Test"))

#Task 3

def calc(a, b, op='multiply'):
    
    try:
        match op:
            case 'add':
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(6, 3, "add"))        
print(calc(5, 0, "divide"))     
print(calc("a", "b"))           
print(calc(4, 5))              

#Task 4

def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "float":
                return float(value)
            case "int":
                return int(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type_name}."

print(data_type_conversion("3.5", "float"))       
print(data_type_conversion(7.9, "int"))           
print(data_type_conversion(42, "str"))            
print(data_type_conversion("nonsense", "float")) 

#Task 5

def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

print(grade(90, 95, 100))     
print(grade(70, 75, 80))      
print(grade(40, 50))        
print(grade("a", "b")) 

#Task 6

def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

print(repeat("up,", 3))  
print(repeat("hi", 0))

#Task 7

def student_scores(mode, **kwargs):
    if mode == "best":
        best_name = ""
        best_score = 0
        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_name = name
        return best_name
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)

print(student_scores("best", Alice=90, Bob=75, Cara=95))   
print(student_scores("mean", Alice=90, Bob=70, Cara=80))   

#Task 8

def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return " ".join(result)

print(titleize("the lord of the rings"))  
print(titleize("war and peace"))          
print(titleize("a tale of two cities"))


#Task 9

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("alphabet", "ab"))  
print(hangman("hello", ""))        
print(hangman("cat", "tac"))      

#Task 10

def pig_latin(text):
    result = []
    for word in text.split():
        i = 0
        while i < len(word) and word[i] not in "aeiou":
            if word[i:i+2] == "qu":
                i += 2
            else:
                i += 1
        result.append(word[i:] + word[:i] + "ay")
    return " ".join(result)

print(pig_latin("apple"))        
print(pig_latin("cherry"))       
print(pig_latin("quick"))        
print(pig_latin("square"))       
print(pig_latin("the quick brown fox"))  