from fastapi import FastAPI, Depends, HTTPException
from database import sessionLocal, Base, engine
from schemas import Todo as TodoSchema, TodoCreate
from sqlalchemy.orm import Session
from models import Todo as TodoModel
from database import sessionLocal, Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@app.post("/todos", response_model=TodoCreate)
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo= TodoModel(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos", response_model=list[TodoSchema])
def read_todo(db: Session = Depends(get_db)):
    return db.query(TodoModel).all()

@app.get("/todos/{todo_id}", response_model=TodoSchema)
def read_todo(todo_id: int,db: Session = Depends(get_db)):
   todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
   if not todo:
       raise HTTPException(status_code=404, detail="Todo not found")
   return todo

@app.put("/todos/{todo_id}", response_model=TodoSchema)
def update_todo(todo_id: int, updated: TodoCreate, db: Session= Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    for key,value in updated.dict().items():
        setattr(todo,key,value)
    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"method": "successfully deleted"}