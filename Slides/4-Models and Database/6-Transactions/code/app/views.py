from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction

# Create your views here.
# Atomic if the atomic settings is true
def atomic_view(request):
    return HttpResponse("atomic view is called...",status = 200)

# non atomic in the case of the active settings
@transaction.non_atomic_requests
def non_atomic_view(request):
    return HttpResponse(" non atomic view is called...",status = 200)


# atomic throuch decorators
@transaction.atomic(durable=True)
def atomic_view_from_decorators(request):
    return HttpResponse("Atomic through the decorators")


# atomic through context managers
def context_atomic(request):
    with transaction.atomic():
        pass
    
# useless function
def dummy():
    pass

# try and except atomic transaction
@transaction.atomic(using="default")
def try_atomic(request):
    dummy()
    
    try:
        with transaction.atomic():
            dummy()
    except Exception as E:
        print(E)
        
    dummy()    
    
    

# On commit function calls
@transaction.atomic
def on_commit_caller(request):
    with transaction.atomic:
        pass
    transaction.on_commit(dummy)
    
    
# transaction commit and rollback
def manual_committer(request):
    try:
        transaction.set_autocommit(autocommit=False)
        # some db queries
        # ------------
        # -------
        # ---
        transaction.commit()
        transaction.set_autocommit(autocommit=True)
    except Exception as E:
        # exception handling is here
        transaction.rollback()
        
# savepoints using transaction
def savepoints_function(request):
    dummy()
    point = transaction.savepoint()
    try:
        # code here
        transaction.savepoint_commit(sid=point)
        # transaction.set_rollback(rollback=False)
        pass
    except Exception as E:
        # code here
        transaction.savepoint_rollback(sid=point)
        pass
    