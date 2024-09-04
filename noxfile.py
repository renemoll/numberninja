import nox


@nox.session
def lint(session: nox.Session) -> None:
    session.install(".[dev]")
    session.run("pre-commit", "run", "--all-files", "--show-diff-on-failure")


@nox.session
def test(session: nox.Session) -> None:
    session.install(".[test]")
    session.run("pytest")


@nox.session
def coverage_report(session: nox.Session) -> None:
    session.install(".[test]")
    session.run("pytest")
    session.run("coverage", "html")
