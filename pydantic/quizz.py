# You need to create a Pydantic model that represents a complex data structure containing nested objects and arrays. The requirements for the model are as follows:

#     The top-level object should have a required string field called "name".
#     It should have an optional integer field called "age" which should be greater than or equal to 0.
#     It should have a list field called "items" which can contain multiple dictionaries, each representing an item. Each item dictionary should have a required string field called "item_name" and an optional float field called "item_price" which should be greater than 0 if present.
#     The model should have a nested object field called "metadata" which should have two optional fields: "description" (string) and "tags" (a list of strings).
#     The model should enforce that "age" is less than or equal to 100 if it is provided.

# Your task is to implement this Pydantic model and write a function that takes a JSON payload as input, validates it against the model, and returns the validated data if it passes the validation, or raises appropriate validation errors if the data is invalid.

# Good luck!


from pydantic import BaseModel, conint, confloat, field_validator, ValidationError


class MetaData(BaseModel):
    description: str | None
    tags: list[str] | None

class User(BaseModel):
    name: str 
    age: conint(ge=0, lt=100) | None
    items: list[dict[str, str | confloat(gt=0)]]
    metadata: MetaData

    @field_validator('items')
    def name_must_contain_space(cls, value):
        print(value)
        if not any("item_name" and not isinstance(d["item_name"], str) in d for d in value):
            raise ValueError("The Dictionarys Should Have required string field called 'item_name'")
        
        if not any("item_price" and not isinstance(d["item_name"], float) in d for d in value):
            raise ValueError("The Dictionarys Should Have optional float field called 'item_price' which should be greater than 0 if present")
        
        return value
    
metadata = MetaData(description="hey", tags=["2434", "salam"])
user = User(name="sadegh", age=0, items=[{"item_name":"hey man", "item_price":234.23}], metadata=metadata)
