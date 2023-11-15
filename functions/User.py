from Models import Register

def welcome():
    return {"message":"Welcome to the page of Faisal Vai"}

def register(post: Register):
    return {"data":post.dict()}