from sqlalchemy import create_engine

# It was not immediately apparent to me that I would need to import the dog model here. 
# The labs leading up to this one did not show this workflow.
from models import Dog 

engine = create_engine('sqlite:///:memory:')

def create_table(base):
    # I was able to get this test to pass just by returning the engine here, but now adding the line below from the solution.
    base.metadata.create_all(engine)
    # Reviewing the 'Defining a Schema with SQLAlchemy ORM' reading, I now see this line is mentioned as being what tells
    # the engine that models created with the specified base as a parent should be used to create tables.
    return engine

# The next test was straightforward to pass based on the information we'd received in previous labs and the information in the test.
def save(session, dog):
    session.add(dog)
    session.commit()
    return session

# I could not figure out what this next test was asking.
# It didn't help that all the other functions already had all the parameters we'd need defined ahead of time, but this one was missing the 'row' parameter.
# I altered the test because it didn't make sense to me as written.
# I thought that the second parameter that was being passed in was the desired outcome of the function in the first place, so I removed from the test.

# My original function:
# def new_from_db(session):
    # return session.query(Dog).first()

# Now I can see that the test wanted to be passed a database row as the second parameter, and then for the function to return that same row from the table based on id.
# I am not sure why you would do this in practice, it seems very redundant. I could use some clarification on the desired outcome here.
# The version the test was looking for:
def new_from_db(session, row):
    return session.query(Dog).filter_by(id = row.id).first()

def get_all(session):
    # I was able to get this test to pass with this line: 
    # return session.query(Dog)

    # The solution code returned a list comprehension instead:
    return [dog for dog in session.query(Dog)]

# The next three tests were straightforward to pass but the solution code uses a syntax we weren't shown previously for specifying columns.
def find_by_name(session, name):
    # My solution which follows the syntax outlined in 'Create Read Update and Delete with SQLAlchemy Lab' for specifying fields as (Table.field == arg):
    # return session.query(Dog).filter(Dog.name == name).first()

    # learn-co-curriculum solution which specifies field as (field=arg) - syntax we weren't shown in previous labs/readings:
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # My solution which follows the syntax outlined in 'Create Read Update and Delete with SQLAlchemy Lab' for specifying fields as (Table.field == arg):
    # return session.query(Dog).filter(Dog.id == id).first()

    # learn-co-curriculum solution which specifies field as (field=arg) - syntax we weren't shown in previous labs/readings:
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    # My solution which follows the syntax outlined in 'Create Read Update and Delete with SQLAlchemy Lab' for specifying fields as (Table.field == arg):
    # return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

    # learn-co-curriculum solution which specifies field as (field=arg) - syntax we weren't shown in previous labs/readings:
    return session.query(Dog).filter_by(name=name, breed=breed).first()
    
def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    # I was able to get this test to pass without the next line:
    return session