class GeoLocationDBRouter:
    """
    Database router for models that should use the geo_location_db database.
    """

    def db_for_read(self, model, **hints):
        """
        Suggests the geo_location_db for reading operations if the model is meant for it.
        """
        if model._meta.app_label == 'near_me':
            return 'geo_location_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Suggests the geo_location_db for writing operations if the model is meant for it.
        """
        if model._meta.app_label == 'near_me':
            return 'geo_location_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both objects are meant for the geo_location_db.
        """
        if obj1._state.db == 'geo_location_db' and obj2._state.db == 'geo_location_db':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the near_me app's models get created on the geo_location_db.
        """
        if app_label == 'near_me':
            return db == 'geo_location_db'
        return None
