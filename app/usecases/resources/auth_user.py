import uuid
from datetime import datetime

import attr
from attr.validators import instance_of, optional


@attr.s(frozen=True)
class AuthUser:

    username = attr.ib(validator=instance_of(str))
    password = attr.ib(validator=instance_of(str))
    email = attr.ib(validator=instance_of(str))

    # Auto-generated on creation of usecase object
    id = attr.ib(validator=instance_of(str))
    is_enabled = attr.ib(validator=optional(instance_of(bool)), default=True)

    # DB auto created
    # When we create the usecase objects in the app or from a POST, these will not be set,
    # but when we create the objects by reading from the database, these will be set
    created_at = attr.ib(validator=optional(instance_of(datetime)), default=None)
    updated_at = attr.ib(validator=optional(instance_of(datetime)), default=None)

    @id.default
    def generate_uuid(self) -> str:
        return str(uuid.uuid4())
