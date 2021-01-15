from ariadne import ObjectType, QueryType, MutationType, gql, make_executable_schema
from ariadne.asgi import GraphQL
import mongo

type_defs = gql("""
    type Query {
        bears: [Bear!]!
        people: [Person!]!
    }
    
    type Bear {
      bear: String
    }
    

    type Person {
        firstName: String
        lastName: String
        age: Int
        fullName: String
    }
    
    type Mutation {
       AddUser(input: employeeInput): employeePayload
    }
    
    input employeeInput {
      firstName: String
      lastName: String
      age: Int
    }
    
    type employeePayload {
      employee: Person
    }
    
""")

query = QueryType()

bear = [
    {"bear": "rooooar"},
        {"bear": "dcrttv"}
   ]

returnarray = mongo.mongo_get()

mutation = MutationType()

@mutation.field("AddUser")
def resolve_create_user(_, info, input, **data):
    clean_input = {
        "firstName": input["firstName"],
        "lastName": input["lastName"],
        "age": input["age"]
    }
    print(data.get("AddUser"))
    try:
        return {
            "status": True,
            "discussion": "efe"
        }
    except ValidationError as err:
        return {
            "status": False,
            "error": err,
        }


@query.field("people")
def resolve_people(*_, **data):
    print(data.get("people"))
    return returnarray


@query.field("bears")
def resolve_people(*_):
    return bear

person = ObjectType("Person")
@person.field("fullName")
def resolve_person_fullname(person, *_):
    return "%s %s" % (person["firstName"], person["lastName"])


schema = make_executable_schema(type_defs, query, person)

app = GraphQL(schema, debug=True)