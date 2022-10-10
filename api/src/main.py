from fastapi import FastAPI

api = FastAPI(debug=True)


@api.get('/')
def root():
    return {'message': 'Welcom !!!'}

