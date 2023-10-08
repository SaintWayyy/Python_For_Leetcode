class Base:
    public_static_field = "public static field"
    _protected_static_field = "protected static field"
    __private_static_field = "private static field"

    # There can only be one method per class
    def __init__(self,
                 public_field="public field",
                 protected_field="protected field",
                 private_field="private_field"):
        self.public_field = public_field
        self._protected_field = protected_field
        self.__private_field = private_field

    def public_method(self):
        print("public method")

    def _protected_method(self):
        print("protected method")

    def __private_method(self):
        print("private method")

    @staticmethod
    def public_static_method():
        print("public static method")

    @staticmethod
    def _protected_static_method():
        print("protected static method")

    @staticmethod
    def __private_static_method():
        print("private static method")


print(Base.public_static_field)
# print(Base._protected_static_field)
# print(Base.__private_static_field)

Base.public_static_method()
# Base._protected_static_method()
# Base.__private_static_method()

base = Base("public field", "protected field", "private_field")

print(base.public_field)
# print(base._protected_field)
# print(base.__private_field)

base.public_method()
# base._protected_method()
# base.__private_method()
