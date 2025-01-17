
class AuthRouter:
    print("Auth Router  is running --------------------------- ")
    main_apps={'admin','auth','contenttypes','sessions','messages','staticfiles'}
    new_app = 'app'
    def db_for_read(self,model,**hints):
        print(model._meta.app_label)
        if model._meta.app_label in self.main_apps:
            return 'default'
        elif model._meta.app_label == self.new_app:
            return 'new'
        else:
            return None
        
    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.main_apps:
            return 'default'
        elif model._meta.app_label == self.new_app:
            return 'new'
        else:
            return None
        
    def allow_relation(self,obj1,obj2,**hints):
        if obj1._meta.app_label in self.main_apps or obj2._meta.app_label in self.main_apps:
            return True
        elif obj1._meta.app_label == self.new_app or obj2._meta.app_label == self.new_app:
            return True
        else:
            return None
        
    def allow_migrate(self,db,app_label,model_name=None,**hints):
        
        if app_label in self.main_apps:
            return db == 'default'
        elif app_label == 'app':
            return db == 'new'
        else:
            return None
        