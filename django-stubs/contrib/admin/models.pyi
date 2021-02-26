from typing import Any, Optional, Union
from uuid import UUID

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.base import Model

ADDITION: int
CHANGE: int
DELETION: int
ACTION_FLAG_CHOICES: Any

class LogEntryManager(models.Manager["LogEntry"]):
    def log_action(
        self,
        user_id: int,
        content_type_id: int,
        object_id: Union[int, str, UUID],
        object_repr: str,
        action_flag: int,
        change_message: Any = ...,
    ) -> LogEntry: ...

class LogEntry(models.Model):
    action_time: models.DateTimeField[Any] = ...
    user: models.ForeignKey[Any] = ...
    content_type: models.ForeignKey[Any] = ...
    object_id: models.TextField[Any] = ...
    object_repr: models.CharField[Any] = ...
    action_flag: models.PositiveSmallIntegerField[Any] = ...
    change_message: models.TextField[Any] = ...
    objects: LogEntryManager = ...
    def is_addition(self) -> bool: ...
    def is_change(self) -> bool: ...
    def is_deletion(self) -> bool: ...
    def get_change_message(self) -> str: ...
    def get_edited_object(self) -> Model: ...
    def get_admin_url(self) -> Optional[str]: ...
