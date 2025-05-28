


# Chạy Alembic migrations (tự tạo migration nếu có thay đổi, hoặc bỏ qua nếu không)
alembic revision --autogenerate -m "Auto migration from container" || echo "No changes to migrate"
alembic upgrade head


# Chạy uvicorn với auto reload (theo dõi thay đổi file)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload