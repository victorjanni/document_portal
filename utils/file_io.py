from enum import unique
from __future__ import annotations

import re
import uuid
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Iterable

from logger import GLOBAL_LOGGER as log
from exception.custom_exception import DocumentPortalException

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}

def generating_the_session_id(prefix: str = "session") -> str:
    ist = ZoneInfo("Asia/Kolkata")

    timestamp = datetime.now(ist).strftime("%Y%m%d_%H%M%S")
    unique_id = uuid.uuid4().hex[:8]

    return f"{prefix}_{timestamp}_{unique_id}"


