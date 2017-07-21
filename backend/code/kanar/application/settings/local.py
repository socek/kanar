def make_settings(settings, paths):
    database(settings, paths)
    settings['threads'] = 1
    settings['debugtoolbar.enabled'] = True


def database(settings, paths):
    # ----------------------------------------
    # This is example postgresql configuration
    # ----------------------------------------
    settings['db:type'] = 'postgresql'
    settings['db:login'] = 'kanar'
    settings['db:password'] = 'kanar'
    settings['db:host'] = 'postgres'
    settings['db:name'] = 'kanar'
    settings['db:port'] = '5432'
