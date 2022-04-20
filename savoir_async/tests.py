from anyio import run

from savoir_async import Savoir


def test_make_savoir_request():
    api = Savoir(
        "multichainrpc",
        "79pgKQusiH3VDVpyzsM6e3kRz6gWNctAwgJvymG3iiuz",
        "localhost",
        "8002",
        "MyChain"
    )
    async def _():
        res = await api.getinfo()
        assert res is not None

    run(_)
