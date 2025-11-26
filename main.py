from db.write_db_soldier import write_db
from return_http.post_sent_scv import post_sent_csv
import  uvicorn
from fastapi import FastAPI,HTTPException, UploadFile, File, BackgroundTasks
import csv
import codecs




app = FastAPI()


@app.get("/")
def root():

    return {"Welcome to the menger base sibolt "}


@app.post("/assignWithCsv")
def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    background_tasks.add_task(file.file.close)

    write_db(list(csvReader))

    return post_sent_csv()

#
# @app.get("/space")
# def get_space():
#     pass
#
#
# @app.get("/search")
# def search():
#






# if __name__ == "__main__":
#     uvicorn.run("main:app", port=8000, log_level="info")
#







