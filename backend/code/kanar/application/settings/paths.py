from os.path import dirname


def paths_setting(settings, paths):
    def get_project_dir(dirs):
        project_dir = __file__
        for index in range(dirs):
            project_dir = dirname(project_dir)
        return project_dir

    with paths.set('code', get_project_dir(4)) as code:
        with code.set('src', 'kanar') as src:
            with src.set('app:application', 'application') as home:
                with home.set('app:settings', 'settings') as settings_path:
                    settings_path.set('settings:command', 'command.py')
                    settings_path.set('settings:default', 'default.py')
                    settings_path.set('settings:local', 'local.py')
                    settings_path.set('settings:paths', 'paths.py')
                    settings_path.set('settings:tests', 'tests.py')

            with src.set('app:home', 'home') as home:
                home.set('app:home:routing', 'routing.yml')

            with src.set('app:auth', 'auth') as auth:
                auth.set('app:auth:routing', 'routing.yml')

            with src.set('app:menu', 'menu') as menu:
                menu.set('app:menu:routing', 'routing.yml')

            with src.set('app:commands', 'commands') as commands:
                with commands.set('backend:templates', 'templates') as templates:
                    templates.set('template:backendini', 'backend.ini.jinja2')

        code.set('data', 'data')
        code.set('backend:ini', 'backend.ini')

    with paths.set('root', '/usr/local/bin', is_root=True) as execs:
        execs.set('exe:pserve', 'pserve')

    with paths.set('logs', '/tmp', is_root=True) as logs:
        logs.set('logs:all', 'all.log')
