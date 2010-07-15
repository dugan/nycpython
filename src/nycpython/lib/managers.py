def get_live_manager(manager_class=None):
    if manager_class is None:
        manager_class = models.Manager
    class LiveManager(manager_class):
        def get_query_set(self):
            return super(LiveManager, self).get_query_set().filter(published=True)
    return LiveManager

