# Rotarran

## About

Application for storing financial history and show proper statistics. This is an experiment of integrating some technologies:

- Pyramid
- Sqlalchemy + alembic
- Angualr2
- Docker
- Baelfire

## First run

For first run we use makefile:

```
$ make
```

It will create virtualenv which gives us tools for managing the backend and frontend tools.

```
. ./venv_rotarran/bin/activate
```

After that, you need to add this to your `/etc/hosts` file to be able to use development server by domain:

```
169.253.0.240   rolocal.com

```

## Avalible host tools

### container - running containers

`container` is a tool for starting containers. The container dependency are set in the `docker-compolse.yml` file, so
if you want to start whole project, just type

```
container nginx
```

This console tool has 2 important switches:

```
-b, --bash            Start bash under running container.
-o, --logs            Show logs of running container.
```

### backend - running tools on backend container

Use tools from backend container. For now we only have shell supported.

```
backend shell
```

### btest - running pytest on backend container

Use py.test like it would be used, when the application were on host.

```
btest -h
```

### balembic - running alembic on backend container

Use alembic like it would be used, when the application were on host.

```
balembic -h
```

### ftest - running test on frontend container

Use frontend tests, like it would be used, when the application were on host.

```
ftest
```

## Avalible tools running under container

### Backend

#### backend tool

```
backend -h
```

This command line tool is for using pyramid tools.

```
backend dev - run dev server (default command of the container)
backend shell - run dev shell
```

#### balembic

balembic is a wrapper for alembic command. Alembic is for postgresql migration.
If you want to migrate, just type:

```
balembic upgrade head
```

If you want to create new migration, just type:


```
balembic revision -m "comment"
```

For more documentation, go to http://alembic.zzzcomputing.com/en/latest/

#### btest - pytest

btest is a proxy for py.test command. For more info about py.test, see https://docs.pytest.org/en/latest/

```
btest -h
```
