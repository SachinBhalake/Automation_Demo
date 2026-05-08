class EndPoints:
    # Auth
    Auth_User_Login = "/auth/login"
    Auth_User_Details = "/auth/me"

    # Users
    User_Get_All = "/users"
    User_Get_By_Id = "/users/{id}"
    User_Create = "/users/add"
    User_Update = "/users/{id}"
    User_Delete = "/users/{id}"