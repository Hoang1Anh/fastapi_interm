import json
import re
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import Response
from app.models import LichSuHeThong as LichSuHeThongModel
from app.database import SessionLocal


def generate_summary(method: str, path: str) -> str:
    parts = [p for p in path.strip("/").split("/") if p and "{" not in p]

    # Loại bỏ phần cuối nếu là số hoặc UUID
    if parts and re.match(r"^\d+$|^[a-fA-F0-9-]{36}$", parts[-1]):
        parts.pop()

    if not parts:
        return f"{method} Unknown"

    resource = parts[-1].replace("_", " ").title()
    method = method.upper()

    if method == "GET":
        if "filter" in path:
            return f"Filter {resource}"
        return f"Read {resource}"
    elif method == "POST":
        if "filter" in path:
            return f"Filter {resource}"
        return f"Create {resource}"
    elif method == "PUT":
        return f"Update {resource}"
    elif method == "DELETE":
        return f"Delete {resource}"
    else:
        return f"{method} {resource}"


class LichSuHeThongMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        SKIP_PATHS = ["/docs", "/redoc", "/openapi.json", "/favicon.ico", "/static"]
        if any(request.url.path.startswith(skip) for skip in SKIP_PATHS):
            return await call_next(request)

        raw_request = f"{request.method} {request.url.path} HTTP/{request.scope.get('http_version', '1.1')}"
        headers = [f"{key}: {value}" for key, value in request.headers.items()]
        du_lieu_vao = f"{raw_request} " + " ".join(headers)

        try:
            response = await call_next(request)
            response_body = b""
            async for chunk in response.body_iterator:
                response_body += chunk

            new_response = Response(
                content=response_body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type,
            )

            try:
                response_json = json.loads(response_body.decode("utf-8"))
            except Exception:
                response_json = {}

            du_lieu_ra = (
                response_json.get("message")
                or response_json.get("detail")
                or f"HTTP {response.status_code}"
            )

            noi_dung = generate_summary(request.method, request.url.path)
            self._write_log(request, noi_dung, du_lieu_vao, du_lieu_ra)

            return new_response

        except Exception as e:
            noi_dung = generate_summary(request.method, request.url.path)
            self._write_log(request, noi_dung, du_lieu_vao, f"Lỗi: {str(e)}")
            raise

    def _write_log(self, request: Request, noi_dung: str, du_lieu_vao: str, du_lieu_ra: str):
        try:
            db = SessionLocal()
            db.info["request"] = request
            log = LichSuHeThongModel(
                noi_dung=noi_dung,
                url=str(request.url),
                du_lieu_vao=du_lieu_vao,
                du_lieu_ra=du_lieu_ra,
            )
            db.add(log)
            db.commit()
            db.close()
        except Exception as log_err:
            print(f"[Middleware ❌ ERROR] Failed to write log: {log_err}")
