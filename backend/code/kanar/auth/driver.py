from kanar.application.driver import ReadDriver
from kanar.application.driver import WriteDriver

from kanar.auth.models import User


class UserReadDriver(ReadDriver):
    model = User

    def get_by_name(self, name):
        return self.query().filter(self.model.name == name).one()


class UserWriteDriver(WriteDriver):
    model = User

    def create(self, **kwargs):
        password = None
        obj = self.model()
        if 'password' in kwargs:
            password = kwargs.pop('password')

        for key, value in kwargs.items():
            setattr(obj, key, value)

        if password:
            obj.set_password(password)

        self.database.add(obj)
        self.database.commit()

        return obj
