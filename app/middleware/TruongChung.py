from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import uuid

class TruongChungMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get user_id from header (UUID)
        request.state.user_id = request.headers.get("X-User-Id")
        request.state.ip_address = request.client.host
        response = await call_next(request)
        return response