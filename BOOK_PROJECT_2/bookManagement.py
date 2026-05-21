import os
print(os.getcwd())

class Book():
  def __init__(self,bid,tittle,author):
    self.bid=bid
    self.tittle=tittle
    self.author=author


  def save(self):
    with open("books.txt","a") as f:
      f.write(f"{self.bid},{self.tittle},{self.author} \n")


# ADD BOOKS

def add_book():
  try:
    bid=input("Enter the Book Id : ")
    tittle=input("Enter the tittle : ")
    author=input("Enter the author name : ")

    book=Book(bid,tittle,author)
    book.save()
    print("Book is added successfully !")
  except Exception as e:
    print("Error : ",e)

# VIEWW BOOK
def view_book():
  try:
    with open("books.txt","r") as f:
      for line in f:
        bid,tittle,author=line.strip().split(",")
        print(f"BOOK ID : {bid},BOOK TITTLE : {tittle},AUTHOR NAME : {author}")
  except FileNotFoundError:
    print("No records found")


def search_book():
  bid_search=input("enter the book ID : ")
  found=False
  try:
    with open("books.txt","r") as f:
      for line in f:
        bid,tittle,author=line.strip().split(",")
        if bid==bid_search:
          print(f"Found,Book Tittle : {tittle},Author Name : {author}")
          found= True
          break
        
  except Exception as e:
    print("Error : ",e)




while True:
  print("----  Book Management System  -----")
  print("1 for ADD BOOK")
  print("2 for VIEW BOOK")
  print("3 for SEARCH BOOK")
  print("4 for exit")
  num=input("ENTER THE CHOICE : ")
  if num=="1":
    add_book()
  elif num =="2":
    view_book()
  elif num=="3":
    search_book()

  elif num=="4":
    break

  else:
    print("INVALID  CHOICE")



  