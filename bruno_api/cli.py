import typer
import uvicorn

from sqlmodel import Session
from .app import app
from .config import settings
from .db import init_db, engine 
from .models.user import User

cli = typer.Typer(name="bruno_api API")


@cli.command()
def run(
    port: int = settings.server.port,
    host: str = settings.server.host,
    log_level: str = settings.server.log_level,
    reload: bool = settings.server.reload,
):  # pragma: no cover
    """Run the API server."""
    uvicorn.run(
        "bruno_api.app:app",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
    )


@cli.command()
def shell():  # pragma: no cover
    """Opens an interactive shell with objects auto imported"""
    _vars = {
        "app": app,
        "settings": settings,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(argv=[], user_ns=_vars)
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()


@cli.command()
def create_user(username: str, password: str, superuser: bool = False):
    """Create user"""
    init_db()
    with Session(engine) as session:
        user = User(username=username, password=password, superuser=superuser)
        session.add(user)
        session.commit()
        session.refresh(user)
        typer.echo(f"created {username} user")
        return user