#___________________________________________MACHINE_LEARNING_BUTLER_________________________________________________
#GOAL: The machine learning program should have the mental capacity to learn new skills move robotic pieces
#___________________________________________________________________________________________________________________
#REQIREMENTS:   Be able to detect objects and people
#		Be able to move around or controle the house
#		Be able to talk to people
#		Be able to remind people of tasks
#		Complete regular tasks
#		Detect danger
#		Learn new things
#
#__________________________________________________________________________________________________________________
#Attributes:    Memory
#		Known objects
#		Known words
#		vision
#		hands
#		location
#		threats
#		known people
#		known tasks
#		known methods
#
#_________________________________________________________________________________________________________________
#Object Model:
#
#Memory:
#	time                                     | what time an event happened
#	emotion                                  | what is everyones emotions at the time
#	current emoji                            | how each individule feels when MLB tells story
#	when to tell                             | relation to current events
#	what to tell                             | what happened how to phrase and tell stories
#Known Object:
#	Object                                   | what is it
#	purpose                                  | what can it be used for
#	importance                               | what are the consequences of it breaking
#	expence                                  | how much an object is worth
#Known words:
#	meaning                                  | definition of a word
#	grammer                                  | how a sentence is formed
#Vision:
#	location                                 | where is MLB
#	other body location                      | where are things in relation to MLB
#	recognition                              | is there an item MLB dosen't know
#Hands:
#	desire                                   | does MLB want to get object
#	holdable                                 | can MLB hold object
#location:
#	locations                                | where are things
#	locations proper                         | where are things supposed to be
#threats:
#	threats                                  | what is a threat
#	danger level                             | is the threat dangerous
#known people:
#	name                                     | a persons name
#	age
#	relations to other known people
#	memories
#	closeness
#Known tasks:
#	order
#	application
#known methods:
#	order
#	applications
#	success
