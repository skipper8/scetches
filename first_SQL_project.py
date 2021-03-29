#First SQL PROJECT

#________________________________ANALYSIS______________________________________

#______________________________________________________________________________
#GOAL: To apply what I have learned about sequel into a project and learn how to combine SQL and python by creating a book database for my books.

#______________________________________________________________________________
#REQUIREMENTS:   needs to be able to add books to SQL database and retrieve books
		#store all important book information (title, author, IBN, edition, publisher, year, form, price, ...
		#be able to determin value of collection
		#be accesable hold onto wishlist
		#check capacity
		#check how many times read
		#checkout system

#______________________________System Archetecture___________________________
#page with four tabs
	#search
		#finds book in system based on any attribute
		#choice in attribute
	#wishlist
		#shows list of desired books that is cross refenced to check that there is no overlap with existing collection
	#checkout
		#finds book
		#check availability
		#records person removing book
		#changes books availability
	#return
		#changes books availability

#____________________________OBJECT DESIGN___________________________________

#OBJECT DIAGRAM_____________________________________________________________

#classes		| instances

#BOOK			| all individual books
#title, author, IBN,year|
#publisher, edition     |
#price			|

#PERSON			|all users of the library
#book they have		|

#WISHLIST		|books we want
#books, disrire level	|

#Collection		|all books in library
#books, availability,   |
#condition, gain data	|
