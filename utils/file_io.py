from __future__ import annotations

import re
import uuid
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Iterable

from logger import GLOBAL_LOGGER as log
from exception.custom_exception import DocumentPortalException


