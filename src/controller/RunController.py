from fastapi import APIRouter

router = APIRouter(prefix="/run", tags=["run"])


@router.get("/")
def run():
    """Run endpoint."""
    return {"status": "ok", "message": "Run completed"}
