
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

def save_uploaded_files(uploaded_files: Iterable, target_dir: Path) -> list[Path]:
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        saved: list[Path] = []

        for uf in uploaded_files:
            name = getattr(uf, "name", "file")

            ext = Path(name).suffix.lower()

            # validation extension
            if ext not in SUPPORTED_EXTENSIONS:
                log.warning("Unsupported file skipped",
                filename=name
                )
                continue
            # clean filename
            safe_name = re.sub(
                r"[^a-zA-Z0-9_-]",
                "_",
                Path(name).stem
            ).lower()

            # generate unique filename
            fname = f"{safe_name}_{uuid.uuid4().hex[:8]}{ext}"
            out = target_dir / fname

            # Read uploaded content
            if hasattr(uf, "seek"):
                uf.seek(0)

            if hasattr(uf, "read"):
                content = uf.read()
            else:
                content = uf.getbuffer()

            if not content :
                log.warning("Empty file skipped", filename=name)
                continue

            # save file 
            with open(out, "wb") as f:
                f.write(content)
            saved.append(out)

            log.info("File saved for ingestion",
            uploaded=name,
            saved_as=str(out))
        return saved

    except Exception as e:
        log.error("Failed to save uploaded file",
        error=str(e),
        dir=str(target_dir)
        )

        raise DocumentPortalException(
            "Failed to save uploaded files",
            e
        )  from e
