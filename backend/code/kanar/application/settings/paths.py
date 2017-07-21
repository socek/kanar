from os.path import dirname


def paths_setting(settings, paths):
    def get_project_dir(dirs):
        project_dir = __file__
        for index in range(dirs):
            project_dir = dirname(project_dir)
        return project_dir

    with paths.set('code', get_project_dir(4)) as code:
        with code.set('src', 'kanar') as src:
            with src.set('app:home', 'home') as home:
                home.set('app:home:routing', 'routing.yml')

            with src.set('app:auth', 'auth') as auth:
                auth.set('app:auth:routing', 'routing.yml')

            with src.set('app:menu', 'menu') as menu:
                menu.set('app:menu:routing', 'routing.yml')

        code.set('data', 'data')
