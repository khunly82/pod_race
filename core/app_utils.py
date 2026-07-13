import inspect
from fastapi import APIRouter, FastAPI
import controllers
import exceptions

def add_controllers(app: FastAPI):
    for name, _ in inspect.getmembers(controllers):
        instance = getattr(controllers, name)
        if isinstance(instance, APIRouter):
            app.include_router(instance)

def add_exception_handlers(app: FastAPI):
    for _, obj in inspect.getmembers(exceptions):
        if inspect.isfunction(obj):
            sig = inspect.signature(obj)
            parameters = list(sig.parameters.values())
            if len(parameters) >= 2:
                exception_class = parameters[1].annotation
                if isinstance(exception_class, type) and issubclass(exception_class, BaseException):
                    app.add_exception_handler(exception_class, obj)