from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import MyCustomDB                                #<-- links to the name of the currrent database to easily change all models to use a new database at same time
class User:                         # singular instance of...
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("name must be longer than 3 characters")
            is_valid = False
        
        if not data['location']:
            flash("choose a location")
            is_valid = False

        if not data['language']:
            flash("choose a language")
            is_valid = False

        if not data['comment']:
            flash("Add a comment")
            is_valid = False

        print("validation ran")
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( name, location, language, comment , created_at , updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s, NOW() , NOW() );"
        return connectToMySQL(MyCustomDB).query_db( query, data )


    @classmethod
    def get_last(cls):
        query = "SELECT * FROM users ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL(MyCustomDB).query_db(query,)
        return cls(results[0])